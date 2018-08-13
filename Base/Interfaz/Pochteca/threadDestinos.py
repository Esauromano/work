from PyQt5.QtCore import QThread,QObject,pyqtSignal
import config
from Base.Interfaz.Pochteca.InterfazP import *
import pandas as pd
from Base.Interfaz.Pochteca.ss import ssj as ssjj





def syncDestinos(signals, pochteca, ssjj):
    if config.threadDestinosMain:
        for x in config.archivosDestinosFTP:
            print(x["key"])
            df = pochteca.open(x["key"], signals)
            

    elif len(config.mainWindow.listDestinos.selectedIndexes()) == 1:
        for x in config.mainWindow.listDestinos.selectedIndexes():
            #print(x)
            #df =  self.open(x.data())
            df = pochteca.open(x.data(), signals)
            return df

class ThreadDestinos(QThread):

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
        #print("llamada a lo de los SS SSSssssssSsSss desde nuevo thread")
        w = config.mainWindow
        df = syncDestinos(self.signals, self.poch, self.ssj)
        config.regresoThreadDestinos = df
        self.signals.end.emit(df)
        
        

class SSSignals(QObject):
    end = pyqtSignal(object)
    progress = pyqtSignal(object,object)