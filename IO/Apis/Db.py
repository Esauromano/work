# -*- coding: utf-8 -*-
import requests
import json
from datetime import datetime
import config
from generales import *
from pygsheets.exceptions import *

class DB:

    def obtenerViajes(self,idEmpresa,status,cedi):
        start_time = datetime.now()
        print('Obteniendo viajes con estatus ' + str(status) + ": " + str(datetime.now()))
        headers = {'content-type': 'application/json', 'X-API-KEY': 'mtS5hV3rl53tBeGeWnfWq2pqxSRDjOvJW6L7hUb9'}
        url = "https://b2uiut18x9.execute-api.us-east-1.amazonaws.com/dev/obtener-viajes"
        datos = {"empresaId": idEmpresa, "status": status, "cedi": cedi}
        try:
            r = requests.post(url, data=json.dumps(datos), headers=headers).json()
            print("viajes obtenidos")
        
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

        duracion = datetime.now() - start_time
        print(duracion)
        return r

    def enviarViajes(self,status,viaje):
        start_time = datetime.now()
        print(status)
        print(viaje)
        print('enviando viajes con estatus ' + str(status) + ": " + str(datetime.now()))
        headers = {'content-type': 'application/json', 'X-API-KEY': 'mtS5hV3rl53tBeGeWnfWq2pqxSRDjOvJW6L7hUb9'}
        url = "https://b2uiut18x9.execute-api.us-east-1.amazonaws.com/dev/pre-despegar-viaje"
        datos = {"status": status, "jsonViaje":viaje}
        try:
            r = requests.post(url, data=json.dumps(datos), headers=headers).json()
            print("viajes enviados")
            print (r)
        
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

        duracion = datetime.now() - start_time
        print(duracion)
        return r


    def getViaje(self,idViaje):
        headers = {'content-type': 'application/json', 'X-API-KEY': 'mtS5hV3rl53tBeGeWnfWq2pqxSRDjOvJW6L7hUb9'}
        url = "https://o0480vy3fe.execute-api.us-east-1.amazonaws.com/dev/leer-viaje"
        datos = {"empresaId":config.usuario["idempresa"] , "IdViaje": idViaje, "cedi": config.usuario["cedi"]}
        try:
            r = requests.post(url, data=json.dumps(datos), headers=headers).json()
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
        return r

    def enviarViajes(self,status,viaje):
        start_time = datetime.now()
        print(status)
        
        print('enviando viajes con estatus ' + str(status) + ": " + str(datetime.now()))
        headers = {'content-type': 'application/json', 'X-API-KEY': 'mtS5hV3rl53tBeGeWnfWq2pqxSRDjOvJW6L7hUb9'}
        url = "https://b2uiut18x9.execute-api.us-east-1.amazonaws.com/dev/pre-despegar-viaje"
        datos = {"status": status, "jsonViaje":viaje}
        try:
            r = requests.post(url, data=json.dumps(datos), headers=headers).json()
            print("viajes enviados")
            print (r)
        
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

        duracion = datetime.now() - start_time
        print(duracion)
        return r