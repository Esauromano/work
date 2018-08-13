import pymysql
import config
import json

class destinosDB:
    def __init__(self):
        pass
        
    

    def traerDestinos(self):
        idCedi = json.loads(config.loginData)['idCedi']
        print("idCedi")
        print(idCedi)

        if config.MODE =='PROD':

            conection = {
                            "dbHost":"darum.cjvffxjbuhgo.us-east-1.rds.amazonaws.com",
                            "dbUser":"root",
                            "dbPassword":"7BAFHP!Lp'YCF7R",
                            "dbName":"ARMS3"
                        }

            esto = "SELECT Destino, CAST(Latitud AS Float) AS Latitud, Longitud, RestriccionVehiculo, RestriccionVolumen, if(Dedicado = 1, 'Sí', 'No') as Dedicado, Region, Subregion, Estado, Municipio, Colonia, CalleNumero, CodigoPostal, left(DATE_FORMAT(VentanaInicioDestino, '%T'),8) VentanaInicioDestino, left(DATE_FORMAT(VentanaFinDestino, '%T'),8) VentanaFinDestino, DesfaseHorario, if(L = 1, 'Sí', 'No') as L, if(M = 1, 'Sí', 'No') as M, if(Mi = 1, 'Sí', 'No') as Mi, if(J = 1, 'Sí', 'No') as J, if(V = 1, 'Sí', 'No') as V, if(S = 1, 'Sí', 'No') as S, if(D = 1, 'Sí', 'No') as D, TiemServicio, Contacto1, Telefono1, Correo1, Contacto2, Telefono2, Correo2, Hotel, FactorSubidaS, FactorSubidaM, FactorSubidaL, FactorIntermedioS, FactorIntermedioM, FactorIntermedioL, FactorRetornoS, FactorRetornoM, FactorRetornoL from destinos WHERE idCedi=\""+ str(idCedi) +"\";"
            sql = esto
        elif config.MODE =='DEV':
            conection = {
                            "dbHost":"darum.cjvffxjbuhgo.us-east-1.rds.amazonaws.com",
                            "dbUser":"root",
                            "dbPassword":"7BAFHP!Lp'YCF7R",
                            "dbName":"ARMS3vDEV"
                        }
            esto = "SELECT Destino, CAST(Latitud AS CHAR) AS Latitud, CAST(Longitud AS CHAR) AS Longitud, RestriccionVehiculo, RestriccionVolumen, if(Dedicado = 1, 'Sí', 'No') as Dedicado, Region, Subregion, Estado, Municipio, Colonia, CalleNumero, CodigoPostal, left(DATE_FORMAT(VentanaInicioDestino, '%T'),8) VentanaInicioDestino, left(DATE_FORMAT(VentanaFinDestino, '%T'),8) VentanaFinDestino, DesfaseHorario, if(L = 1, 'Sí', 'No') as L, if(M = 1, 'Sí', 'No') as M, if(Mi = 1, 'Sí', 'No') as Mi, if(J = 1, 'Sí', 'No') as J, if(V = 1, 'Sí', 'No') as V, if(S = 1, 'Sí', 'No') as S, if(D = 1, 'Sí', 'No') as D, TiemServicio, Contacto1, Telefono1, Correo1, Contacto2, Telefono2, Correo2, Hotel, FactorSubidaS, FactorSubidaM, FactorSubidaL, FactorIntermedioS, FactorIntermedioM, FactorIntermedioL, FactorRetornoS, FactorRetornoM, FactorRetornoL from destinos WHERE idCedi=\""+ str(idCedi) +"\";"
            sql = esto

        response = {"message":"","status":False,"data":{}}
        

        try:
            db = pymysql.connect(host=conection["dbHost"], 
                                 user=conection["dbUser"],
                                 passwd=conection["dbPassword"], db=conection["dbName"],
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
            #print(db)
        except Exception as e:
            response["message"]= "error de conexión a BD"

            
            #print(response)
            return response
        
        if db is not None:

            try:
                with db.cursor() as cursor:            
                    cursor.execute(sql)
                    data = cursor.fetchall()
                    # Si no se encuentra al usuario
                   
                    if data is not None:
                        response["status"] = True
                        response["data"] = data
                        
                        #print(response)
                        return response
                        
                    else:
                        response["message"]="No hay planes en la DB"
                        
                        #print(response)
                        return response
                    
                
            except Exception as e:
                response["message"]="error de query"
                print(e)
                
                #print(response)
                return response
        else:
            response["message"]="error de conexión a BD"
            
            #print(response)
            return response
       
                                  
        print("___________________________________________")




    def updateRow(self, obj, recalcular):
        idCedi = json.loads(config.loginData)['idCedi']
        if config.MODE =='PROD':

            conection = {
                            "dbHost":"darum.cjvffxjbuhgo.us-east-1.rds.amazonaws.com",
                            "dbUser":"root",
                            "dbPassword":"7BAFHP!Lp'YCF7R",
                            "dbName":"ARMS3"
                        }
            
            esto = "UPDATE destinos SET Destino=%s, Latitud==%s, Longitud=%s, RestriccionVehiculo=%s, RestriccionVolumen=%s, Dedicado=%s, Region=%s, Subregion=%s, Estado=%s, Municipio=%s, Colonia=%s, CalleNumero=%s, CodigoPostal=%s, VentanaInicioDestino=%s, VentanaFinDestino=%s, DesfaseHorario=%s, L=%s, M=%s, Mi=%s, J=%s, V=%s, S=%s, D=%s, TiemServicio=%s, Contacto1=%s, Telefono1=%s, Correo1=%s, Contacto2=%s, Telefono2=%s, Correo2=%s, Hotel=%s, FactorSubidaS=%s, FactorSubidaM=%s, FactorSubidaL=%s, FactorIntermedioS=%s, FactorIntermedioM=%s, FactorIntermedioL=%s, FactorRetornoS=%s, FactorRetornoM=%s, FactorRetornoL=%s, RecalcularDestino=%s, Validado=%s WHERE Destino=%s AND idCedi=%s;"
            sql = esto
        elif config.MODE =='DEV':
            conection = {
                            "dbHost":"darum.cjvffxjbuhgo.us-east-1.rds.amazonaws.com",
                            "dbUser":"root",
                            "dbPassword":"7BAFHP!Lp'YCF7R",
                            "dbName":"ARMS3vDEV"
                        }
            esto = "UPDATE destinos SET Destino=%s, Latitud=%s, Longitud=%s, RestriccionVehiculo=%s, RestriccionVolumen=%s, Dedicado=%s, Region=%s, Subregion=%s, Estado=%s, Municipio=%s, Colonia=%s, CalleNumero=%s, CodigoPostal=%s, VentanaInicioDestino=%s, VentanaFinDestino=%s, DesfaseHorario=%s, L=%s, M=%s, Mi=%s, J=%s, V=%s, S=%s, D=%s, TiemServicio=%s, Contacto1=%s, Telefono1=%s, Correo1=%s, Contacto2=%s, Telefono2=%s, Correo2=%s, Hotel=%s, FactorSubidaS=%s, FactorSubidaM=%s, FactorSubidaL=%s, FactorIntermedioS=%s, FactorIntermedioM=%s, FactorIntermedioL=%s, FactorRetornoS=%s, FactorRetornoM=%s, FactorRetornoL=%s, RecalcularDestino=%s, Validado=%s WHERE Destino=%s AND idCedi=%s;"
            sql = esto



        response = {"message":"","status":False,"data":{}}
        print("validando login")
        
        sqlSelectUpdated   = "SELECT * from destinos WHERE Destino=\"" + obj['Destino'] +  "\";"
        try:
            db = pymysql.connect(host=conection["dbHost"], 
                                 user=conection["dbUser"],
                                 passwd=conection["dbPassword"], db=conection["dbName"],
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor,
                                 autocommit=True)
            #print(db)
        except Exception as e:
            response["message"]= "error de conexión a BD"

            
            #print(response)
            return response
        
        if db is not None:

            try:
                with db.cursor() as cursor:            
                    cursor.execute(sql, (obj['Destino'], obj['Latitud'], obj['Longitud'], obj['RestriccionVehiculo'], obj['RestriccionVolumen'], obj['Dedicado'], obj['Region'], obj['Subregion'], obj['Estado'], obj['Municipio'], obj['Colonia'], obj['CalleNumero'], obj['CodigoPostal'], obj['VentanaInicioDestino'], obj['VentanaFinDestino'], obj['DesfaseHorario'], obj['L'], obj['M'], obj['Mi'], obj['J'], obj['V'], obj['S'], obj['D'], obj['TiemServicio'], obj['Contacto1'], obj['Telefono1'], obj['Correo1'], obj['Contacto2'], obj['Telefono2'], obj['Correo2'], obj['Hotel'], obj['FactorSubidaS'], obj['FactorSubidaM'], obj['FactorSubidaL'], obj['FactorIntermedioS'], obj['FactorIntermedioM'], obj['FactorIntermedioL'], obj['FactorRetornoS'], obj['FactorRetornoM'], obj['FactorRetornoL'], recalcular, 1, obj['Destino'], idCedi))

                    cursor.execute(sqlSelectUpdated)

                    data = cursor.fetchall()
                    '''for column in data:
                                                            
                        print(column)'''
                    # Si no se encuentra al usuario
                   
                    if data is not None:
                        response["status"] = True
                        response["data"] = data
                        
                        #print(response)
                        return response
                        
                    else:
                        response["message"]="No hay planes en la DB"
                        
                        #print(response)
                        return response
                    
                
            except Exception as e:
                response["message"]="error de query"
                print(e)
                
                #print(response)
                return response
        else:
            response["message"]="error de conexión a BD"
            
            #print(response)
            return response
       
                                  
        print("___________________________________________")
