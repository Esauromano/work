from PyQt5.QtWidgets import *
import config

def popup(msg):
    msgBox = QMessageBox()
    msgBox.setText(msg)
    msgBox.exec_()

def progress_fn(percent, message):
    config.mainWindow.progressBar.setValue(percent)
    config.mainWindow.labelProgress.setText(str(message))