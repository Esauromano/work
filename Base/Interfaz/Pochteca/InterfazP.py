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
from PyQt5 import QtCore, QtWidgets, QtWebEngineWidgets, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from IO.Apis.Db import DB
from IO.Apis.spread_sheet import SpreadSheet
from PyQt5.QtWidgets import QTableWidget,QTableWidgetItem, QMessageBox
from Base.Interfaz.Pochteca.ss import ssj
import numpy as np
import config
from time import gmtime, strftime, localtime
import Base.Interfaz.gmplot.gmplot as gmplot
from Base.Interfaz.Pochteca.destinosDB import *
from pygsheets.exceptions import *
from generales import *
'''
Clase
'''

PinCedi = 'https://s3.amazonaws.com/arete-arms3/resources/cece.png'


class InterfazPochteca:
    def __init__(self, ui, signals):
        self.signals = signals

        self.signals.progress.emit(10,"Inicializando componentes")
        self.ui = ui
        self.destinos = []
        self.SSdesde = {}
        self.SShacia = {}
        self.coordSelecc={}
        self.colDestinos = ['Destino', 'CalleNumero', 'Colonia', 'Municipio', 'Estado', 'CodigoPostal', 'Region', 'Subregion', 'Latitud', 'Longitud', 'RestriccionVehiculo', 'RestriccionVolumen', 'Dedicado', 'VentanaInicioDestino', 'VentanaFinDestino', 'DesfaseHorario', 'L', 'M', 'Mi', 'J', 'V', 'S', 'D', 'TiemServicio', 'Contacto1', 'Telefono1', 'Correo1', 'Contacto2', 'Telefono2', 'Correo2', 'Hotel', 'RecalcularDestino', 'FactorSubidaS', 'FactorSubidaM', 'FactorSubidaL', 'FactorIntermedioS', 'FactorIntermedioM', 'FactorIntermedioL', 'FactorRetornoS', 'FactorRetornoM', 'FactorRetornoL']
        self.pedidos = ''
        self.operadores = ''
        self.json_datos = ''       
        self.ssj = ssj(ui)        
        self.ui.tablePochtecaLatLong.clear()
        self.ui.tablePochtecaLatLong_2.clear()
        self.ui.listWidgetPochtecaHistorial.clear()
        self.ui.dateEditPochteca.hide()
        self.ui.filtrarFechas.clicked.connect(self.doCheck)
        #self.mapa()
        self.pdb = destinosDB()
        self.signals.progress.emit(100,"terminando de inicializar componentes")
        self.ui.listWidgetPochtecaFTP.setSelectionMode(QListWidget.MultiSelection)
        self.ui.tableWidget.setSelectionMode(QTableWidget.SingleSelection)
        self.ui.tableWidget.setSelectionBehavior(QTableWidget.SelectRows)
        self.ui.tableWidget.itemSelectionChanged.connect(self.mostrarPin)
        self.ui.mandarDestinosDB.clicked.connect(self.mandarUno)
        #self.ui.tabWidget1Principal.resized.connect(self.resizewindow_dash)
        


    '''def mapa(self):
        self.signals.progress.emit(20,"Desplegando mapa")
        longitudes = []
        latitudes = []
        self.ui.dashboardMotor.setGeometry(0, 0, self.ui.mapFrame.frameGeometry().width(), self.ui.mapFrame.frameGeometry().height())
        gmap = gmplot.GoogleMapPlotter(37.428, -122.145, 5, "AIzaSyD-GOe2kJOEyrTZR_wcx4k789RpVcO3qk0")
        gmap.plot(latitudes, latitudes, 'cornflowerblue', edge_width=10)
        mapvar = 'mapmotor.html'
        gmap.draw(mapvar)
        maphtml = open(mapvar, 'r')
        maphtmltext = maphtml.read()
        self.ui.dashboardMotor.setHtml(maphtmltext)'''

    def abrirLocal(self):
        nombre, tipos = QFileDialog.getOpenFileName(config.mainWindow, 'Open file', '~', "SpreadSheet files (*.tsv *xlsx)")
        print(nombre)
        if nombre.endswith('.tsv'):
            print("tsv")
            dataFrame = pd.read_csv(nombre, sep="\t", decimal=",")
            dataFrame = dataFrame.replace('No', 0)
            dataFrame = dataFrame.replace('Sí', 1)
            dataFrame = dataFrame.replace('NO', 0)
            dataFrame = dataFrame.replace('Si', 1)
            dataFrame = dataFrame.replace('SI', 1)
            if 'destinos' in nombre:
                if set(self.colDestinos) == set(dataFrame.columns.values):
                    self.procesoDestinos(dataFrame, nombre)


            elif 'pedidos' in nombre:
                print("hay pedidos")
                self.procesoPedidos(dataFrame, nombre)

            elif 'operadores' in nombre:
                print("Hay operadores")
                self.procesoOperadores(dataFrame, nombre)


        elif nombre.endswith('.xlsx'):
            print("xlsx")
            workbook = pd.ExcelFile(nombre)
            hojas = {}
            for sheet_name in workbook.sheet_names:
                df = workbook.parse(sheet_name)
                hojas[sheet_name] = df
            if 'destinos' in hojas:
                if set(self.colDestinos) == set(dataFrame.columns.values):
                    self.procesoDestinos(hojas['destinos'], nombre)

            elif 'pedidos' in hojas:
                print("hay pedidos")
                self.procesoPedidos(hojas['pedidos'], nombre)

            elif 'operadores' in hojas:
                print("Hay operadores")
                self.procesoOperadores(hojas['operadores'], nombre)


    def procesoDestinos(self, dataFrame, nombre):
        dataFrame = dataFrame.replace(np.nan, '', regex=True)
        #print(dataFrame)
        print(dataFrame.shape)

        for index, row in dataFrame.loc[dataFrame['Longitud']==''].iterrows():
            print(index)
            direccion = str(row['Municipio']) + ' ' + str(row['CodigoPostal']) + ' ' + str(row['CalleNumero'])
            latitud, longitud = self.coordenadas(direccion)
            print(latitud + longitud + ' Destino:' + str(row['Destino']))
            if latitud != "Se necesitan mas datos" and longitud != "Se necesitan mas datos":
                if self.enMX(latitud, longitud):

                    #latitud = latitud.replace(".", ",")
                    #longitud = longitud.replace(".", ",")
                    

                    dataFrame.set_value(index, 'Latitud', latitud, takeable=False)
                    dataFrame.set_value(index, 'Longitud', longitud, takeable=False)
                    '''numeroCliente = str(row['Destino']).replace(" - ", "-")
                       dataFrame.set_value(index, 'Destino', numeroCliente, takeable=False)'''

                    
                else:
                    latitud = 'Se necesitan mas datos'
                    longitud = 'Se necesitan mas datos'
                    print(str(row['Destino']) + ' ' + str(row['CalleNumero']))

                    dataFrame.set_value(index, 'Latitud', latitud, takeable=False)
                    dataFrame.set_value(index, 'Longitud', longitud, takeable=False)
                    '''numeroCliente = str(row['Destino']).replace(" - ", "-")
                       dataFrame.set_value(index, 'Destino', numeroCliente, takeable=False)  '''
            
        #crea archivo faltantes
        conCoordenadas = dataFrame.loc[dataFrame['Longitud'] != '']
        sinCoordenadas = dataFrame.loc[dataFrame['Longitud'] == '']
        nombre = config.MODE+".DestinosRechazados."+strftime("%Y-%m-%d_%H:%M:%S", localtime())
        print(conCoordenadas.shape)
        print(sinCoordenadas.shape)
        print(sinCoordenadas)

        #guardar sincoordenadas como rechazados en s3
        self.saveS3(sinCoordenadas, nombre)

        #Guardar archivo local
        #conCoordenadas.to_csv('conCoordenadas'+strftime("%Y-%m-%d_%H:%M:%S", localtime()), encoding='utf-8', sep="\t")
        #sincoordenadas.to_csv(nombre, encoding='utf-8', sep="\t")

        #guardar en BD
        df = conCoordenadas.to_json(orient='records')
        status, res = self.mandarDestinos(df)
        print(status)
        print(res)
        config.procesoExitoso=status


    def procesoPedidos(self, df1, nombre):
        print(df1.shape)
        print(df1)
        df = df1.replace(np.nan, '', regex=True)
        destinos = json.loads(df.to_json(orient='records'))
        lisDestinos = []
        lisDB = []

        for destino in destinos:
            lisDestinos.append(destino['DestinoTR1'])

        lisDestinos=list(set(lisDestinos))
        datosDB, status = self.consultarDestinos(list(set(lisDestinos)))
        print(datosDB)
        print("longitud de lisDestinos")
        print(len(lisDestinos))
        if datosDB != "no existen destinos":
            if datosDB is not None and status is True and datosDB != "OK":
                if len(list(set(lisDestinos))) == len(datosDB): 
                    print("crearSS()")
                    nombres = nombre.split("/")
                    nombres.reverse()
                    nombre = nombres[0]
                    sh = self.ssj.crearSS("pedidos", nombre)
                    print("salvarDFtoSS()")
                    resultadoGuardar = self.ssj.salvarDFtoSS(df,sh)

                    config.procesoExitoso=resultadoGuardar
                       

                    return resultadoGuardar, '', nombre
                else:
                    print("Faltan destinos")
                    for dato in datosDB:
                        #print(dato)
                        lisDB.append( dato['Destino'])

                    faltantes = list(filter(lambda x: x not in lisDB, list(set(lisDestinos)))) 
                    print(faltantes)
                    print(len(faltantes))
                    config.destinosNoDB = faltantes
                    myString = ", ".join(faltantes)
                    print(myString)


                    return False, myString, nombre
            else:
                faltantes = list(filter(lambda x: x not in lisDB, list(set(lisDestinos)))) 
                print(faltantes)
                print(len(faltantes))

                myString = ", ".join(faltantes) 

                #self.ui.progress_fn(100,"Faltan todos los destinos de este archivo en la DB, no se creara el spreadsheet hasta que se inserten")
                #self.fnMuestraMensaje(myString)
                return False, myString, nombre
        else:
            print(datosDB)
            config.destinosNoDB = ['No existe ningun destino']
            return False, 'no existen destinos', nombre

    def procesoOperadores(self, df1, nombre):

        print(df1.shape)
        print(nombre)
        nombres = nombre.split("/")
        print(nombres)

        nombres.reverse()

        print(nombres)

        nombre = nombres[0]
        df = df1.replace(np.nan, '', regex=True)
        print("crearSS()")
        sh = self.ssj.crearSS('operadores', nombre)

        print("salvarDFtoSS()")
        esto = self.ssj.salvarDFtoSS(df,sh)

        config.procesoExitoso = esto
            


    def dameJson(self, value):
        try:
            json = {}
            json["Destino"] = self.ui.tableWidget.item(value, 0).text()
            json["Latitud"] = self.ui.tableWidget.item(value, 1).text()
            json["Longitud"] = self.ui.tableWidget.item(value, 2).text()
            json["RestriccionVehiculo"] = self.ui.tableWidget.item(value, 3).text()
            json["RestriccionVolumen"] = self.ui.tableWidget.item(value, 4).text()
            json["Dedicado"] = self.ui.tableWidget.item(value, 5).text()
            json["Region"] = self.ui.tableWidget.item(value, 6).text()
            json["Subregion"] = self.ui.tableWidget.item(value, 7).text()
            json["Estado"] = self.ui.tableWidget.item(value, 8).text()
            json["Municipio"] = self.ui.tableWidget.item(value, 9).text()
            json["Colonia"] = self.ui.tableWidget.item(value, 10).text()
            json["CalleNumero"] = self.ui.tableWidget.item(value, 11).text()
            json["CodigoPostal"] = self.ui.tableWidget.item(value, 12).text()
            json["VentanaInicioDestino"] = self.ui.tableWidget.item(value, 13).text()
            json["VentanaFinDestino"] = self.ui.tableWidget.item(value, 14).text()
            json["DesfaseHorario"] = self.ui.tableWidget.item(value, 15).text()
            json["L"] = self.ui.tableWidget.item(value, 16).text()
            json["M"] = self.ui.tableWidget.item(value, 17).text()
            json["Mi"] = self.ui.tableWidget.item(value, 18).text()
            json["J"] = self.ui.tableWidget.item(value, 19).text()
            json["V"] = self.ui.tableWidget.item(value, 20).text()
            json["S"] = self.ui.tableWidget.item(value, 21).text()
            json["D"] = self.ui.tableWidget.item(value, 22).text() 
            json["TiemServicio"] = self.ui.tableWidget.item(value, 23).text()
            json["Contacto1"] = self.ui.tableWidget.item(value, 24).text()
            json["Telefono1"] = self.ui.tableWidget.item(value, 25).text()
            json["Correo1"] = self.ui.tableWidget.item(value, 26).text()
            json["Contacto2"] = self.ui.tableWidget.item(value, 27).text()
            json["Telefono2"] = self.ui.tableWidget.item(value, 28).text()
            json["Correo2"] = self.ui.tableWidget.item(value, 29).text()
            json["Hotel"] = self.ui.tableWidget.item(value, 30).text()
            json["FactorSubidaS"] = self.ui.tableWidget.item(value, 31).text()
            json["FactorSubidaM"] = self.ui.tableWidget.item(value, 32).text()
            json["FactorSubidaL"] = self.ui.tableWidget.item(value, 33).text()
            json["FactorIntermedioS"] = self.ui.tableWidget.item(value, 34).text()
            json["FactorIntermedioM"] = self.ui.tableWidget.item(value, 35).text()
            json["FactorIntermedioL"] = self.ui.tableWidget.item(value, 36).text()
            json["FactorRetornoS"] = self.ui.tableWidget.item(value, 37).text()
            json["FactorRetornoM"] = self.ui.tableWidget.item(value, 38).text()
            json["FactorRetornoL"] = self.ui.tableWidget.item(value, 39).text()
            return json
        except Exception as e:
            print(e)



    def checkChangeCoords(self, jsonRow):
        try:
            if jsonRow["Latitud"] != self.coordSelecc["Latitud"]:
                self.recalcular=1
            elif jsonRow["Longitud"] != self.coordSelecc["Longitud"]:
                self.recalcular=1
            else:
                self.recalcular=0
        except Exception as e:
            print(e)




    def selec2json(self):
        json = {}
        rows = [idx.row() for idx in self.ui.tableWidget.selectionModel().selectedRows()]
        value= rows[0]
        print(rows)
        print(value)
        json["destino"] = self.ui.tableWidget.item(value, 0).text()
        json["lat"] = self.ui.tableWidget.item(value, 1).text()
        json["lon"] = self.ui.tableWidget.item(value, 2).text()
        json["RestriccionVehiculo"] = self.ui.tableWidget.item(value, 3).text()
        json["RestriccionVolumen"] = self.ui.tableWidget.item(value, 4).text()
        json["Dedicado"] = self.ui.tableWidget.item(value, 5).text()
        json["Region"] = self.ui.tableWidget.item(value, 6).text()
        json["Subregion "] = self.ui.tableWidget.item(value, 7).text()
        json["Estado"] = self.ui.tableWidget.item(value, 8).text()
        json["Municipio"] = self.ui.tableWidget.item(value, 9).text()
        json["Colonia"] = self.ui.tableWidget.item(value, 10).text()
        json["CalleNumero"] = self.ui.tableWidget.item(value, 11).text()
        json["CodigoPostal"] = self.ui.tableWidget.item(value, 12).text()
        json["VentanaInicioDestino"] = self.ui.tableWidget.item(value, 13).text()
        json["VentanaFinDestino"] = self.ui.tableWidget.item(value, 14).text()
        json["DesfaseHorario"] = self.ui.tableWidget.item(value, 15).text()
        json["L"] = self.ui.tableWidget.item(value, 16).text()
        json["M"] = self.ui.tableWidget.item(value, 17).text()
        json["Mi"] = self.ui.tableWidget.item(value, 18).text()
        json["J"] = self.ui.tableWidget.item(value, 19).text()
        json["V"] = self.ui.tableWidget.item(value, 20).text()
        json["S"] = self.ui.tableWidget.item(value, 21).text()
        json["D"] = self.ui.tableWidget.item(value, 22).text() 
        json["TiemServicio"] = self.ui.tableWidget.item(value, 23).text()
        json["Contacto1"] = self.ui.tableWidget.item(value, 24).text()
        json["Telefono1"] = self.ui.tableWidget.item(value, 25).text()
        json["Correo1"] = self.ui.tableWidget.item(value, 26).text()
        json["Contacto2"] = self.ui.tableWidget.item(value, 27).text()
        json["Telefono2"] = self.ui.tableWidget.item(value, 28).text()
        json["Correo2"] = self.ui.tableWidget.item(value, 29).text()
        json["Hotel"] = self.ui.tableWidget.item(value, 30).text()
        json["FactorSubidaS"] = self.ui.tableWidget.item(value, 31).text()
        json["FactorSubidaM"] = self.ui.tableWidget.item(value, 32).text()
        json["FactorSubidaL"] = self.ui.tableWidget.item(value, 33).text()
        json["FactorIntermedioS"] = self.ui.tableWidget.item(value, 34).text()
        json["FactorIntermedioM"] = self.ui.tableWidget.item(value, 35).text()
        json["FactorIntermedioL"] = self.ui.tableWidget.item(value, 36).text()
        json["FactorRetornoS"] = self.ui.tableWidget.item(value, 37).text()
        json["FactorRetornoM"] = self.ui.tableWidget.item(value, 38).text()
        json["FactorRetornoL"] = self.ui.tableWidget.item(value, 39).text()
        json["RecalcularDestino"] = self.ui.tableWidget.item(value, 40).text()
        print(json)

    
    def updateCoordRow(self, coordenadas):
        try:
            if len([idx.row() for idx in self.ui.tableWidget.selectionModel().selectedRows()]) == 1:
                coordenadas = coordenadas.replace("(", "")
                coordenadas = coordenadas.replace(")", "")
                coordenadas = coordenadas.split(", ")
                print("coordenadas")
                print(coordenadas)
                lat = coordenadas[0]
                lon = coordenadas[1]
                rows = [idx.row() for idx in self.ui.tableWidget.selectionModel().selectedRows()]
                row= rows[0]
                self.ui.tableWidget.setItem(row, 1, QTableWidgetItem(lat))
                self.ui.tableWidget.setItem(row, 2, QTableWidgetItem(lon))
                ºself.recalcular=1
        except Exception as e:
            print(e)

    def mostrarPin(self):
        try:
            rows = [idx.row() for idx in self.ui.tableWidget.selectionModel().selectedRows()]
            value= rows[0]
            print(rows)
            print(value)
            lat = self.ui.tableWidget.item(value, 1)
            lon = self.ui.tableWidget.item(value, 2)
            self.coordSelecc["Latitud"]=lat.text()
            self.coordSelecc["Longitud"]=lon.text()
            print(self.coordSelecc)
            self.ui.dashboardMotor.setGeometry(0, 0, self.ui.mapFrame.frameGeometry().width(), self.ui.mapFrame.frameGeometry().height())
            antes = '<!DOCTYPE html> <html> <head> <meta name="viewport" content="initial-scale=1.0, user-scalable=no" /> <style type="text/css"> html { height: 100% } body { height: 100%; margin: 0; padding: 0 } #map-canvas { height: 100% } </style> <script type="text/javascript" src="https://maps.googleapis.com/maps/api/js?v=3.exp&sensor=false"> </script> <script type="text/javascript"> function palPy(arg){new QWebChannel(qt.webChannelTransport, function(channel) { channel.objects.bridge.print(arg); });}  function initialize() { var myLatlng = new google.maps.LatLng('
            despues = '); var mapOptions = { center: myLatlng, zoom: 16 }; var map = new google.maps.Map(document.getElementById("map-canvas"), mapOptions); var marker = new google.maps.Marker({ position: myLatlng, map: map, title: "Hello World!" }); google.maps.event.addListener(map, "center_changed", function() { window.setTimeout(function() { var center = map.getCenter(); marker.setPosition(center); console.log(center.toString()); palPy(center.toString()); window.status = center.lat(); }, 100); }); } google.maps.event.addDomListener(window, "load", initialize); </script> </head> <body><div id="map-canvas"/></body></html>'
            html = antes + lat.text() + ',' + lon.text() + despues
            config.mainWindow.dashboardMotor.setHtml(html)
            self.ui.progress_fn(100,"Mostrando pin en mapa")
        except Exception as e:
            print(e)



    def mandarUno(self):
        try:
            rows = [idx.row() for idx in self.ui.tableWidget.selectionModel().selectedRows()]
            row= rows[0]
            jsonRow = self.dameJson(row)
            self.checkChangeCoords(jsonRow)
            message, status, data = self.pdb.updateRow(jsonRow, self.recalcular)
            print(data)
            if status:
                self.popup("El destino se ha actualizado correctamente")
                
            
        except Exception as e:
            print(e)


    def popup(self, message):
        msgBox = QMessageBox()
        msgBox.setText(message)
        msgBox.exec_()

    def json2df(self):
        self.ui.progress_fn(20,"Leyendo destinos")
        dato = self.pdb.traerDestinos()
        #print(dato)
        self.ui.progress_fn(60,"Desplegando datos")
        df = pd.DataFrame.from_dict(dato["data"], orient='columns', dtype=None)
        #print(df)
        
        chidas = ['Destino', 'Latitud', 'Longitud', 'RestriccionVehiculo', 'RestriccionVolumen', 'Dedicado', 'Region', 'Subregion', 'Estado', 'Municipio', 'Colonia', 'CalleNumero', 'CodigoPostal', 'VentanaInicioDestino', 'VentanaFinDestino', 'DesfaseHorario', 'L', 'M', 'Mi', 'J', 'V', 'S', 'D', 'TiemServicio', 'Contacto1', 'Telefono1', 'Correo1', 'Contacto2', 'Telefono2', 'Correo2', 'Hotel', 'FactorSubidaS', 'FactorSubidaM', 'FactorSubidaL', 'FactorIntermedioS', 'FactorIntermedioM', 'FactorIntermedioL', 'FactorRetornoS', 'FactorRetornoM', 'FactorRetornoL', 'RecalcularDestino']

        df = df.reindex(columns=chidas)
        #print(df)
        self.desplegarDatos(df, self.ui.tableWidget, chidas)
        self.ui.progress_fn(100,"Se muestran todos los destinos")


    def desplegarDatos(self, df, grid, ordenCampos):
        self.ui.progress_fn(60,"Desplegando datos")

        try:
            grid.setRowCount(0)
            df.reset_index(drop=True, inplace=True)
            # ordena el df
            camposOriginal = []
            camposTitulos = []
            for i in range(len(ordenCampos)):
                camposOriginal.append(ordenCampos[i])
                camposTitulos.append(ordenCampos[i])

            df = df[camposOriginal]

            # dimension de la tabla y borra antes
            grid.setRowCount(df.shape[0])
            grid.setColumnCount(df.shape[1])
            # headers de las cols
            grid.setHorizontalHeaderLabels(camposTitulos)
            grid.setSortingEnabled(False)
            # mete celda x celda
            for row in range(df.shape[0]):
                for col in range(df.shape[1]):
                    
                    s = str(df.iloc[row, col])

                    item = QTableWidgetItem(s)

                    item.setTextAlignment(Qt.AlignLeft)
                    item.setForeground(QColor(255,255,255))
                    #item.setFlags(item.flags() ^ Qt.ItemIsEditable)
                    grid.setItem(row, col, item)
            grid.resizeColumnsToContents()
            grid.setSortingEnabled(True)
            grid.repaint()
        # ----------------------------------------------------
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            error = '{} - {} - linea {}  ({})'.format(exc_type, fname, exc_tb.tb_lineno, str(e))
            print(error)
            return False, 0, 0





    def doCheck(self):
        if self.ui.filtrarFechas.isChecked():
            self.ui.dateEditPochteca.show()
        else:
            self.ui.dateEditPochteca.hide()



    def filtroFecha(self):
        fec = self.ui.dateEditPochteca.date().toPyDate()
        fech = str(fec)
        print("fech")
        print(fech)
        fecha = fech.split("-")
        fechita = fecha[0] + '-' + fecha[1] + '-' + fecha[2]
        print("fechita")
        print(fechita)
        datos2 = json.loads(self.pedidos)
        datos = json.loads(self.json_datos)
        datos2 = json.loads(self.json_datos)
        print("Estos son los DATOS ")
        print(datos)

        for value in datos['pedidos']:
            print(value)
            print(datos['pedidos'][value])

            for dato in datos2['pedidos'][value]:
                if fechita != dato['nombre'].rsplit('.', 4)[1]:
                    print(dato['nombre'].rsplit('.', 4)[1])
                    print(fechita)
                    datos['pedidos'][value].remove(dato);
                    print("Removiendo!!!!!!!!!!!!!!")
                    print(dato)
                else:
                    print(dato['nombre'].rsplit('.', 4)[1])
                    print(fechita)
                    print("NO Removiendo!!!!!!!!!!!!!!")
                    print(dato)

        for dato in datos['operadores']:
            #print(value)
            if fechita not in dato['nombre']:
                datos['operadores'].remove(dato);

        self.ui.listWidgetPochtecaFTP.clear()
        if self.ui.radioButtonInterfasePochtecaPedidos.isChecked() == True:

            if self.ui.radioButtonInterfasePochtecaTodos.isChecked() == True:
                for cosa in datos['pedidos']["normales"]:
                    self.ui.listWidgetPochtecaFTP.addItem(cosa["nombre"])
                for cosa in datos['pedidos']["urgentes"]:
                    self.ui.listWidgetPochtecaFTP.addItem(cosa["nombre"])
                for cosa in datos['pedidos']["otros"]:
                    self.ui.listWidgetPochtecaFTP.addItem(cosa["nombre"])

            #print("pedidos/")
            if self.ui.radioButtonInterfasePochtecaOrdinarios.isChecked() == True:
                for cosa in datos['pedidos']["normales"]:
                    self.ui.listWidgetPochtecaFTP.addItem(cosa["nombre"])

            if self.ui.radioButtonInterfasePochtecaUrgentes.isChecked() == True:
                #print("*************")
                #print("urgentes")
                for cosa in datos['pedidos']["urgentes"]:
                    self.ui.listWidgetPochtecaFTP.addItem(cosa["nombre"])

            
                

        elif self.ui.radioButtonInterfasePochtecaOperadores.isChecked() == True:
            for cosa in datos['operadores']:
                self.ui.listWidgetPochtecaFTP.addItem(cosa["nombre"])





    def coordenadas(self, direccion):
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



    def limpiarlatlong(self, dato):
        try:
            dato1 = dato.replace(".","")
            dato2 = dato1.replace(",","")
            dato3 = dato2.replace("-","")
            return dato3
        except Exception as e:
            raise e



    def concatTSV(self):
        sp = SpreadSheet()
        try:
            concatenado = self.openS3(self.ui.listWidgetPochtecaFTP.selectedIndexes()[0].data())
            tipo = None
            testigo = self.ui.listWidgetPochtecaFTP.selectedIndexes()[0].data()
            if "/" not in testigo:
                tipo = testigo.split('.', 2)[0]
            else:
                tipo = testigo.split('.', 2)[0].split('/', 2)[1]
            print(concatenado.shape)
            for index, x in enumerate(self.ui.listWidgetPochtecaFTP.selectedIndexes()):
                if index < len(self.ui.listWidgetPochtecaFTP.selectedIndexes())-1:

                    print(self.ui.listWidgetPochtecaFTP.selectedIndexes()[(index+1)].data())
                    resultado = self.openS3(self.ui.listWidgetPochtecaFTP.selectedIndexes()[(index+1)].data())
                    concatenado = pd.concat([concatenado, resultado])
                    print(concatenado.shape)
            
            conca = concatenado.drop_duplicates(keep='last', inplace=False)

            df = conca.replace(np.nan, '', regex=True)

            return df, tipo
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

    def concatPedidos(self):
        try:
            self.ui.tablePochtecaLatLong.clear()
            self.ui.tablePochtecaLatLong_2.clear()
            sp = SpreadSheet()
            status, duracion, resultado = sp.abrirSS(self.SSdesde["id"],'DESTINOS','key')
            status2, duracion2, resultado2 = sp.abrirSS(self.SShacia["id"],'DESTINOS','key')
            ##print(resultado2)

            if self.SSdesde["id"] == self.SShacia["id"]:
                #print("son iguales")
                concatenados = resultado

            else:
                #print("No son iguales")
                concatenados = pd.concat([resultado2, resultado])

                #df2 = concatenados.loc[concatenados['Longitud']=='']

            for index, row in concatenados.loc[concatenados['Longitud']==''].iterrows():
                #print (row['CalleNumero'])
                latitud, longitud = self.coordenadas(row['CalleNumero'])
                latitud = latitud.replace(".", ",")
                longitud = longitud.replace(".", ",")
                concatenados.set_value(index, 'Latitud', latitud, takeable=False)
                concatenados.set_value(index, 'Longitud', longitud, takeable=False)
                checador = self.limpiarlatlong(latitud)
                if checador.isnumeric():
                    self.ui.tablePochtecaLatLong.addItem(row['CalleNumero'])
                else:
                    self.ui.tablePochtecaLatLong_2.addItem(row['CalleNumero'])
                    #row['Latitud']=latitud
                    #row['Longitud']=longitud


            conca = concatenados.drop_duplicates(keep='first', inplace=False)
            #print(conca)

            sp.salvarDFtoSS(conca,self.SShacia["id"])
        except Exception as e:
            raise e


    def selection_changed(self):
        try:
            rows = [idx.row() for idx in self.ui.tableWidgetPochtecaAnadeDe.selectionModel().selectedRows()]
            #print(rows)
            for value in rows:
                if value < len(self.destinos):
                    value = value
                    self.SSdesde = self.destinos[value]
                    #print("Lo que hay en desde " + self.SSdesde["id"])

            rows2 = [idx.row() for idx in self.ui.tableWidgetPochtecaAnadeA.selectionModel().selectedRows()]
            #print(rows)
            for value in rows2:
                if value < len(self.destinos):
                    value = value
                    self.SShacia = self.destinos[value]
                    #print("Lo que hay en hacia " + self.SShacia["id"])
        except Exception as e:
            raise e

    def listarDestinos(self):
        try:
            sp = SpreadSheet()
            lss = sp.listarSS()
            tamaño = len(lss) + 1
            self.destinos = lss
            self.ui.tableWidgetPochtecaAnadeDe.setRowCount(tamaño)
            self.ui.tableWidgetPochtecaAnadeDe.setColumnCount(2)
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


         




    def getResultDestinos2(self, tipo, obj):
        if obj.shape[0]>0:
            df2 = obj.replace(np.nan, '', regex=True)
            TSVconCoordenadas = df2.loc[(df2['Longitud'].notnull()) & (df2['Latitud'].notnull()) & (df2['Destino'].notnull()) & (df2['CalleNumero'].notnull()) & (df2['Colonia'].notnull()) & (df2['Estado'].notnull()) & (df2['CodigoPostal'].notnull()) & (df2['Destino'].notnull())]
            print(TSVconCoordenadas)
            coor = TSVconCoordenadas.to_json(orient='records')
            print(coor)
            result = self.mandarDestinos(coor)
            print(result)
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
            
            data = self.openS3(x.data())
            df2 = data.replace(np.nan, '', regex=True)
            
 
            for index, row in df2.loc[df2['Longitud']==''].iterrows():
                direccion = str(row['CalleNumero'])
                print(index + ' ' +direccion)
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
                self.saveS3(sinCoordenadas,nombre)
            

    def getResultDestinos(self,tipo,obj, signals):
        print(tipo)
        print(obj)
        print(signals)
        df2 = pd.DataFrame()
        try:
            signals.progress.emit(20,"Procesando el archivo de destinos")
            Recalcular = []
            NoRecalcular = []
            #print("procesar datos del dataframe")
            if obj.shape[0]>0:
                df2 = obj.replace(np.nan, '', regex=True)


                '''TSVconCoordenadas = df2.loc[(df2['Longitud'].notnull()) & (df2['Latitud'].notnull()) & (df2['Destino'].notnull()) & (df2['CalleNumero'].notnull()) & (df2['Colonia'].notnull()) & (df2['Estado'].notnull()) & (df2['CodigoPostal'].notnull()) & (df2['Destino'].notnull())]
                print(TSVconCoordenadas)
                coor = TSVconCoordenadas.to_json(orient='records')
                #print(coor)
                result = self.mandarDestinos(coor)
                print(result)
                if result is not None:
                    #TODO validar campo status
                    self.ui.progress_fn(100,"Destinos actualizados")
                    return True
                else:
                    self.ui.progress_fn(100,"Fallo al actualizar destinos")
                    return False'''
                    
                destinos = json.loads(df2.to_json(orient='records'))
                listaDestinos = []
                for destino in destinos:
                    default=''
                    if destino.get('Destino', default) != '':
                        listaDestinos.append(destino['Destino'])
                #print(listaDestinos)

                datosDB,status = self.consultarDestinos(listaDestinos)
                '''print("datosDB")
                                                                print(datosDB)
                                                                print("status")
                                                                print(status)'''
                if datosDB is not None and status is True and datosDB != "OK":
                    #print('hay algunos candidatos')
                    signals.progress.emit(50,"Comparando contra la base de datos")
                    #print("comparar")
                    #buscar en el DF que destinos no tiene latitud para ser calculada
                    for index, row in df2.loc[df2['Longitud']==''].iterrows():
                        #print("datosDB")
                        #print(datosDB)
                        for dato in datosDB:
                            #print("dato")
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
                                    jsonCoordenadas = self.procesaCoordenadas(index, row, df2, signals)
                            else:
                                signals.progress.emit(100,"Todos los destinos de este archivo han sido procesados")

                else:
                    #todos son candidatos 
                    #print('todos son candidatos')
                    for index, row in df2.loc[df2['Longitud']==''].iterrows():
                        direccion = str(row['CalleNumero'])
                        latitud, longitud = self.coordenadas(direccion, signals)

                        if 'Se necesitan mas datos' not in latitud:
                            jsonCoordenadas = self.procesaCoordenadas(index, row, df2, signals)
                        else:
                            df2.set_value(index, 'Latitud', latitud, takeable=False)
                            df2.set_value(index, 'Longitud', longitud, takeable=False)
                            #self.ui.tablePochtecaLatLong_2.addItem(row['CalleNumero'])
                    
                    #crea archivo faltantes
                    df = df2.to_json(orient='records')
                    conCoordenadas = df2.loc[df2['Longitud'] != 'Se necesitan mas datos']
                    sinCoordenadas = df2.loc[df2['Longitud'] == 'Se necesitan mas datos']
                    nombre = config.MODE+".DestinosRechazados."+strftime("%Y-%m-%d_%H:%M:%S", localtime())

                    #guardar sincoordenadas como rechazados en s3
                    self.saveS3(sinCoordenadas,nombre)

                    #guardar en BD
                    df = conCoordenadas.to_json(orient='records')
                    if self.mandarDestinos(df, signals) is not None:
                        #TODO validar campo status
                        signals.progress.emit(100,"Destinos actualizados")

                        return True, df2
                    else:
                        signals.progress.emit(100,"Fallo al actualizar destinos")
                        return False, df2

                #si no hay conexion con al base de datos no deberia de borrar el archivo
                if status:
                    return True, df2
                else:
                    return False, obj
                
                #print(NoRecalcular)
                #print(Recalcular)        

            else:
                signals.progress.emit(100,"el archivo tsv no cuenta con destinos")
                return True, df2

        except Exception as e:
            print(e)

        



    def openS3(self,nombre):
        data = None
        try:
            bucket,key,access = config.enviromentS3Read
            s3 = boto3.client('s3', aws_access_key_id = key, aws_secret_access_key = access)
            obj = s3.get_object(Bucket=bucket, Key=nombre)
            #print(obj)
            object_content = obj['Body'].read().decode('utf-8')
            data = pd.read_csv(StringIO(object_content), sep="\t")
            return data

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


        
    def process(self,nombre, signals):
        try:
            pass
        
            signals.progress.emit(10,"Abriendo archivo")
            tipo = None
            if "/" not in nombre:
                tipo = nombre.split('.', 2)[0]
            else:
                tipo = nombre.split('.', 2)[0].split('/', 2)[1]
            print("tipo")
            print(tipo)
            print("tipo")
            data = None
            res = None
            #valida que el tipo sea correcto 
            if tipo is not None:
                #valida obtener el archivo tsv de s3
                data = self.openS3(nombre)

                if data is None:
                    signals.progress.emit(100,"Archivo inexistente")
                else:
                    signals.progress.emit(20,"Archivo abierto correctamente")
                    print("trayendo destinos")
                    print("data")
                    print(data)
                    print("data")
                    status, res = self.getResultDestinos(tipo, data, signals)
                    print("status")
                    print(status)
                    print("res")
                    print(res)
            else:
                signals.progress.emit(100,"El tsv no comienza con un nombre correcto")

            if res is not None: 
                #print("MOVER ARCHIVO DE DESTINOS")
                #mover el archivo
                #nombre
                signals.progress.emit(100,"Moviendo archivo a historial")
                self.enviaHistorial(nombre, signals)
                return res
            else:
                return None
        except Exception as e:
            print(e)

        


    def destinosFTP(self):
        try:
            dato = self.leerTSVdesdeFTP('SAN JUAN')
            resultado = json.loads(dato)
            res = pd.DataFrame()
            for cosa in resultado["pedidos"]["normales"]:
                print(cosa)
                print(cosa["nombre"])
                nombre = cosa["nombre"]

                if "/" not in nombre:
                    tipo = nombre.split('.', 2)[0]
                else:
                    tipo = nombre.split('.', 2)[0].split('/', 2)[1]
                
                
                df = self.openS3(nombre)

                print(list(df['DestinoTR1']))

                
                res = pd.concat([res, df])
                print(res.shape)

            print(list(set(list(res['DestinoTR1']))))

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


    '''
    open
    Esta función toma un nombre de archivo y abre el TSV desde
    '''
    def open(self, nombre, signals):
        df1 = None
        print("Entrando a OPEN()")
        try:
            if "/" not in nombre:
                tipo = nombre.split('.', 2)[0]
            else:
                tipo = nombre.split('.', 2)[0].split('/', 2)[1]

            signals.progress.emit(40,"Abriendo archivo")
            df1 = self.openS3(nombre)

            if nombre.endswith('.tsv'):
                nombre = nombre[:-4]
                if 'pedidos' in nombre:
                    signals.progress.emit(50,"Procesando pedidos")
                    filename = 'PEDIDOS ' + nombre.split('pedidos.', 1 )[1]
                

                    df = df1.replace(np.nan, '', regex=True)
                    destinos = json.loads(df.to_json(orient='records'))
                    lisDestinos = []
                    lisDB = []

                    for destino in destinos:
                        lisDestinos.append(destino['DestinoTR1'])

                    datosDB, status = self.consultarDestinos(list(set(lisDestinos)))
                    print("lisDestinos")
                    print(list(set(lisDestinos)))
                    print(len(list(set(lisDestinos))))

                    print("status")
                    print(status)

                    print("datosDB")
                    print(datosDB)
                    print(len(datosDB))

                    if datosDB != "no existen destinos":
                        if datosDB is not None and status is True and datosDB != "OK":
                            if len(list(set(lisDestinos))) == len(datosDB): 
                                print("No, faltan destinos de estos pedidos, procesando")
                                signals.progress.emit(70,"Destinos completos, procesando...")
                                print("crearSS()")
                                sh = self.ssj.crearSS(tipo, filename)
                                print("salvarDFtoSS()")
                                resultadoGuardar = self.ssj.salvarDFtoSS(df,sh)

                                if resultadoGuardar == True:

                                    print("enviaHistorial")
                                    self.enviaHistorial(nombre + '.tsv', signals)
                                    signals.progress.emit(90,"Archivo procesado correctamente")
                                return resultadoGuardar, '', nombre
                            else:
                                print("Faltan destinos de estos pedidos")
                                signals.progress.emit(90,"Faltan destinos de estos pedidos")
                                for dato in datosDB:
                                    lisDB.append( dato['Destino'])
                                print(datosDB)
                                faltantes = list(filter(lambda x: x not in lisDB, list(set(lisDestinos)))) 
                                print(faltantes)
                                #print(len(faltantes))
                                try:
                                    myString = ", ".join(faltantes)
                                except Exception as e:
                                    myString = faltantes
                                
                                #print(myString)


                                return False, myString, nombre
                        else:
                            print("Faltan destinos de estos pedidos")
                            signals.progress.emit(90,"Faltan destinos de estos pedidos")
                            faltantes = list(filter(lambda x: x not in lisDB, list(set(lisDestinos)))) 
                            print(faltantes)
                            print(len(faltantes))

                            myString = ", ".join(faltantes) 

                            #self.ui.progress_fn(100,"Faltan todos los destinos de este archivo en la DB, no se creara el spreadsheet hasta que se inserten")
                            #self.fnMuestraMensaje(myString)
                            return False, myString, nombre
                    else:
                        signals.progress.emit(90,"No existe ningun destino")
                        return False, "No existe ningun destino de este archivo en la base de datos de destinos", nombre


                elif 'operadores' in nombre:
                    config.destinosNoDB = []
                    filename = 'OPERADORES ' + nombre.split('operadores.', 1 )[1]
                    if df1 is not None:
                        df = df1.replace(np.nan, '', regex=True)
                        print("crearSS()")
                        sh = self.ssj.crearSS(tipo, filename)

                        print("salvarDFtoSS()")
                        esto = self.ssj.salvarDFtoSS(df,sh)

                        if esto == True:

                            print("enviaHistorial")
                            envio = self.enviaHistorial(nombre + '.tsv', signals)
                            if envio == True:
                                return True, '', nombre
                            else:
                                return False, '', nombre
                    else:
                        print("El dataframe esta vacio o el archivo no existe")
                        return False, '', nombre

                elif 'destinos' in nombre:
                    if df1 is not None:
                        df1 = df1.replace(np.nan, '', regex=True)
                        print("Calcular coordenadas")
                        df2 = self.dameCoordenadas(df1, signals)
                        
                        
                        conCoordenadas = df2.loc[df2['Longitud'] != 0]

                        sinCoordenadas = df2.loc[df2['Longitud'] == 0]

                        failed = config.MODE+".DestinosRechazados."+strftime("%Y-%m-%d_%H:%M:%S", localtime())

                        #guardar sincoordenadas como rechazados en s3
                        #crea archivo faltantes
                        self.saveS3(sinCoordenadas,failed)

                        print("Enviar a DB")
                        #guardar en BD
                        df = conCoordenadas.to_json(orient='records')
                        esto = self.mandarDestinos(df)
                        print("Esto es esto")
                        print(esto)
                        if esto is not None:

                            #TODO validar campo status
                            signals.progress.emit(100,"Destinos actualizados")

                            print("enviaHistorial")
                            print(nombre)
                            envio = self.enviaHistorial(nombre + '.tsv', signals)
                            if envio == True:
                                return df2
                            else:
                                return df2
                        else:
                            signals.progress.emit(100,"Fallo al actualizar destinos")
                       
                    else:
                        print("El dataframe esta vacio o el archivo no existe")
                        



        except Exception as e:
            print(e)
            raise e


    def fnMuestraMensaje(self, mensaje):
        msgBox = QMessageBox()
        msgBox.setText("Faltan destinos de este archivo en la DB, no se creara el spreadsheet hasta que se inserten: \n \n \n" + mensaje)
        msgBox.exec_()




    def procesaCoordenadas(self, index, row, dataFrame, signals):
        json={}
        encontradas=[]
        noEncontradas=[]
        direccion = str(row['CalleNumero'])
        latitud, longitud = self.coordenadas(direccion, signals)
        if latitud != "Se necesitan mas datos" and longitud != "Se necesitan mas datos":
            if self.enMX(latitud, longitud):

                latitud = latitud.replace(".", ",")
                longitud = longitud.replace(".", ",")
                #print(latitud + longitud)

                dataFrame.set_value(index, 'Latitud', latitud, takeable=False)
                dataFrame.set_value(index, 'Longitud', longitud, takeable=False)

                #self.ui.tablePochtecaLatLong.addItem(row['CalleNumero'])
                encontradas.append(row['CalleNumero'])
            else:
                latitud = 'Se necesitan mas datos'
                longitud = 'Se necesitan mas datos'
                #print(latitud + longitud)

                dataFrame.set_value(index, 'Latitud', latitud, takeable=False)
                dataFrame.set_value(index, 'Longitud', longitud, takeable=False)

                #self.ui.tablePochtecaLatLong_2.addItem(row['CalleNumero'])
                noEncontradas.append(row['CalleNumero'])

        json['encontradas']=encontradas
        json['noEncontradas']=noEncontradas
        return json

    def dameCoordenadas(self, dataFrame, signals):
        dataFrame = dataFrame.replace(np.nan, '', regex=True)
        for index, row in dataFrame.iterrows():
            direccion = str(row['Municipio']) + ' ' + str(row['CodigoPostal']) + ' ' + str(row['CalleNumero'])
            latitud, longitud = self.coordenadas(direccion)
            print(latitud + longitud + ' Destino:' + str(row['Destino']))
            if latitud != "Se necesitan mas datos" and longitud != "Se necesitan mas datos":
                if self.enMX(latitud, longitud):

                    #latitud = latitud.replace(".", ",")
                    #longitud = longitud.replace(".", ",")
                    #print(latitud + longitud)
                    

                    #dataFrame.set_value(index, 'Latitud', latitud, takeable=False)
                    #dataFrame.set_value(index, 'Longitud', longitud, takeable=False)
                    dataFrame.loc[index, 'Latitud'] = latitud
                    dataFrame.loc[index, 'Longitud'] = longitud
                    #self.ui.tablePochtecaLatLong.addItem(row['CalleNumero'])
                else:
                    latitud = 0
                    longitud = 0
                    #print(latitud + longitud)

                    dataFrame.set_value(index, 'Latitud', latitud, takeable=False)
                    dataFrame.set_value(index, 'Longitud', longitud, takeable=False)
                    #self.ui.tablePochtecaLatLong_2.addItem(row['CalleNumero'])

        return dataFrame

    def mandarDestinos(self, destinos):
        idCedi = json.loads(config.loginData)['idCedi']
        #sss.progress.emit(80,"Enviando destinos")
        try:
            destinos = json.loads(destinos)

            for destino in destinos:
                destino['Subregion'] = json.loads(config.loginData)['cedi']
                destino['Region'] = 'Centro'
                destino['Hotel'] = "Básico"


            if(config.MODE == 'DEV'):
                url = 'https://b2uiut18x9.execute-api.us-east-1.amazonaws.com/dev/pochteca-alta-destinos'
            elif(config.MODE == 'PROD'):
                url = 'https://b2uiut18x9.execute-api.us-east-1.amazonaws.com/prod/pochteca-alta-destinos'
            
            payload = { "idCedi": idCedi, "destinos": destinos}
            #print(payload)
            headers = {'content-type': 'application/json', 'X-API-KEY': 'mtS5hV3rl53tBeGeWnfWq2pqxSRDjOvJW6L7hUb9'}

            r = requests.post(url, data=json.dumps(payload), headers=headers)
            resultado = json.loads(r.text)
            #sss.progress.emit(100,"Destinos enviados")
            #print(resultado)
            return resultado
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


    def consultarDestinos(self, destinos):
        #print('consultando destinos')

        try:
            payload = {"idCedi": json.loads(config.loginData)['idCedi'], "Destinos": destinos}
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
        except requests.exceptions.ConnectionError as errc:
            print ("Error de conexion: ",errc)
            progress_fn(0, "Verifica tu conexion")
        except requests.exceptions.Timeout as errt:
            print ("Timeout Error:",errt)
            progress_fn(0, "Verifica tu conexion - Timeout -")
        except requests.exceptions.RequestException as err:
            print ("OOps: Something Else",err)
            progress_fn(0, "Verifica tu conexion")




    def manejador(self):
        try:
            if config.mainWindow.filtrarFechas.isChecked():
                self.filtroFecha()
            else:
                '''print("imprimiendo loginData")
                                                                print(config.loginData)
                                                                print(json.loads(config.loginData)['cedi'])'''
                dato = self.leerTSVdesdeFTP(json.loads(config.loginData)['cedi'])


                resultado = json.loads(dato)
                self.ui.listWidgetPochtecaFTP.clear()

                self.ui.listDestinos.clear()
                for cosa in resultado["destinos"]:
                    self.ui.listDestinos.addItem(cosa["nombre"])

                if self.ui.radioButtonInterfasePochtecaPedidos.isChecked():

                    if self.ui.radioButtonInterfasePochtecaTodos.isChecked():
                        for cosa in resultado["pedidos"]["normales"]:
                            self.ui.listWidgetPochtecaFTP.addItem(cosa["nombre"])
                        
                        for cosa in resultado["pedidos"]["urgentes"]:
                            self.ui.listWidgetPochtecaFTP.addItem(cosa["nombre"])
                        
                        for cosa in resultado["pedidos"]["otros"]:
                            self.ui.listWidgetPochtecaFTP.addItem(cosa["nombre"])
                       
                    #print("pedidos/")
                    if self.ui.radioButtonInterfasePochtecaOrdinarios.isChecked():
                        for cosa in resultado["pedidos"]["normales"]:
                            self.ui.listWidgetPochtecaFTP.addItem(cosa["nombre"])
                        self.ui.progress_fn(100,"Se muestran NORMALES")

                    if self.ui.radioButtonInterfasePochtecaUrgentes.isChecked():
                        #print("*************")
                        #print("urgentes")
                        for cosa in resultado["pedidos"]["urgentes"]:
                            self.ui.listWidgetPochtecaFTP.addItem(cosa["nombre"])

                        self.ui.progress_fn(100,"Se muestran URGENTES")
                    

                elif self.ui.radioButtonInterfasePochtecaOperadores.isChecked():
                    
                    for cosa in resultado["operadores"]:
                        self.ui.listWidgetPochtecaFTP.addItem(cosa["nombre"])
                    self.ui.progress_fn(100,"Se muestran OPERADORES")

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

    def deactivate(self):   
        
        if self.ui.radioButtonInterfasePochtecaOperadores.isChecked():
            #print("desactivar filtros todos")
            self.ui.radioButtonInterfasePochtecaTodos.hide()
            self.ui.radioButtonInterfasePochtecaOrdinarios.hide()
            self.ui.radioButtonInterfasePochtecaCancelados.hide()
            self.ui.radioButtonInterfasePochtecaUrgentes.hide()
        elif self.ui.radioButtonInterfasePochtecaPedidos.isChecked():
            
            self.ui.radioButtonInterfasePochtecaTodos.show()
            self.ui.radioButtonInterfasePochtecaOrdinarios.show()
            self.ui.radioButtonInterfasePochtecaCancelados.show()
            self.ui.radioButtonInterfasePochtecaUrgentes.show()

    def findConfig(self):
        print("obtener campos activados y no activados")

    def leerTSVdesdeFTP(self,cedi):
        try:
            self.ui.progress_fn(20,"Leyendo archivos desde el FTP")
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

            self.ui.progress_fn(40,"Listando archivos")
            for key in conn.list_objects(Bucket='arete-arms3-ftp-pochteca')['Contents']:
                archivo = {}
                s3obj = s3.Object('arete-arms3-ftp-pochteca', key['Key'])
                nombre = s3obj.key
                #print(nombre)


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
            config.archivosDestinosFTP = destinos
            json_data = json.dumps(json_datos)
            #print(json_data)
            self.pedidos = json.dumps(pedidos)
            self.operadores = json.dumps(operadores)
            self.json_datos = json.dumps(json_datos)
            self.ui.progress_fn(100,"Se muestran archivos del FTP")
            return json_data

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

    def enviaHistorial(self, keyOrigen, signals):
        

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
            signals.progress.emit(100,"El archivo ha terminado de procesarse y se ha movido al historial")

            #llamamo manejador para actualizar la tabla de destinos
            

            return True
        except Exception as e:
            if 'NoSuchKey' in str(e):
                signals.progress.emit(100,'El archivo TSV no existe')
                print('El archivo TSV no existe')
                return False
            elif 'NoSuchBucket' in str(e):
                signals.progress.emit(100,'El bucket no existe')
                print('El bucket no existe')
                return False
            else:
                return False
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




    def enMX(self, lat, lon):
        if float(lat) < 32.523658 and float(lat) > 11.968611 and float(lon) > -122.170278 and float(lon) < -84.641667:
            #print('Si ta en MEXICO')
            return True
        else:
            #print('vale gorro, no ta.... ')
            return False


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
