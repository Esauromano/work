# -*- coding: utf-8 -*-
import requests
import json
import sys
import os
import config
import pygsheets
from datetime import datetime
from pygsheets.exceptions import *
import pandas as pd
from generales import *

class SpreadSheet:
    
    def AbrirSS(self, id, sheetname, tipo):
        try:

            if(config.MODE == 'DEV'):
                url = 'https://b2uiut18x9.execute-api.us-east-1.amazonaws.com/dev/leer-spreadsheet'
            elif(config.MODE == 'PROD'):
                url = 'https://b2uiut18x9.execute-api.us-east-1.amazonaws.com/prod/leer-spreadsheet'

            payload = {"spreadsheetId": id, "sheetName": sheetname, "tipo": tipo}
            headers = {'content-type': 'application/json', 'X-API-KEY': 'mtS5hV3rl53tBeGeWnfWq2pqxSRDjOvJW6L7hUb9'}

            r = requests.post(url, data=json.dumps(payload), headers=headers)
            resultado = r.text
            duracion = datetime.now() - start_time
            return True, duracion, resultado

        except Exception as e:
            return False, error, False
        except requests.exceptions.HTTPError as errh:
            print ("Http Error:",errh)
            progress_fn(0, "Verifica tu conexion")
        except requests.exceptions.ConnectionError as errc:
            print ("Error de conexion: ",errc)
            progress_fn(0, "Verifica tu conexion")
        except requests.exceptions.Timeout as errt:
            print ("Timeout Error:",errt)
            progress_fn(0, "Verifica tu conexion - Timeout -")
        except requests.exceptions.RequestException as err:
            print ("OOps: Something Else",err)
            progress_fn(0, "Verifica tu conexion")

    def AbrirSSResultados(self, spreadID, sheetName):
        try:
            print('Obteniendo viajes desde el SSResultados ' + str(spreadID) + ": " + str(datetime.now()))
            headers = {'content-type': 'application/json', 'X-API-KEY': 'mtS5hV3rl53tBeGeWnfWq2pqxSRDjOvJW6L7hUb9'}
            if(config.MODE == 'DEV'):
                url = 'https://b2uiut18x9.execute-api.us-east-1.amazonaws.com/dev/obtener-viajes'
            elif(config.MODE == 'PROD'):
                url = 'https://b2uiut18x9.execute-api.us-east-1.amazonaws.com/prod/obtener-viajes'


            datos = {"spreadsheetId":spreadID,"sheetName":sheetName,"tipo":"resultados/optimizador"}
            

            r = requests.post(url, data=json.dumps(datos), headers=headers).json()
            print("termina lectura de viajes en ssResultados")
            
            duracion = datetime.now() - start_time
            print(duracion)
            return r
        except Exception as e:
            return False, error, False
        except requests.exceptions.HTTPError as errh:
            print ("Http Error:",errh)
            progress_fn(0, "Verifica tu conexion")
        except requests.exceptions.ConnectionError as errc:
            print ("Error de conexion: ",errc)
            progress_fn(0, "Verifica tu conexion")
        except requests.exceptions.Timeout as errt:
            print ("Timeout Error:",errt)
            progress_fn(0, "Verifica tu conexion - Timeout -")
        except requests.exceptions.RequestException as err:
            print ("OOps: Something Else",err)
            progress_fn(0, "Verifica tu conexion")

    def obtenerLista(self, tipo,cedi,empresa):
        try:
           
            headers = {'content-type': 'application/json', 'X-API-KEY': 'mtS5hV3rl53tBeGeWnfWq2pqxSRDjOvJW6L7hUb9'}
            
            if(config.MODE == 'DEV'):
                url = 'https://o0480vy3fe.execute-api.us-east-1.amazonaws.com/dev/listar-ss'
            elif(config.MODE == 'PROD'):
                url = 'https://o0480vy3fe.execute-api.us-east-1.amazonaws.com/prod/listar-ss'

            datos = {"tipo": tipo,"cedi": cedi, "empresa": empresa}
            try:
                r = requests.post(url, data=json.dumps(datos), headers=headers).json()
                return r
            except requests.exceptions.HTTPError as err:
                print("fallo")
                print(err)
            return r

        except Exception as e:
            return False, error, False
        except requests.exceptions.HTTPError as errh:
            print ("Http Error:",errh)
            progress_fn(0, "Verifica tu conexion")
        except requests.exceptions.ConnectionError as errc:
            print ("Error de conexion: ",errc)
            progress_fn(0, "Verifica tu conexion")
        except requests.exceptions.Timeout as errt:
            print ("Timeout Error:",errt)
            progress_fn(0, "Verifica tu conexion - Timeout -")
        except requests.exceptions.RequestException as err:
            print ("OOps: Something Else",err)
            progress_fn(0, "Verifica tu conexion")

    def abrirSS(self, nombre_ss, nombre_wks, tipo_nombre_ss, abierto=False, encabezado=False):
        start_time = datetime.now()
        try:
            # TODO: pide autorizacion
            if not abierto:
                config.gc = pygsheets.authorize(service_file='IO/ARMS 2 Legacy-327b3624f992.json', no_cache=True)
                # TODO: abre el ss
                if tipo_nombre_ss == 'key':
                    config.sheet = config.gc.open_by_key(nombre_ss)
                elif tipo_nombre_ss == 'url':
                    config.sheet = config.gc.open_by_url(nombre_ss)
                else:
                    config.sheet = config.gc.open(nombre_ss)
            # TODO: selecciona el wks
            wks = config.sheet.worksheet_by_title(nombre_wks)
            df = wks.get_as_df()
            # TODO: borra los 4 primeros renglones. Siempre en todos los SS de ARMS
            if not encabezado:
                df.drop(df.index[0:3], inplace=True)

            # para cronometro
            duracion = datetime.now() - start_time
            return True, duracion, df

            # guarda como json
            # df.to_json('Datos/resultados.json')
            #

        # ----------------------------------------------------
        except PyGsheetsException as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            error = str(exc_type)

            if error == "<class 'pygsheets.exceptions.SpreadsheetNotFound'>":
                error = (e.SpreadsheetNotFound())

            duracion = datetime.now() - start_time
            return False, duracion, error


    def listarSS(self):
        start_time = datetime.now()
        destinos = []
        try:
            
            # TODO: pide autorizacion
            config.gc = pygsheets.authorize(service_file='IO/ARMS 2 Legacy-327b3624f992.json', no_cache=True)
            # TODO: lista los SS
            todas = config.gc.list_ssheets()
            #print(todas)
            for algo in todas:
                #print(algo)

                if 'ARMS DESTINOS' in algo["name"]:
                    destinos.append(algo)
            return destinos
                    
           

            # guarda como json
            # df.to_json('Datos/resultados.json')
            #33

        # ----------------------------------------------------
        except Exception as e:
            file_name = os.path.basename(sys.argv[0])
            this_function_name = sys._getframe().f_code.co_name
            error = '{} - {} - {}'.format(file_name,this_function_name,str(e))
            return False, error, False

    def obtenerLista(self, tipo,cedi,empresa):
        try:
            headers = {'content-type': 'application/json', 'X-API-KEY': 'mtS5hV3rl53tBeGeWnfWq2pqxSRDjOvJW6L7hUb9'}
            
            if(config.MODE == 'DEV'):
                url = 'https://o0480vy3fe.execute-api.us-east-1.amazonaws.com/dev/listar-ss'
            elif(config.MODE == 'PROD'):
                url = 'https://o0480vy3fe.execute-api.us-east-1.amazonaws.com/prod/listar-ss'
            datos = {"tipo": tipo,"cedi": cedi, "empresa": empresa}
            try:
                r = requests.post(url, data=json.dumps(datos), headers=headers).json()
                return r
            except requests.exceptions.HTTPError as err:
                print("fallo")
                print(err)
            return r

        except Exception as e:
            return False, error, False
        except requests.exceptions.HTTPError as errh:
            print ("Http Error:",errh)
            progress_fn(0, "Verifica tu conexion")
        except requests.exceptions.ConnectionError as errc:
            print ("Error de conexion: ",errc)
            progress_fn(0, "Verifica tu conexion")
        except requests.exceptions.Timeout as errt:
            print ("Timeout Error:",errt)
            progress_fn(0, "Verifica tu conexion - Timeout -")
        except requests.exceptions.RequestException as err:
            print ("OOps: Something Else",err)
            progress_fn(0, "Verifica tu conexion")


    def crearSS(self, nombre, idFolderPadre):
        gc = pygsheets.authorize(service_file='IO/ARMS 2 Legacy-327b3624f992.json', no_cache=True)
        sh = gc.create(nombre, idFolderPadre)
        print('Esto es lo que hay en el sh de la clase Spreadsheet')
        print(str(sh.id))
        detinos = gc.open_by_key('1gqduIf0LvAbb4higuzJEjcFDeGZIy50pitOy05lQdWc')
        pedidos = gc.open_by_key('1FlI0-0ZKL7QhrcDNWpHPIvzwuTAx-87rVWiLwckKEQM')
        operadores  = gc.open_by_key('14n5dNqFuh6Xv7OQwMScrhdTH1nD2-LfLYzZOHqUU6zc')
        wks = pedidos[0]
        #df.to_csv(file_name, sep='\t', encoding='utf-8')
        wks.copy_to(sh.id)
        return sh

        
        
    def copiarPlantilla(self, plantilla, destino):
        if config.MODE == "DEV":
            url = "https://b2uiut18x9.execute-api.us-east-1.amazonaws.com/dev/copiar-plantilla"
            api_key = 'mtS5hV3rl53tBeGeWnfWq2pqxSRDjOvJW6L7hUb9'
        elif config.MODE == "PROD":
            url = "https://b2uiut18x9.execute-api.us-east-1.amazonaws.com/prod/copiar-plantilla"
            api_key = 'GovScPeaAw54yYqzD5qFb173iusQ93RQrL7PnYI7'
        headers = {'content-type': 'application/json', 'X-API-KEY': api_key}
        datos = {
                  "id_plantilla": plantilla,
                  "nombre_archivo": config.nombrePlan,
                  "folder_destino": destino
                }
        try:
            r = requests.post(url, data=json.dumps(datos), headers=headers).json()
            if r['status']:
                return r['result']
            else: return False
        
        
        except Exception as e:
            return False, error, False
        except requests.exceptions.HTTPError as errh:
            print ("Http Error:",errh)
            progress_fn(0, "Verifica tu conexion")
        except requests.exceptions.ConnectionError as errc:
            print ("Error de conexion: ",errc)
            progress_fn(0, "Verifica tu conexion")
        except requests.exceptions.Timeout as errt:
            print ("Timeout Error:",errt)
            progress_fn(0, "Verifica tu conexion - Timeout -")
        except requests.exceptions.RequestException as err:
            print ("OOps: Something Else",err)
            progress_fn(0, "Verifica tu conexion")





    def salvarDFtoSS(self, df, key):
        try:
            gc = pygsheets.authorize(service_file='IO/ARMS 2 Legacy-327b3624f992.json', no_cache=True)
                        
            #open the google spreadsheet 
            sh = gc.open_by_key(key)

            #df2 = df.loc[df['Longitud']=='']

            #print(df2)
           
            #select the first sheet 
            wks = sh[0]

            #update the first sheet with df, starting at cell B2. 
            wks.set_dataframe(df, (5, 1), fit=True, copy_head=False)
            return True
            
        except Exception as e:
            return False, error, False
        except requests.exceptions.HTTPError as errh:
            print ("Http Error:",errh)
            progress_fn(0, "Verifica tu conexion")
        except requests.exceptions.ConnectionError as errc:
            print ("Error de conexion: ",errc)
            progress_fn(0, "Verifica tu conexion")
        except requests.exceptions.Timeout as errt:
            print ("Timeout Error:",errt)
            progress_fn(0, "Verifica tu conexion - Timeout -")
        except requests.exceptions.RequestException as err:
            print ("OOps: Something Else",err)
            progress_fn(0, "Verifica tu conexion")
        