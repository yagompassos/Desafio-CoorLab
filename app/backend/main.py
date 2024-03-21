from fastapi import FastAPI
from typing import List
import json

from .models import City


app = FastAPI()

with open('backend/data.json', 'r') as f:
    data = json.load(f)['transport']

@app.get("/")
def get_root():
    return {"msg": "Funcionando"}

@app.get("/cities", response_model=List[City])  # Especifique o modelo de resposta como List[City]
async def get_cities():
    # Conjunto para armazenar os nomes das cidades
    unique_cities = set()

    # Itera sobre a lista de transportadoras no arquivo JSON
    for transport in data:
        # Adiciona o nome da cidade ao conjunto
        unique_cities.add(transport['city'])

    # Converte o conjunto de cidades de volta para uma lista
    cities = [{"cityName": city} for city in unique_cities]

    # Retorna a lista de cidades
    return cities