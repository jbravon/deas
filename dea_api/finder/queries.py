import requests as req
import json
import os
from .models import DEA
from requests.api import get

#? Carga de los datos del json
# url = "http://datos.comunidad.madrid/catalogo/dataset/35609dd5-9430-4d2e-8198-3eeb277e5282/resource/c38446ec-ace1-4d22-942f-5cc4979d19ed/download/desfibriladores_externos_fuera_ambito_sanitario.json"
# response = req.get(url).json()
# with open ("deas.json", "w", encoding="utf8") as file:
#     json.dump(response, file,   ensure_ascii=False, indent=4)

di_path = os.path.realpath(__file__)[0:-10]
# print(di_path)

def get_data():
    with open(f"{di_path}deas.json", encoding="utf8") as file:
        return json.load(file)

data = get_data()["data"]
print(len(data))

#? INSERCION EN LA BD
def insert_into(dataset):
    for dea in dataset:
        codigo_dea = dea["codigo_dea"]
        direccion_ubicacion = dea["direccion_ubicacion"]
        direccion_via_nombre = dea["direccion_via_nombre"]
        direccion_portal_numero = dea["direccion_portal_numero"]
        horario_acceso = dea["horario_acceso"]
        x_utm= dea["direccion_coordenada_x"]
        y_utm= dea["direccion_coordenada_y"]

        DEA.objects.create(
            codigo_dea = codigo_dea,
            direccion_ubicacion = direccion_ubicacion,
            direccion_via_nombre = direccion_via_nombre,
            direccion_portal_numero = direccion_portal_numero,
            horario_acceso = horario_acceso,
            x_utm = x_utm,
            y_utm = y_utm
        )