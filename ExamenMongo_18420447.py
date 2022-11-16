#Alejandro Galvez Maravilla
#18420447

from mongodb import PyMongo
import json

#Variables

varmongo = {}
varmongo["host"] = "localhost"
varmongo["db"] = "itj_estudiantes"
varmongo["port"] = 27017
varmongo["timeout"] = 1000
varmongo["user"] = ""
varmongo["password"] = "root"

def consulta_materias_estudiante(ctrl):
    obj = PyMongo(varmongo)
    filtro = {'control': ctrl}
    atributos_estudiante = {"_id": 0, "nombre": 1}
    atributos_kardex = {"_id": 0, "materia": 1, "calificacion": 1}

    obj.conectar_mongodb()
    respuesta1 = obj.consulta_mongodb('estudiantes', filtro, atributos_estudiante)
    respuesta2 = obj.consulta_mongodb('kardex', filtro, atributos_kardex)
    obj.desconectar_mongodb()

    list = {}
    dir = []
    if(respuesta1["status"]==True and respuesta2["status"]):
        list["estudiante"]=respuesta1["resultado"][0]["nombre"]
        for mat in respuesta2["resultado"]:
            listTemp={}
            listTemp["materia"]=mat["materia"]
            listTemp["calificacion"] = mat["calificacion"]
            dir.append(listTemp)
        list["materias"] = dir
    alumno = json.dumps(list)
    return alumno


print(consulta_materias_estudiante("18420100"))
