#from flask import Flask, render_template, request, redirect, url_for
import json
import os

app = Flask(__name__)
DATA_FILE = 'poupanca.json'

# Inicializa arquivo se não existir
def init_data():
    if not os.path.exists(DATA_FILE):
        meses = ["janeiro", "fevereiro", "marco", "abril", "maio", "junho",
                 "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
        data = {mes: [0, 0, 0, 0] * 4 for mes in meses}  # 4 semanas x 4 dias = 16 entradas
        with open(DATA_FILE, 'w') as f:
            json.dump(data, f)

# Lê os dados do arquivo JSON
def ler_dados():
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

# Salva os dados no arquivo JSON
def salvar_dados(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f)

@app.route('/')
def index():