import random
from pathlib import Path
import pandas as pd

random.seed(42)

ZONAS = {"Norte" : {"letra" : "N", "subestaciones" : ["SE Playa Grande", "SE Los Cocos", "SE Puerto Viejo"]},
         "Centro" : {"letra" : "C", "subestaciones" : ["SE El Morro", "SE La Plaza", "SE Rio Claro"]},
         "Sur" : {"letra" : "S", "subestaciones" : ["SE Las Salinas", "SE Bahia Sur", "SE Monte Alto"]}}

circuitos = []

for zona, info in ZONAS.items():
    for numero in range (1, 16):
        subestacion = info["subestaciones"][(numero - 1) // 5]
        fila = {"id_circuito" : f'CIR-{info["letra"]}-{numero:02d}',
                "zona" : zona,
                "subestacion" : subestacion,
                "clientes" : random.randint(1500 , 8000),
                "km_red" : round(random.uniform(5, 40), 1)}
        circuitos.append(fila)

df = pd.DataFrame(circuitos)
carpeta = Path("data/raw")
carpeta.mkdir(parents= True, exist_ok= True)
df.to_csv(carpeta / "circuitos.csv", index= False)

print(f'Se generaron {len(df)} circuitos')
print(df.head())
        