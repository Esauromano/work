# -*- coding: utf-8 -*-
import httplib2
import os
from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage
import pygsheets
from datetime import datetime
from pygsheets.exceptions import *
import config
import sys
import requests
import json
from pygsheets.exceptions import *
from generales import *

class ssj:
    def __init__(self, ui):
        self.ui = ui


    def get_credentials(self):

        SCOPES = 'https://www.googleapis.com/auth/drive.metadata.readonly','https://www.googleapis.com/auth/drive','https://www.googleapis.com/auth/drive.file','https://www.googleapis.com/auth/drive.appdata','https://www.googleapis.com/auth/drive.apps.readonly','https://www.googleapis.com/auth/drive.photos.readonly'
        CLIENT_SECRET_FILE = 'client_secret.json'
        APPLICATION_NAME = 'ARMS3'
        """Gets valid user credentials from storage.

        If nothing has been stored, or if the stored credentials are invalid,
        the OAuth2 flow is completed to obtain the new credentials.

        Returns:
            Credentials, the obtained credential.
        """
        home_dir = os.path.expanduser('~')
        credential_dir = os.path.join(home_dir, '.credentials')
        if not os.path.exists(credential_dir):
            os.makedirs(credential_dir)
        credential_path = os.path.join(credential_dir,
                                       'client_secret.json')
        print(credential_path)

        store = Storage(credential_path)
        credentials = store.get()
        if not credentials or credentials.invalid:
            flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
            flow.user_agent = APPLICATION_NAME
            if flags:
                credentials = tools.run_flow(flow, store, flags)
            else: # Needed only for compatibility with Python 2.6
                credentials = tools.run(flow, store)
            #print('Storing credentials to ' + credential_path)
        return credentials



    def crearSS2(self, tipo, nombre):
        print("tipo")
        print(tipo)
        print("nombre")
        print(nombre)
        print("config.folderOrigen")
        print(config.folderOrigen)

        name = "ARMS " + nombre.upper()

        credentials = self.get_credentials()
        http = credentials.authorize(httplib2.Http())
        service = discovery.build('drive', 'v2', http=http)
        pedidos = {"parents": [{"id": config.folderOrigen}], "title": name}
        destinos = {"parents": [{"id": config.folderOrigen}], "title": name}
        operadores = {"parents": [{"id": config.folderOrigen }], "title": name}

        if tipo == 'destinos':
            results = service.files().copy(fileId=config.SSDestinos, body=destinos).execute()
            print(results)
            return results["id"]
        elif tipo == 'pedidos':
            print(config.SSPedidos)
            print(pedidos)
            results = service.files().copy(fileId=config.SSPedidos, body=pedidos).execute()
            print(results)
            return results["id"]
        elif tipo == 'operadores':
            results = service.files().copy(fileId=config.SSOperadores, body=operadores).execute()
            print(results)
            return results["id"]

    def crearSS3(self, tipo, nombre):
        name = "ARMS " + nombre.upper()

        credentials = self.get_credentials()
        http = credentials.authorize(httplib2.Http())
        service = discovery.build('drive', 'v2', http=http)

        pedidos = {"parents": [{"id": "1s3tO8zvGZj4LgDxlCaCH0l2l1V0ipqTS"}], "title": name}
        operadores = {"parents": [{"id": "1s3tO8zvGZj4LgDxlCaCH0l2l1V0ipqTS"}], "title": name}
        try:
            if tipo == 'pedidos':
                results = service.files().copy(fileId='1kwWJUjJ3DQKXRPnAHt7OfsVnT7_VefA4txxHzC_nLaQ', body=pedidos).execute()
                #print(results)
                return results["id"]
            elif tipo == 'operadores':
                results = service.files().copy(fileId='11MxxaSladUgYgeNBzIYP689sYXhBp6j_h2XCxvo8YWg', body=operadores).execute()
                #print(results)
                return results["id"]

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




    def crearSS(self, tipo, nombre):

        name = "ARMS " + nombre.upper()
        #credentials = self.get_credentials()
        #http = credentials.authorize(httplib2.Http())
        #service = discovery.build('drive', 'v2', http=http)
        try:
            if config.MODE=="DEV":
                pedidos = {"parents": [{"id": "1mwBzmVr85YyFcZkx62A57FPLCO6qOpjh"}], "title": name}
                operadores = {"parents": [{"id": "1mwBzmVr85YyFcZkx62A57FPLCO6qOpjh"}], "title": name}

                if tipo == 'pedidos':
                    #results = service.files().copy(fileId='1kwWJUjJ3DQKXRPnAHt7OfsVnT7_VefA4txxHzC_nLaQ', body=pedidos).execute()
                    results = self.copiarPlantilla('1kwWJUjJ3DQKXRPnAHt7OfsVnT7_VefA4txxHzC_nLaQ', '1mwBzmVr85YyFcZkx62A57FPLCO6qOpjh', name)
                    print(results)
                    return results
                elif tipo == 'operadores':
                    #results = service.files().copy(fileId='11MxxaSladUgYgeNBzIYP689sYXhBp6j_h2XCxvo8YWg', body=operadores).execute()
                    results = self.copiarPlantilla('11MxxaSladUgYgeNBzIYP689sYXhBp6j_h2XCxvo8YWg', '1mwBzmVr85YyFcZkx62A57FPLCO6qOpjh', name)
                    print(results)
                    return results


            elif config.MODE=="PROD":
                pedidos = {"parents": [{"id": "1s3tO8zvGZj4LgDxlCaCH0l2l1V0ipqTS"}], "title": name}
                operadores = {"parents": [{"id": "1s3tO8zvGZj4LgDxlCaCH0l2l1V0ipqTS"}], "title": name}

                if tipo == 'pedidos':
                    #results = service.files().copy(fileId='1kwWJUjJ3DQKXRPnAHt7OfsVnT7_VefA4txxHzC_nLaQ', body=pedidos).execute()
                    results = self.copiarPlantilla('1kwWJUjJ3DQKXRPnAHt7OfsVnT7_VefA4txxHzC_nLaQ', '1s3tO8zvGZj4LgDxlCaCH0l2l1V0ipqTS', name)
                    print(results)
                    return results
                elif tipo == 'operadores':
                    #results = service.files().copy(fileId='11MxxaSladUgYgeNBzIYP689sYXhBp6j_h2XCxvo8YWg', body=operadores).execute()
                    results = self.copiarPlantilla('11MxxaSladUgYgeNBzIYP689sYXhBp6j_h2XCxvo8YWg', '1s3tO8zvGZj4LgDxlCaCH0l2l1V0ipqTS', name)
                    print(results)
                    return results


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




    def copiarPlantilla(self, plantilla, destino, nombre):
        if config.MODE == "DEV":
            url = "https://b2uiut18x9.execute-api.us-east-1.amazonaws.com/dev/copiar-plantilla"
            api_key = 'mtS5hV3rl53tBeGeWnfWq2pqxSRDjOvJW6L7hUb9'
        elif config.MODE == "PROD":
            url = "https://b2uiut18x9.execute-api.us-east-1.amazonaws.com/prod/copiar-plantilla"
            api_key = 'GovScPeaAw54yYqzD5qFb173iusQ93RQrL7PnYI7'
        headers = {'content-type': 'application/json', 'X-API-KEY': api_key}
        datos = {
                  "id_plantilla": plantilla,
                  "nombre_archivo": nombre,
                  "folder_destino": destino
                }
        try:
            r = requests.post(url, data=json.dumps(datos), headers=headers).json()
            if r['status']:
                return r['result']
            else: 
                return False
        # ----------------------------------------------------
        
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




    def salvarDFtoSS(self, df, key):
        try:
            print(key)
            gc = pygsheets.authorize(service_file='IO/ARMS 2 Legacy-327b3624f992.json', no_cache=True)
                            
            #open the google spreadsheet 
            sh = gc.open_by_key(key)
            print("Ya se abrio")
            print(sh)
            #df2 = df.loc[df['Longitud']=='']

            #print(df)
           
            #select the first sheet 
            wks = sh[0]

            #update the first sheet with df, starting at cell B2. 

            #obteniendo el CEDI
            cedi = json.loads(config.loginData)['cedi']
        
            wks.set_dataframe(df, (5, 1), fit=True, copy_head=False)
            wks.update_cell('E2', cedi)
            return True

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
    

