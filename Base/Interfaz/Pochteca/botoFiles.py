from boto3 import client
import boto3
import pandas as pd
import config
import json

class botoFiles():
    """docstring for botoFiles"""
    def __init__(self):
        pass


    def openS3(self,nombre):
        data = None
        try:
            bucket,key,access = config.enviromentS3Read
            s3 = boto3.client('s3', aws_access_key_id = key, aws_secret_access_key = access)
            obj = s3.get_object(Bucket=bucket, Key=nombre)
            object_content = obj['Body'].read().decode('utf-8')
            data = pd.read_csv(StringIO(object_content), sep="\t")
            return data

        except Exception as e:
            print(e)

    def leerTSVdesdeFTP(self,cedi):
        print("Leyendo archivos desde el FTP")
        config.mainWindow.progress_fn(20,"Leyendo archivos desde el FTP")
        s3 = boto3.resource('s3', aws_access_key_id = 'AKIAJEFVIQQQ7VJB7NAQ', aws_secret_access_key = '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')
        conn = client('s3', aws_access_key_id = 'AKIAJEFVIQQQ7VJB7NAQ', aws_secret_access_key = '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')
        json_datos = {}
        pedidos = {}
        operadores = []
        destinos = []
        pedidos['normales'] = []
        pedidos['urgentes'] = []
        pedidos['historial'] = []
        pedidos['otros'] = []

        config.mainWindow.progress_fn(40,"Listando archivos")
        for key in conn.list_objects(Bucket='arete-arms3-ftp-pochteca')['Contents']:
            archivo = {}
            s3obj = s3.Object('arete-arms3-ftp-pochteca', key['Key'])
            nombre = s3obj.key
            print(nombre)


            if len(nombre) > 1:
                if cedi in s3obj.key:
                    #print(s3obj)
                    if len(nombre) > 0:
                        tipo = nombre.rsplit('.', 4)[0]
                        if not('Historial/' in s3obj.key):
                            if 'Normales' in s3obj.key:
                                if s3obj.key != 'Normales/':
                                    nom = nombre.lstrip("Normales/")
                                    archivo['nombre'] = nombre
                                    archivo['key'] = s3obj.key
                                    if tipo == 'Normales/pedidos':
                                        Normales = []
                                        Urgentes = []
                                        Historial = []
                                        Normales.append(archivo)
                                        pedidos['normales'].extend(Normales)
                                    if tipo == 'operadores':
                                        operadores.append(archivo)
                                    if tipo == 'destinos':
                                        destinos.append(archivo)



                            if 'Urgentes' in s3obj.key:
                                if s3obj.key != 'Urgentes/':
                                    archivo['nombre'] = nombre
                                    archivo['key'] = s3obj.key
                                    if tipo == 'Urgentes/pedidos':
                                        Normales = []
                                        Urgentes = []
                                        Historial = []
                                        Urgentes.append(archivo)
                                        pedidos['urgentes'].extend(Urgentes)
                                    if tipo == 'operadores':
                                        operadores.append(archivo)
                                    if tipo == 'destinos':
                                        destinos.append(archivo)

                            elif not('Normales' in s3obj.key) and not('Urgentes' in s3obj.key):
                                if s3obj.key != '/':
                                    archivo['nombre'] = nombre
                                    archivo['key'] = s3obj.key
                                    if tipo == 'pedidos':
                                        Otros = []
                                        Otros.append(archivo)
                                        pedidos['otros'].extend(Otros)
                                    if tipo == 'operadores':
                                        operadores.append(archivo)
                                    if tipo == 'destinos':
                                        destinos.append(archivo)

                    else :
                        Normales = []
                        Urgentes = []
                        Historial = []
                        archivo['nombre'] = nombre
                        archivo['key'] = s3obj.key
                        if tipo == 'pedidos':
                            Normales = []
                            Urgentes = []
                            Historial = []
                            Historial.append(archivo)
                            pedidos['historial'].extend(Historial)
                        if tipo == 'operadores':
                            operadores.append(archivo)
                        if tipo == 'destinos':
                            destinos.append(archivo)
            else:
                Normales = []
                Urgentes = []
                Historial = []
                Otros = []
                if s3obj.key != '/':
                    #if args.cedi in s3obj.key:
                    #print(s3obj.key)
                    tipo = nombre.rsplit('.', 4)[0]
                    archivo['nombre'] = nombre
                    archivo['key'] = s3obj.key
                    if tipo == 'pedidos':
                        Otros = []
                        Otros.append(archivo)
                        pedidos['otros'].extend(Otros)
                    if tipo == 'operadores':
                        operadores.append(archivo)
                    if tipo == 'destinos':
                        destinos.append(archivo)


        json_datos['pedidos'] = pedidos
        json_datos['operadores'] = operadores
        json_datos['destinos'] = destinos
        json_data = json.dumps(json_datos)
        print("Esto es lo del JSON")
        print(json_data)
        self.pedidos = json.dumps(pedidos)
        self.operadores = json.dumps(operadores)
        self.json_datos = json.dumps(json_datos)
        config.mainWindow.progress_fn(100,"Se muestran archivos del FTP")
        return json_data



    def enviaHistorial(self, keyOrigen):
        

        #copia el key a otra direccion
        try:
            if "/" in keyOrigen:
                keyDestino = "Historial/" + keyOrigen.rsplit('/', 2)[1]
            else:
                keyDestino = "Historial/" + keyOrigen

            #print(keyOrigen)
            #print(keyDestino)
            s3 = boto3.resource('s3', aws_access_key_id = config.aws_access_key_id, aws_secret_access_key = config.aws_secret_access_key)
            s3.Object(config.Bucket, keyDestino).copy_from(CopySource= config.Bucket + '/' + keyOrigen)
            s3.Object(config.Bucket, keyOrigen).delete()
            config.mainWindow.progress_fn(100,"El archivo ha terminado de procesarse y se ha movido al historial")

            #llamamo manejador para actualizar la tabla de destinos
            self.manejador()

            return ('ok')
        except Exception as e:
            if 'NoSuchKey' in str(e):

                return ('El archivo TSV no existe')
            elif 'NoSuchBucket' in str(e):
                return ('El bucket no existe')
            else:
                return (e)


    def saveS3(self,content,name):
        content = content.to_csv(None,sep="\t",header=True,index = False).encode()
        bucket,key,access = config.enviroment
        s3 = boto3.resource('s3',
            aws_access_key_id=key,
            aws_secret_access_key=access
            )       
        nombre = 'DestinosIncompletos'+'/'+name+'.tsv'
        try:
            o = s3.Object(bucket,nombre)
            o.put(Body=content)
            #print("GUARDADO EN S3")    
        except Exception as e:
            print("error al guardar: "+str(e))