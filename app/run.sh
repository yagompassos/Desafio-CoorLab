#!/bin/bash

# Instalação das dependências Python
pip install flask

# Executa o servidor Flask em background
python backend/main.py &

# Espera um momento para o servidor Flask iniciar
sleep 5

# Navega para o diretório "frontend"
cd frontend

# Instalação das dependências do projeto Vue.js
yarn install

# Executa o servidor de desenvolvimento do Vue.js
yarn serve
