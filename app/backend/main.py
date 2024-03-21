from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import List
import json

from .models import City

app = FastAPI()

# Configurar o CORS para permitir solicitações de qualquer origem
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir solicitações de qualquer origem
    allow_credentials=True,
    allow_methods=["GET"],  # Métodos permitidos
    allow_headers=["*"],  # Cabeçalhos permitidos
)

# Abrindo a base de dados em jason para leiutra
with open('backend/data.json', 'r') as f:
    data = json.load(f)['transport']

@app.get("/")
def get_root():
    return {"msg": "Funcionando"}

# Endpoint para retornar a lista de cidades que estão com voos disponíveis
@app.get("/cities", response_model=List[City])  
async def get_cities():
    unique_cities = set()

    for transport in data:
        unique_cities.add(transport['city'])

    cities = [{"cityName": city} for city in unique_cities]

    return cities