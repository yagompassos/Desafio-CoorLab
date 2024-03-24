from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import List
import json

from .models import City, Transport
from .services import get_best_transport_options

app = FastAPI()

# Configurar o CORS para permitir solicitações de qualquer origem
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir solicitações de qualquer origem
    allow_credentials=True,
    allow_methods=["GET"],  # Métodos permitidos
    allow_headers=["*"],  # Cabeçalhos permitidos
)

# Opening json data base for reading
with open('backend/data.json', 'r') as f:
    data = json.load(f)['transport']

print(data)

@app.get("/")
def get_root():
    return {"msg": "Funcionando"}

# Endpoint that returns the list of cities with available flights in the data base in the moment
@app.get("/cities", response_model=List[City])  
async def get_cities():
    unique_cities = set()

    for transport in data:
        unique_cities.add(transport['city'])

    cities = [{"cityName": city} for city in unique_cities]

    return cities

@app.get("/best_transport/{city}", response_model=dict)  
async def get_best_transport(city: str):
    best_transport_options = get_best_transport_options(city, data)
    return best_transport_options