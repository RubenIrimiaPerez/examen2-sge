#Hacer un script de nombre securizar.py en el que se cree un nuevo JSON
#a partir de users.json de nombre secure-users.json en el que las contraseñas estén hasheadas
import hashlib
import json


users = {}
file = open("users.json","r")
users = json.load(file)

print(users)


for item in users:
    password = item["password"]
    hash_password = hashlib.sha1(password.encode()).hexdigest()
    item["password"] = hash_password



fichero_creado = open("secure-users.json","a")

json.dump(users,fichero_creado)





