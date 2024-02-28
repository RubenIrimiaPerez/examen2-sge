import json

import pandas as pd

users = {}
file = open("secure-users.json", "r")
users = json.load(file)

id = []
for item in users:

        id.append(item['userId'])

contr = []
for item in users:

        contr.append(item['password'])

        df = pd.DataFrame({'idUsuario': id, 'HashContra': contr})

        df.index.name = 'ID'

        # Generar el documento
        df.to_excel(f'usuarios.xlsx')