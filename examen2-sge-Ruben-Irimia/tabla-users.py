import json

import pandas as pd


file = open("secure-users.json","r")
users = json.load(file)


df = pd.json_normalize(users)
df.to_excel('usuarios.xlsx',  index=False)

