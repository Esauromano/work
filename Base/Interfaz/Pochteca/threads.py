from PyQt5.QtCore import QThread,QObject,pyqtSignal
import config
from Base.Interfaz.Pochteca.InterfazP import *
import pandas as pd
from Base.Interfaz.Pochteca.ss import ssj as ssjj





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
            sss.progress.emit(20,"Recolecta en segundo CEDI")
            if len(config.mainWindow.listWidgetPochtecaFTP.selectedIndexes()) > 1:
                sss.progress.emit(30,"Creando un archivo desde los archivos seleccionados")

                concatenados, tipo = poch.concatTSV()

                filename = tipo.upper() + ' ' + str(datetime.now()).split(" ")[0]
                
                sh = ssj.crearSS(tipo, filename)
                sss.progress.emit(50,"El archivo se ha creado")
                esto = ssj.salvarDFtoSS(concatenados, sh)
                
                #config.mainWindow.listWidgetPochtecaHistorial.addItem(filename)
                sss.progress.emit(80,"Se han guardado lso datos")
                return []

            elif len(config.mainWindow.listWidgetPochtecaFTP.selectedIndexes()) == 1:
                sss.progress.emit(30,"Creando un archivo desde el archivo seleccionado")
                for x in config.mainWindow.listWidgetPochtecaFTP.selectedIndexes():
                    status, myString, nombre = poch.open(x.data(), signals)
                    if status == False:
                        destinosNoDB.append(myString)
                return destinosNoDB  
                    
        else:
            sss.progress.emit(20,"No recolecta en segundo CEDI")
            for x in config.mainWindow.listWidgetPochtecaFTP.selectedIndexes():
                status, myString, nombre = poch.open(x.data(), signals)
                if status == False:
                    destinosNoDB.append(myString)
            return destinosNoDB
    except Exception as e:
            raise e

class ThreadSS(QThread):

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
        print("llamada a lo de los SS SSSssssssSsSss desde thread")
        w = config.mainWindow
        destinosNoDB = procesar(self.signals, self.poch, self.ssj)
        config.destinosNoDB = destinosNoDB
        self.signals.end.emit("finalizado")
        
        

class SSSignals(QObject):
    end = pyqtSignal(object)
    progress = pyqtSignal(object,object)