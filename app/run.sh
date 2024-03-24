#!/bin/bash

# Instalação das dependências Python
pip install fastapi
pip install "uvicorn[standard]"

# Executa o servidor fastapi em background
python3 -m uvicorn backend.main:app --reload --port 3000 &

# Espera um momento para o servidor do backend iniciar
sleep 5

# Navega para o diretório "frontend"
cd frontend

# Instalação das dependências do projeto Vue.js
yarn install

# Executa o servidor de desenvolvimento do Vue.js
yarn serve
