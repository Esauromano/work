
# -*- coding: utf-8 -*-

import httplib2
import os
import json
import copy
import re
import pandas as pd
import os, sys
import config
from apiclient import discovery
from oauth2client import file, client, tools
from oauth2client.file import Storage
from httplib2 import Http
from Base.GeneradorRutas.Optimiza.funciones import fnMuestraMensaje
from IO.Apis import spread_sheet as ss
import string
from itertools import combinations_with_replacement as cwr
import pygsheets
from pygsheets.exceptions import *


def alphabet_columns():

    alphabet = string.ascii_uppercase
    length = 2
    column_names = []
    for letter in alphabet:
        column_names.append(letter)
    for comb in cwr(alphabet, length):
        column_names.append(''.join(comb))

    return column_names


def abrir_SS(nombre_ss, nombre_wks):

    try:
        gcPlan = pygsheets.authorize(service_file='IO/ARMS 2 Legacy-327b3624f992.json', no_cache=True)
        sheet = gcPlan.open(nombre_ss)
        # TODO: selecciona el wks
        wks = sheet.worksheet_by_title(nombre_wks)
        df = wks.get_as_df()
        return True, sheet, wks, df

    except PyGsheetsException as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        error = str(exc_type)
        print(error)
        if error == "<class 'pygsheets.exceptions.SpreadsheetNotFound'>": lblMensaje = 'Spreadsheet {0} no encontrado'.format(
                nombre_ss)
        if error == "<class 'pygsheets.exceptions.WorksheetNotFound'>": lblMensaje = 'Worksheet  {0} no encontrado'.format(
                nombre_wks)
        return False, error, 0,


def check_plan_format(NameSS):

    # ss_list = ['RESULTADOS', 'DESTINOS', 'VEHICULOS', 'CEDI', 'CONFIGURACION', 'COMPATIBILIDAD', 'TARIFARIO', 'OPERADORES']
    ss_list = ['RESULTADOS', 'DESTINOS', 'VEHICULOS', 'CEDI', 'CONFIGURACION', 'COMPATIBILIDAD']
    #column_names = alphabet_columns()
    statusfinal = True
    errors_final = {}
    x=ss.SpreadSheet()

    try:
        if NameSS != '':
            for sheet_name in ss_list:
                print("Antes leyendo .......................................................", sheet_name, NameSS)
                status, wks, dataframe = x.abrirSS(NameSS, sheet_name)
                statusfinal = statusfinal and status
                print("After leyendo .......................................................")
                print(statusfinal, status, dataframe.shape)
                if statusfinal is True:
                    #json_sheet = json.loads(dataframe.to_json(orient='records'))
                    #auto_format_ss(sheet, wks, dataframe, sheet_name)
                    modified, errors_sheet = check_format_ss(dataframe, sheet_name)
                    #print(errors_sheet)
                    errors_final[sheet_name]=errors_sheet
                else:
                    break

            print("Fin For ", statusfinal)

        else:
            statusfinal = False

        for sheet_name in ss_list:
            print("Errores ", sheet_name)
            #for i in errors_final[sheet_name]:
            #    print(i)

            return statusfinal, 0, errors_final

    except Exception as e:
        return False, 0, e

def check_tsv(tsv_data, tipo):
    try:
        status = True
        msj = ''
        tsv_data.fillna(value='', inplace=True)
        modified, errors = check_format_ss(tsv_data, tipo)
        if tipo == 'PEDIDOS':
            duplicados = tsv_data.duplicated(subset='Pedido', keep='first')
            if len(tsv_data[duplicados]) > 0:
                status = False
                d = tsv_data[duplicados].index.tolist()
                errors['Duplicados'] =  {'Necessary': '', 'Index': ''}
                errors['Duplicados']['Index'] = d[:20]
        for key, value in errors.items():
            status = status and not bool(value['Necessary'])
        if not status:
            msj = mensajes_error(errors, tipo)    
        return status, msj
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        error = '{} - {} - linea {} ({})'.format(exc_type, fname, exc_tb.tb_lineno, str(e))
        print(error)
        return False, error

def check_format_ss(spread_data, sheet_name):

    """

    Inputs:
    :param data = dataframe with the records to be written in SS:


    :param sheet_name: Name of the SS to be written:
    one of the following:

    'USUARIOS'
    'EMPRESAS'
    'OPERADORES'
    'PEDIDOS'
    'COMPATIBILIDAD'
    'DESTINOS'
    'PREFERENCIAS'
    'VEHICULOS'

    Outputs:

    self.errors = JSON with errors found in the regular expression match

    The JSON has the following fields:
        Column: Field name of the value with error
        ExpectedRegEx: Regular expression expected for the field
        ActualValue: Value tried to be written in the SS
        Row: Row number of the SS

    example (if there is no errors):
    {} =
    example (if there is errors in 3 different rows)

  {
    "ss_name": [
        {
        "Row": "1",
        "Columns: [A, B, C, AJ]",
        }
        {
        "Row": "6",
        "Columns: [D, E, Z]",
        }
        {
        "Row": "19",
        "Columns: [A]",
        }
    ]
    }

    """
    try:
        modified = False
        acdir = os.path.abspath(os.path.join('IO', 'validaciones'))
        file_validation = acdir + '/VALIDACION_' + sheet_name + '.json'

        with open(file_validation, "r", encoding='utf-8') as data_file:
            validation_data = json.loads(data_file.read())
        necessary = [field for field, values in validation_data.items() if values['Necessary']]
        missing = list(set(necessary) - set(spread_data.columns))
        # Add missing columns
        if missing:
            modified = True
            for col_name in missing:
                spread_data[col_name] = validation_data[col_name]['Default']
        # Format necessary columns
        for col_name in necessary:
            # Fill empty with default
            col = spread_data[col_name]
            col.replace('', validation_data[col_name]['Default'], inplace=True)
            format_type = validation_data[col_name]['Type']
            format_string = validation_data[col_name]['Pattern']
            if format_type == 'DATETIME':
                dts = pd.to_datetime(spread_data[col_name], errors='coerce',dayfirst=True)
                dts = dts[~dts.isnull()].dt.strftime(format_string)
                spread_data.loc[dts.index, col_name]=dts
        # Find index of errors
        error_index = dict()
        for col_name, val in validation_data.items():
            if col_name in spread_data.columns:
                col = spread_data[col_name].astype(str)
                if col_name in necessary:
                    pat = val['RegEx']
                    error_values=col[~col.str.contains(pat)]
                    error=error_values.index.values
                    if bool(error.size):
                        error_index[col_name] = {'Necessary': '', 'Index': ''}
                        error_index[col_name]['Necessary'] = val['Necessary']
                        error_index[col_name]['Index'] = error.tolist()
                else:
                    col=col[col!='']
                    pat = val['RegEx']
                    error = col[~col.str.contains(pat)].index.values
                    if bool(error.size):
                        error_index[col_name] = {'Necessary': '', 'Index': ''}
                        error_index[col_name]['Necessary'] = val['Necessary']
                        error_index[col_name]['Index'] = error.tolist()
        return modified, error_index
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        error = '{} - {} - linea {} ({})'.format(exc_type, fname, exc_tb.tb_lineno, str(e))
        print(error)
        return False, {}


def auto_format_ss(sheet, wks, df_sheet, sheet_name):

    DATAFormat = [
        {'repeatCell': {
            'range': {
                'sheetId': 0,
                'startRowIndex': 1,
                'endRowIndex': 1,
                'startColumnIndex': 1,
                'endColumnIndex': 1},
            "cell": {
                "userEnteredFormat": {
                    "numberFormat": {
                        "type": "DATE",
                        "pattern": "hh:mm:ss am/pm, ddd mmm dd yyyy"
                    }
                }
            },
            "fields": "userEnteredFormat.numberFormat"
        }}
    ]

    acdir = os.path.dirname(__file__)
    file_validation = acdir + '/VALIDACION_'+sheet_name+'.json'
    print(file_validation)
    with open(file_validation) as data_file:
        validation_data = json.loads(data_file.read())

    lastrow = len(df_sheet.index)
    fields_ss = df_sheet.columns
    contcol = 0
    countcolformat = 0
    # print(fields_ss)
    for field in fields_ss:

        # print(field)
        contcol = contcol + 1

        if field in validation_data:

            if validation_data[field]['Type'] != 'STRING':

                # print(validation_data[field])

                if countcolformat > 0:
                    DATAFormat.append(copy.deepcopy(DATAFormat[countcolformat - 1]))

                DATAFormat[countcolformat]['repeatCell']['range']['sheetId'] = wks.id
                DATAFormat[countcolformat]['repeatCell']['range']['endRowIndex'] = lastrow
                DATAFormat[countcolformat]['repeatCell']['range']['startColumnIndex'] = \
                                                                                        contcol - 1
                DATAFormat[countcolformat]['repeatCell']['range']['endColumnIndex'] = \
                                                                                      contcol
                DATAFormat[countcolformat]['repeatCell']['cell']['userEnteredFormat'] \
                    ['numberFormat']['type'] = validation_data[field]['Type']
                DATAFormat[countcolformat]['repeatCell']['cell']['userEnteredFormat'] \
                    ['numberFormat']['pattern'] = validation_data[field]['Pattern']
                countcolformat = countcolformat + 1

    if countcolformat > 0:
        # for i in DATAFormat:
        #    print(i)
        jsonRes = sheet.custom_request(DATAFormat, None)


def mensajes_error(error_index, tipo):
    mensaje = ''
    if tipo=='PEDIDOS':
        dkey = error_index.get('Duplicados')
        if dkey:
            mensaje = "Se encontraron datos duplicados en las filas: \n {0}.\n".format(", ".join(str(x+1) for x in dkey['Index']))
        
    if error_index:
        mensaje_error=''
        for col, val in error_index.items():
            if val['Necessary']:
                mensaje_error = mensaje_error + '\n - ' + col + ' en fila(s): {0}'.format(
                    ", ".join(str(x+1) for x in val['Index']))
        if mensaje_error:
            mensaje = mensaje+"Los siguientes datos estan vacios o el formato no es correcto en el archivo de {0}: \n {1}".format(tipo, mensaje_error)
    return mensaje

def mensajes_error_destinos(dat):
    status = dat['status']
    if not status:
        rows = []
        mensaje_error = ''
        if len(dat['data']) > 20:
            for row in dat['data'][:20]:
                if 'cedi' in row['falta'][0]:
                    mensaje_error = mensaje_error + '\n - {0} '.format(row['falta'][0])
                else:
                    mensaje_error = mensaje_error + '\n - {0} hubicado en fila {1}'.format(row['falta'][0], row['row']+5)
                    mensaje = "Parece que hay un error en los datos, revisa e intenta nuevamente \n {0} \n - etc.".format(mensaje_error)
        else:
            for row in dat['data']:
                if 'cedi' in row['falta'][0]:
                    mensaje_error = mensaje_error + '\n - {0} '.format(row['falta'][0])
                else:
                    mensaje_error = mensaje_error + '\n - {0} hubicado en fila {1}'.format(row['falta'][0], row['row']+5)
                    mensaje = "Parece que hay un error en los datos, revisa e intenta nuevamente \n {0}".format(mensaje_error)
                    fnMuestraMensaje(mensaje)
        return False
    return True



def fnMuestraMensaje(mensaje):
    msgBox = QMessageBox()
    msgBox.setText(mensaje)
    msgBox.exec_()
