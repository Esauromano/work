import pymysql
from generales import *

class Login:
    def __init__(self):
        pass
        
    

    def validate(config,cedi,user,password):

        sql  ="""  SELECT
        user.correo, 
        user.Nombre,
        emp.IdEmpresa, 
        emp.Empresa,
        cedi.Cedi ,
        cedi.idCedi,
        cedi.FolderCedi, 
        cedi.FolderOrigen,
        cedi.FolderResultados,
        emp.SSPedidos, 
        emp.SSDestinos,
        emp.SSResultados,
        emp.SSOperadores,
        funciones
    FROM
        usuarios user 
        JOIN cedis cedi using(idCedi) -- ON (user.idCedi = cedi.idCedi) 
        JOIN empresas emp using(idEmpresa) -- ON (cedi.idEmpresa = emp.IdEmpresa) 
        left JOIN (
            select 
                idCedi
                ,concat(group_concat(nombre_funcion)) as funciones
            from
                cedi_funciones
            group by
                idCedi
        ) as funciones using (idCedi)
    WHERE
        user.correo = "{}"
        AND user.password = "{}"
        and LOWER(cedi.Cedi)= LOWER('{}'); """
            
        if config.MODE =='PROD':

            conection = {
                            "dbHost":"darum.cjvffxjbuhgo.us-east-1.rds.amazonaws.com",
                            "dbUser":"root",
                            "dbPassword":"7BAFHP!Lp'YCF7R",
                            "dbName":"ARMS3"
                        }

            #sql = "SELECT user.correo, user.Nombre, emp.IdEmpresa, emp.Empresa, cedi.Cedi, cedi.idCedi, cedi.FolderCedi, cedi.FolderOrigen, cedi.FolderResultados, emp.SSPedidos, emp.SSDestinos, emp.SSResultados, emp.SSOperadores FROM usuarios user JOIN cedis cedi ON (user.idCedi = cedi.idCedi) JOIN empresas emp ON (cedi.idEmpresa = emp.IdEmpresa) WHERE user.correo = '{}' AND user.password = '{}' and LOWER(cedi.Cedi)= LOWER('{}'); "
            response = {"message":"","status":False,"data":{}}
        elif config.MODE =='DEV':
            conection = {
                            "dbHost":"darum.cjvffxjbuhgo.us-east-1.rds.amazonaws.com",
                            "dbUser":"root",
                            "dbPassword":"7BAFHP!Lp'YCF7R",
                            "dbName":"ARMS3vDEV"
                        }
          
            #sql = "SELECT user.correo, user.Nombre, emp.IdEmpresa, emp.Empresa, cedi.Cedi, cedi.idCedi, cedi.FolderCedi, cedi.FolderOrigen, cedi.FolderResultados, emp.SSPedidos, emp.SSDestinos, emp.SSResultados, emp.SSOperadores FROM usuarios user JOIN cedis cedi ON (user.idCedi = cedi.idCedi) JOIN empresas emp ON (cedi.idEmpresa = emp.IdEmpresa) WHERE user.correo = '{}' AND user.password = '{}' and LOWER(cedi.Cedi)= LOWER('{}'); "

            response = {"message":"","status":False,"data":{}}
            
           

        try:
            db = pymysql.connect(host=conection["dbHost"], user=conection["dbUser"],
                                  passwd=conection["dbPassword"], db=conection["dbName"])
            
        except Exception as e:
            response["message"]= "error de conexión a BD"
            popup("Error de conexión a BD")
            return response
        
        if db is not None:

            success = False
            
            sql = sql.format(user, password,cedi)        
           
            try:
                with db.cursor() as cursor:            
                    cursor.execute(sql)
                    data = cursor.fetchone()
                    # Si no se encuentra al usuario
                    
                    if data is not None:
                        response["status"] = True
                        response["data"] = {
                            "correo":data[0],
                            "nombre":data[1],
                            "idEmpresa":data[2],
                            "empresa":data[3],
                            "cedi":data[4],
                            "idCedi":data[5],
                            "folderCedi":data[6],
                            "folderOrigen":data[7],
                            "folderResultados":data[8],
                            "SSPedidos":data[9],
                            "SSDestinos":data[10],
                            "SSResultados":data[11],
                            "SSOperadores":data[12],
                            "funciones":data[13],
                            "dashboards":{}
                        }
                        #buscar dashboards
                        sql2 = "select name,url from dashboards where idEmpresa ='{}';"
                        sql2 = sql2.format(data[2])
                       
                       
                        cursor.execute(sql2)
                        data2 = cursor.fetchall()
                        dashboardJson ={}
                        if data2 is not None:
                            for row2 in data2:
                                name, url = row2
                                dashboardJson[name]=url

                        response["data"]["dashboards"] = dashboardJson
                        return response
                        
                    else:
                        response["message"]="usuario inválido"
                        return response
                    
                
            except Exception as e:
                response["message"]="error de query"
                print(e)
                return response;
                
        else:
            response["message"]="error de conexión a BD"
            popup("Error de conexión a BD")
            return response
       
      

       
