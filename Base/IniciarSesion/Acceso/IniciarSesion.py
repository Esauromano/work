from datetime import datetime
import os
import pymysql
import sys
import json
import config
import requests
from IO.Apis.login import Login

def block_app(activate):
    config.mainWindow.tabWidget1Principal.setCurrentIndex(0)
    number_tabs = config.mainWindow.tabWidget1Principal.count()
    print(number_tabs)
    activate = not activate
    for i in range(1, number_tabs):
        config.mainWindow.tabWidget1Principal.setTabEnabled(i, activate)

class IniciarSesion:
    def __init__(self):
        self.ui =config.mainWindow



    def authenticate(self,config):
        """Metodo para consultar si el usuario con el usuario y password existen, el cedi puede no existir"""

        cedi =  self.ui.editCEDI_3.text()
        user = self.ui.editUsuario_3.text()
        pwd  = self.ui.editClave_3.text()

        if user == "" or pwd == "" or cedi =="":
            print("falta llenar datos del usuario en login")
            return {"message":"falta llenar datos del usuario en login","status":False,"data":{}}
        else:        
            return Login.validate(config,cedi,user,pwd)

    def do_login(self):
        """Método para handlear el inicio de sesión, obtiene los datos de CEDI, usuario y password de la UI"""
        cedi = self.ui.editCEDI_3.text()
        user = self.ui.editUsuario_3.text()
        pwd = self.ui.editClave_3.text()

        if user == "" or pwd == "":
            """Lanzar error, ningun campo puede estar vacio"""
            self.ui.labelStatusBarMensaje.setText("Ingresa el usuario y la contrasena")
            print("Ingresa los campos (usuario y password) ... (Login)")
        else:
            res = self.authenticate(config)
            print(res)
            #config.loginData = json.dumps(res[1])
            #print(config.loginData)
            """Aqui se debería desbloquear la app ya que se pudo loquear correctamente"""
            

            print(res["status"])
            if res["status"]:
                config.session_started = True
                config.usuario = res["data"]
                config.loginData = json.dumps(res["data"])
               
                self.update_ui_labels()
                print("Login correcto: "+config.usuario["nombre"])
                return True

            else:
                
                config.mainWindow.labelProgress.setText("Usuario o contraseña incorrectos")
                return False

    def auth(self):
        print("cargar valores del config")
        config.mainWindow.progress_fn(50,"Verificando...")
        cedi = config.mainWindow.editCEDI_3.text()
        user = config.mainWindow.editUsuario_3.text()
        pwd  = config.mainWindow.editClave_3.text()
        if user == "" or pwd == "" or cedi =="":
            print("falta llenar datos del usuario en login")
            config.mainWindow.progress_fn(100,"Campos obligatorios para iniciar sesión")
        else:    
            loginData = Login.validate(config.MODE,cedi,user,pwd)
            if loginData["status"]:

                config.mainWindow.progress_fn(80,"Sesión iniciada...buscando pedidos")
                config.loginData = json.dumps(loginData["data"])
                #TODO quitar variables y solo dejarlo hacia loginData
                additionalData = loginData["data"]
                config.SSPedidos = additionalData["SSPedidos"]
                config.folderOrigen = additionalData["folderOrigen"]
                config.SSDestinos = additionalData["SSDestinos"]
                config.SSOperadores = additionalData["SSOperadores"]

                
                config.mainWindow.empreCedi.setText(additionalData["empresa"]+" - "+ additionalData["cedi"])
                config.mainWindow.user.setText(additionalData["nombre"])
                config.mainWindow.version.setText(config.version)
                
                config.mainWindow.tabWidget1Principal.setCurrentIndex(2)

                return True
            else:
                
                config.mainWindow.progress_fn(100,"Datos incorrectos revisa nuevamente")
        return False
        


    def update_ui_labels(self):
        self.ui.empreCedi.setText(config.usuario["empresa"] + ' ' + config.usuario["cedi"])
        self.ui.user.setText(config.usuario["nombre"])
        self.ui.labelProgress.setText("Bienvenido: " + config.usuario["nombre"])
        self.ui.version.setText(config.MODE + ' ' + config.version)



    '''def update_ui_labels(self):
                    self.ui.labelStatusBarEmpresa.setText(config.usuario["empresa"])
                    self.ui.labelStatusBarCEDI.setText(config.usuario["cedi"])
                    self.ui.labelStatusBarUser.setText(config.usuario["nombre"])
                    self.ui.labelStatusBarMensaje.setText("Bienvenido: " + config.usuario["nombre"])'''
