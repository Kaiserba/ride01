
import json


Alumnos = {
    "Nombre1" : "Gabriel" , "Edad1" : 27 , "altura1" : 1.78,
    "Nombre2" : "jorge" , "Edad2" : 18 , "altura2" : 1.30,
    "Nombre3" : "raul" , "Edad3" : 19 , "altura3" : 1.50
}


json_string = json.dumps(Alumnos,
                         skipkeys = True,
                         allow_nan = True,
                         indent = 6)

print('Equivalent json string of dictionary:',
      json_string)
