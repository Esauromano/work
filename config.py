import pandas as pd

xxx = 0
progressBar = 0
labelMensaje = ''
optimiza = ''
vacio = 0
cercania = 0
valor = 0
ventana = 0
volumen = 0
peso = 0
ignoraAcceso = 0
ignoraMatriz = 0
cont = 0
mainWindow = 0
dashboards_cargados = 0
distancia_al_destino = 0
tiempo_google_al_destino = 0
contadorReubicados = 0

pdb=''

destinosNoDB = None
columnasDestinos=True
procesoExitoso=False
fileType=None


MODE = 'DEV'
version = "1.0.1"
origen = ''
idPlantillaPedidos = ''
loginData = ''
SSPedidos = ''
folderOrigen = ''
SSDestinos = ''
SSOperadores = ''
enviroment=["arete-arms3-ftp-pochteca","AKIAIGPFZH4MAPGTNCGQ","jzL4NBcqMNTedPChg0CaytfIk5vu2yHaHKZM6PHQ"]
enviromentS3Read=["arete-arms3-ftp-pochteca","AKIAIGPFZH4MAPGTNCGQ","jzL4NBcqMNTedPChg0CaytfIk5vu2yHaHKZM6PHQ"]

signals = ''
regresoThreadDestinos=None
archivosDestinosFTP=None
threadDestinosMain=False


# SS
gc = None
sheet = None
ss_nombre_resultados = ''

# pandas DataFrames
dfResultados = 0
dfCompatibilidad = 0
txtArcos = 0
TableroOriginal = 0
TableroOptimizado = 0
B = None # bitacora
bitacora = []
b = ''
bAbierto = False

#Login Data
session_started = False
usuario = dict()

pedidos = {}
vehiculos = {}
operadores = {}
resultados = []
destinos = {}
preferencias = {}
tarifario = {}
compatibilidad = {}


#credenciales s3
aws_access_key_id = 'AKIAJEFVIQQQ7VJB7NAQ'
aws_secret_access_key = '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'
Bucket='arete-arms3-ftp-pochteca'