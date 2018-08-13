# -*- coding: utf-8 -*-
import requests
import json
from datetime import datetime
import os
import sys
from argparse import ArgumentParser
from boto3 import client
import boto3
import pandas as pd
from io import StringIO
from IO.Apis.spread_sheet import SpreadSheet as ss
from PyQt5 import QtCore, QtWidgets, QtWebEngineWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from IO.Apis.Db import DB
from IO.Apis.spread_sheet import SpreadSheet
from PyQt5.QtWidgets import QTableWidget,QTableWidgetItem, QMessageBox
from Base.Interfaz.Pochteca.ss import ssj
import cchardet
import numpy as np
import config
from time import gmtime, strftime, localtime
from pygsheets.exceptions import *
from generales import *

class destinos:
    def __init__(self):
        self.ui = config.mainWindow
    
    def mandarDestinos(self, destinos):
        self.ui.progress_fn(80,"Enviando destinos")
        try:
            destinos = json.loads(destinos)

            for destino in destinos:
                destino['Subregion'] = json.loads(config.loginData)['cedi']


            if(config.MODE == 'DEV'):
                url = 'https://b2uiut18x9.execute-api.us-east-1.amazonaws.com/dev/pochteca-alta-destinos'
            elif(config.MODE == 'PROD'):
                url = 'https://b2uiut18x9.execute-api.us-east-1.amazonaws.com/prod/pochteca-alta-destinos'
            
            payload = { "idEmpresa": 10, "destinos": destinos}
            headers = {'content-type': 'application/json', 'X-API-KEY': 'mtS5hV3rl53tBeGeWnfWq2pqxSRDjOvJW6L7hUb9'}

            r = requests.post(url, data=json.dumps(payload), headers=headers)
            resultado = json.loads(r.text)
            self.ui.progress_fn(100,"Destinos enviados")
            #print(resultado)
            return resultado
        except Exception as e:
            print(e)
            return None
        except requests.exceptions.HTTPError as errh:
            print ("Http Error:",errh)
            progress_fn(0, "Verifica tu conexion")
            return False
        except requests.exceptions.ConnectionError as errc:
            print ("Error de conexion: ",errc)
            progress_fn(0, "Verifica tu conexion")
            return False
        except requests.exceptions.Timeout as errt:
            print ("Timeout Error:",errt)
            progress_fn(0, "Verifica tu conexion - Timeout -")
            return False
        except requests.exceptions.RequestException as err:
            print ("OOps: Something Else",err)
            progress_fn(0, "Verifica tu conexion")
            return False

    def consultarDestinos(self, destinos):
        #print('consultando destinos')

        try:
            payload = { "idEmpresa": json.loads(config.loginData)['idEmpresa'], "Subregion": json.loads(config.loginData)['cedi'], "Destinos": destinos}
            headers = {'content-type': 'application/json', 'X-API-KEY': 'mtS5hV3rl53tBeGeWnfWq2pqxSRDjOvJW6L7hUb9', }

            if(config.MODE == 'DEV'):
                url = 'https://b2uiut18x9.execute-api.us-east-1.amazonaws.com/dev/pochteca-listar-destinos'
            elif(config.MODE == 'PROD'):
                url = 'https://b2uiut18x9.execute-api.us-east-1.amazonaws.com/prod/pochteca-listar-destinos'
            r = requests.post(url, data=json.dumps(payload), headers=headers)
            resultado = json.loads(r.text)
            
            # validar respuestas
            if "no existen destinos para " in resultado['Resultado']:
                return None, True
            else:
                return resultado['Resultado'],True    
            
        except Exception as e:
            return None,False
        except requests.exceptions.HTTPError as errh:
            print ("Http Error:",errh)
            progress_fn(0, "Verifica tu conexion")
            return False
        except requests.exceptions.ConnectionError as errc:
            print ("Error de conexion: ",errc)
            progress_fn(0, "Verifica tu conexion")
            return False
        except requests.exceptions.Timeout as errt:
            print ("Timeout Error:",errt)
            progress_fn(0, "Verifica tu conexion - Timeout -")
            return False
        except requests.exceptions.RequestException as err:
            print ("OOps: Something Else",err)
            progress_fn(0, "Verifica tu conexion")
            return False

    def listarDestinos(self):
        try:
            sp = SpreadSheet()
            lss = sp.listarSS()
            tamaño = len(lss) + 1
            self.destinos = lss
            self.ui.tableWidgetPochtecaAnadeDe.setRowCount(tamaño)
            self.ui.tableWidgetPochtecaAnadeDe.setColumnCount(2)
            '''self.ui.tableWidgetPochtecaAnadeDe.setItem(0,0, QTableWidgetItem("Nombre"))
                                    self.ui.tableWidgetPochtecaAnadeDe.setItem(0,1, QTableWidgetItem("ID"))'''
            self.ui.tableWidgetPochtecaAnadeDe.setColumnWidth(0, 300)
            self.ui.tableWidgetPochtecaAnadeDe.setColumnWidth(1, 400)
            self.ui.tableWidgetPochtecaAnadeDe.setSelectionBehavior(QTableWidget.SelectRows)
            self.ui.tableWidgetPochtecaAnadeDe.setSelectionMode(QTableWidget.SingleSelection)


            self.ui.tableWidgetPochtecaAnadeA.setRowCount(tamaño)
            self.ui.tableWidgetPochtecaAnadeA.setColumnCount(2)
            '''self.ui.tableWidgetPochtecaAnadeA.setItem(0,0, QTableWidgetItem("Nombre"))
                                    self.ui.tableWidgetPochtecaAnadeA.setItem(0,1, QTableWidgetItem("ID"))'''
            self.ui.tableWidgetPochtecaAnadeA.setColumnWidth(0, 300)
            self.ui.tableWidgetPochtecaAnadeA.setColumnWidth(1, 400)
            self.ui.tableWidgetPochtecaAnadeA.setSelectionBehavior(QTableWidget.SelectRows)
            self.ui.tableWidgetPochtecaAnadeA.setSelectionMode(QTableWidget.SingleSelection)
            for idx, cosa in enumerate(lss):
                esto = str(cosa["name"])
                esto2 = str(cosa["id"])
                #print(esto2)
                index = idx
                self.ui.tableWidgetPochtecaAnadeDe.setItem(index,0, QTableWidgetItem(esto))
                self.ui.tableWidgetPochtecaAnadeDe.setItem(index,1, QTableWidgetItem(esto2))

                self.ui.tableWidgetPochtecaAnadeA.setItem(index,0, QTableWidgetItem(esto))
                self.ui.tableWidgetPochtecaAnadeA.setItem(index,1, QTableWidgetItem(esto2))
        except Exception as e:
            raise e

    def syncDestinos(self):
        for x in self.ui.listDestinos.selectedIndexes():
            #print(x)
            #df =  self.open(x.data())
            #self.process(x.data())
            self.pruebasPochDestinos(x.data())

    def getResultDestinos2(self, tipo, obj):
        if obj.shape[0]>0:
            df2 = obj.replace(np.nan, '', regex=True)
            TSVconCoordenadas = df2.loc[(df2['Longitud'].notnull()) & (df2['Latitud'].notnull()) & (df2['Destino'].notnull()) & (df2['CalleNumero'].notnull()) & (df2['Colonia'].notnull()) & (df2['Estado'].notnull()) & (df2['CodigoPostal'].notnull()) & (df2['Destino'].notnull())]
            #print(TSVconCoordenadas)
            coor = TSVconCoordenadas.to_json(orient='records')
            #print(coor)
            result = self.mandarDestinos(coor)
            #print(result)
            if result is not None:
                #TODO validar campo status
                self.ui.progress_fn(100,"Destinos actualizados")
            else:
                self.ui.progress_fn(100,"Fallo al actualizar destinos")

    def pruebasPochDestinos(self):
        self.ui.tablePochtecaLatLong.clear()
        self.ui.tablePochtecaLatLong_2.clear()
        for x in self.ui.listDestinos.selectedIndexes():
            #print(x)
            #df =  self.open(x.data())
            
            data = self.botof.openS3(x.data())
            df2 = data.replace(np.nan, '', regex=True)
            
 
            for index, row in df2.loc[df2['Longitud']==''].iterrows():
                direccion = str(row['CalleNumero'])
                #print(index + ' ' +direccion)
                latitud, longitud = self.coordenadas(direccion)

                if 'Se necesitan mas datos' not in latitud:
                    self.procesaCoordenadas(index, row, df2)
                else:
                    df2.set_value(index, 'Latitud', latitud, takeable=False)
                    df2.set_value(index, 'Longitud', longitud, takeable=False)
                    self.ui.tablePochtecaLatLong_2.addItem(row['CalleNumero'])
                
                #crea archivo faltantes
                df = df2.to_json(orient='records')
                conCoordenadas = df2.loc[df2['Longitud'] != 'Se necesitan mas datos']
                sinCoordenadas = df2.loc[df2['Longitud'] == 'Se necesitan mas datos']
                nombre = config.MODE+".DestinosRechazados."+strftime("%Y-%m-%d_%H:%M:%S", localtime())

                #guardar sincoordenadas como rechazados en s3
                self.botof.saveS3(sinCoordenadas,nombre)

    def procesaCoordenadas(self, index, row, dataFrame):

        direccion = str(row['CalleNumero'])
        latitud, longitud = self.coordenadas(direccion)
        if latitud != "Se necesitan mas datos" and longitud != "Se necesitan mas datos":
            if self.enMX(latitud, longitud):

                latitud = latitud.replace(".", ",")
                longitud = longitud.replace(".", ",")
                #print(latitud + longitud)

                dataFrame.set_value(index, 'Latitud', latitud, takeable=False)
                dataFrame.set_value(index, 'Longitud', longitud, takeable=False)

                self.ui.tablePochtecaLatLong.addItem(row['CalleNumero'])
            else:
                latitud = 'Se necesitan mas datos'
                longitud = 'Se necesitan mas datos'
                #print(latitud + longitud)

                dataFrame.set_value(index, 'Latitud', latitud, takeable=False)
                dataFrame.set_value(index, 'Longitud', longitud, takeable=False)

                self.ui.tablePochtecaLatLong_2.addItem(row['CalleNumero'])

    def coordenadas(self, direccion):
        self.ui.progress_fn(60,"Calculando coordenadas")
        try:

            val = direccion.replace(" ", "+")
            key="AIzaSyD-GOe2kJOEyrTZR_wcx4k789RpVcO3qk0"
            url = 'https://maps.googleapis.com/maps/api/geocode/json?address='+val+'&key='+key
            payload = {}
            headers = {'content-type': 'application/json'}

            r = requests.post(url, data=json.dumps(payload), headers=headers)
            resultado = r.text
            j = json.loads(resultado)
            #print(j)
            if j['status'] == "OK":
                latitud = str(j['results'][0]['geometry']['location']['lat'])
                longitud = str(j['results'][0]['geometry']['location']['lng'])
                #print(latitud, longitud)
                #print(' ')
                return (latitud, longitud)
            else:
                return('Se necesitan mas datos','Se necesitan mas datos')
        except Exception as e:
            raise e
        except requests.exceptions.HTTPError as errh:
            print ("Http Error:",errh)
            progress_fn(0, "Verifica tu conexion")
            return False
        except requests.exceptions.ConnectionError as errc:
            print ("Error de conexion: ",errc)
            progress_fn(0, "Verifica tu conexion")
            return False
        except requests.exceptions.Timeout as errt:
            print ("Timeout Error:",errt)
            progress_fn(0, "Verifica tu conexion - Timeout -")
            return False
        except requests.exceptions.RequestException as err:
            print ("OOps: Something Else",err)
            progress_fn(0, "Verifica tu conexion")
            return False


    def getResultDestinos(self,tipo,obj):
        self.ui.progress_fn(10,"Procesando el archivo de destinos")
        Recalcular = []
        NoRecalcular = []
        #print("procesar datos del dataframe")
        if obj.shape[0]>0:
            df2 = obj.replace(np.nan, '', regex=True)

            TSVconCoordenadas = df2.loc[(df2['Longitud'].notnull()) & (df2['Latitud'].notnull()) & (df2['Destino'].notnull()) & (df2['CalleNumero'].notnull()) & (df2['Colonia'].notnull()) & (df2['Estado'].notnull()) & (df2['CodigoPostal'].notnull()) & (df2['Destino'].notnull())]
            #print(TSVconCoordenadas)
            coor = TSVconCoordenadas.to_json(orient='records')
            #print(coor)
            result = self.mandarDestinos(coor)
            #print(result)
            if result is not None:
                #TODO validar campo status
                self.ui.progress_fn(100,"Destinos actualizados")
                return True
            else:
                self.ui.progress_fn(100,"Fallo al actualizar destinos")
                return False
                
            destinos = json.loads(df2.to_json(orient='records'))
            listaDestinos = []
            for destino in destinos:
                listaDestinos.append(destino['Destino'])
            #print(listaDestinos)

            datosDB,status = self.consultarDestinos(listaDestinos)

            #print(datosDB)
           
            if datosDB is not None and status is True and datosDB != "OK":
                #print('hay algunos candidatos')
                self.ui.progress_fn(50,"Comparando contra la base de datos")
                #print("comparar")
                #buscar en el DF que destinos no tiene latitud para ser calculada
                for index, row in df2.loc[df2['Longitud']==''].iterrows():
                    
                    #print(datosDB)
                    for dato in datosDB:
                        #print(dato)
                        if (dato['Destino'] == str(row['Destino'])):
                        #if str(row['Destino']) == str(dato['Destino']):
                            if ['CalleNumero'] == dato['CalleNumero']:
                                NoRecalcular.append(index)
                                latitud = 'Se necesitan mas datos'
                                longitud = 'Se necesitan mas datos'
                                df2.set_value(index, 'Latitud', latitud, takeable=False)
                                df2.set_value(index, 'Longitud', longitud, takeable=False)

                            else:

                                Recalcular.append(index)
                                #print('aqui ta, pero cambio, si recalcula geocode')
                                self.procesaCoordenadas(index, row, df2)
                        else:
                            self.ui.progress_fn(100,"Todos los destinos de este archivo han sido procesados")

            else:
                #todos son candidatos 
                #print('todos son candidatos')
                for index, row in df2.loc[df2['Longitud']==''].iterrows():
                    direccion = str(row['CalleNumero'])
                    latitud, longitud = self.coordenadas(direccion)

                    if 'Se necesitan mas datos' not in latitud:
                        self.procesaCoordenadas(index, row, df2)
                    else:
                        df2.set_value(index, 'Latitud', latitud, takeable=False)
                        df2.set_value(index, 'Longitud', longitud, takeable=False)
                        self.ui.tablePochtecaLatLong_2.addItem(row['CalleNumero'])
                
                #crea archivo faltantes
                df = df2.to_json(orient='records')
                conCoordenadas = df2.loc[df2['Longitud'] != 'Se necesitan mas datos']
                sinCoordenadas = df2.loc[df2['Longitud'] == 'Se necesitan mas datos']
                nombre = config.MODE+".DestinosRechazados."+strftime("%Y-%m-%d_%H:%M:%S", localtime())

                #guardar sincoordenadas como rechazados en s3
                self.botof.saveS3(sinCoordenadas,nombre)

                #guardar en BD
                df = conCoordenadas.to_json(orient='records')
                if self.mandarDestinos(df) is not None:
                    #TODO validar campo status
                    self.ui.progress_fn(100,"Destinos actualizados")

                    return True
                else:
                    self.ui.progress_fn(100,"Fallo al actualizar destinos")
                    return False

            #si no hay conexion con al base de datos no deberia de borrar el archivo
            if status:
                return True
            else:
                return False
            
            #print(NoRecalcular)
            #print(Recalcular)        

        else:
            self.ui.progress_fn(100,"el archivo tsv no cuenta con destinos")
            return True

    def enMX(self, lat, lon):
        if float(lat) < 32.523658 and float(lat) > 11.968611 and float(lon) > -122.170278 and float(lon) < -84.641667:
            return True
        else:
            return False