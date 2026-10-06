import json
from pathlib import Path
import requests

URL = "https://archive-api.open-meteo.com/v1/archive"
FECHA_INICIO = "2024-01-01"
FECHA_FIN = "2025-12-31"

ZONAS = {"Norte" : {"latitud" : 10.21, "longitud" : -64.63},
         "Centro" : {"latitud" : 10.46, "longitud" : -64.17},
         "Sur" : {"latitud" : 10.67, "longitud" : -63.25}}

def descargar_clima(latitud, longitud):
    params = {"latitude" : latitud,
              "longitude" : longitud,
              "start_date" : FECHA_INICIO,
              "end_date" : FECHA_FIN,
              "daily": "precipitation_sum,temperature_2m_max,wind_speed_10m_max",
              "timezone": "America/Caracas"}

    respuesta = requests.get(URL, params = params, timeout = 30)
    respuesta.raise_for_status()

    return respuesta.json()

def guardar_json(datos, zona):
    carpeta = Path("data/raw/clima")
    carpeta.mkdir(parents= True, exist_ok= True)
    ruta = carpeta / f'{zona.lower()}.json'
    with open(ruta, 'w', encoding= 'utf8') as archivo:
        json.dump(datos, archivo, ensure_ascii= False, indent= 2)

    return ruta 

for zona, coords in ZONAS.items():
    try:
        datos = descargar_clima(coords['latitud'], coords['longitud'])
        ruta = guardar_json(datos, zona)
        dias = len(datos['daily']['time'])
        print(f'{zona}: {dias} días guardados en {ruta}')

    except requests.RequestException as error:
        print(f'{zona}: error al descargar el clima -> {error}')