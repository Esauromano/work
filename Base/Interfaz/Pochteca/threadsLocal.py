from PyQt5 import QtCore, QtWidgets, QtWebEngineWidgets, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import config
from Base.Interfaz.Pochteca.InterfazP import *
import pandas as pd
from Base.Interfaz.Pochteca.ss import ssj as ssjj
import csv




def procesar(signals, pochteca, ssjj):
    print("Entrando al mero thread, a procesar")
    try:
        print("Clase Pochteca")
        poch = pochteca
        print("Clase ssj")
        ssj = ssjj
        sss = signals
        destinosNoDB = []
        sss.progress.emit(10,"Procesando archivos seleccionados")
        permiso = json.loads(config.loginData)['funciones']
        print(permiso)

        if permiso.split(',')[0] == 'recoleccion segundo cedi':
            print('recoleccion segundo cedi')
            if len(config.mainWindow.listWidgetPochtecaFTP.selectedIndexes()) > 1:
                sss.progress.emit(30,"Creando un archivo desde los archivos seleccionados")

                concatenados, tipo = poch.concatTSV()

                filename = tipo.upper() + ' ' + str(datetime.now()).split(" ")[0]
                
                sh = ssj.crearSS(tipo, filename)
                
                esto = ssj.salvarDFtoSS(concatenados, sh)
                
                #config.mainWindow.listWidgetPochtecaHistorial.addItem(filename)
                return []

            elif len(config.mainWindow.listWidgetPochtecaFTP.selectedIndexes()) == 1:

                for x in config.mainWindow.listWidgetPochtecaFTP.selectedIndexes():
                    status, myString, nombre = poch.open(x.data(), signals)
                    if status == False:
                        destinosNoDB.append(myString)
                return destinosNoDB  
                    
        else:
                for x in config.mainWindow.listWidgetPochtecaFTP.selectedIndexes():
                    status, myString, nombre = poch.open(x.data(), signals)
                    if status == False:
                        destinosNoDB.append(myString)
                return destinosNoDB
    except Exception as e:
            raise e

def cosa():
    print("WORK WORK WORK")


def abrirLocal(pochteca, signals, nombre, tipos):
    colDestinos = ['Destino', 'CalleNumero', 'Colonia', 'Municipio', 'Estado', 'CodigoPostal', 'Latitud', 'Longitud', 'RestriccionVehiculo', 'RestriccionVolumen', 'Dedicado', 'VentanaInicioDestino', 'VentanaFinDestino', 'L', 'M', 'Mi', 'J', 'V', 'S', 'D', 'TiemServicio', 'Contacto1', 'Telefono1', 'Correo1', 'Contacto2', 'Telefono2', 'Correo2']
    poch = pochteca
    config.columnasDestinos == True
    print(nombre)
    if nombre.endswith('.tsv'):
        print("tsv")
        dataFrame = pd.read_csv(nombre, sep="\t", decimal=",", quoting=csv.QUOTE_NONE)
        dataFrame = dataFrame.replace('No', 0)
        dataFrame = dataFrame.replace('Sí', 1)
        dataFrame = dataFrame.replace('NO', 0)
        dataFrame = dataFrame.replace('Si', 1)
        dataFrame = dataFrame.replace('SI', 1)

        if 'destinos' in nombre:
            config.fileType = 'destinos'
            if set(colDestinos) == set(dataFrame.columns.values):
                config.columnasDestinos == True
                poch.procesoDestinos(dataFrame, nombre)
            else:
                print(dataFrame.columns.values)
                print("colDestinos")
                print(colDestinos)
                config.columnasDestinos=False

        elif 'pedidos' in nombre:
            config.fileType = 'pedidos'
            print("hay pedidos")
            config.columnasDestinos == True
            status, string, archivo = poch.procesoPedidos(dataFrame, nombre)

        elif 'operadores' in nombre:
            config.fileType = 'operadores'
            print("Hay operadores")
            config.columnasDestinos == True
            poch.procesoOperadores(dataFrame, nombre)


    elif nombre.endswith('.xlsx'):
        print("xlsx")
        workbook = pd.ExcelFile(nombre)
        hojas = {}
        for sheet_name in workbook.sheet_names:
            df = workbook.parse(sheet_name)
            hojas[sheet_name] = df
        if 'destinos' in hojas:
            config.fileType = 'destinos'
            if set(colDestinos) == set(dataFrame.columns.values):
                poch.procesoDestinos(hojas['destinos'], nombre)

        elif 'pedidos' in hojas:
            config.fileType = 'pedidos'
            print("hay pedidos")
            poch.procesoPedidos(hojas['pedidos'], nombre)

        elif 'operadores' in hojas:
            config.fileType = 'operadores'
            print("Hay operadores")
            poch.procesoOperadores(hojas['operadores'], nombre)

class Locales(QThread):

    def __init__(self):
        QThread.__init__(self)
        self.signals = SSSignals()
        config.signals = self.signals
        self.poch = InterfazPochteca(config.mainWindow, self.signals)
        self.ssj = ssjj(config.mainWindow)
        

    def __del__(self):
        self.wait()

    def run(self):
        #testing
        print("Comienza a abrir archivos")
        w = config.mainWindow
        nombre = config.nombre
        tipos = config.tipos
        config.destinosNoDB = None
        abrirLocal(self.poch, self.signals, nombre, tipos)
        cosa()
        self.signals.end.emit("finalizado")
        
        

class SSSignals(QObject):
    end = pyqtSignal(object)
    progress = pyqtSignal(object,object)