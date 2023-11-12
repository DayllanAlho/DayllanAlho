import pandas as pd
from datetime import datetime
import requests
from flask import Flask, jsonify
from sqlalchemy import create_engine
import sqlite3
import json

app = Flask(__name__)

cidades = [
    "São Paulo", "Rio de Janeiro", "Niterói", "São Gonçalo", "Guapimirim", "Recife", "Magé", "Búzios",
    "Maricá", "São Pedro da Aldeia", "Nova Iguaçu"
]


def consultar_tempo():
    url = "https://api.openweathermap.org/data/2.5/weather"
    parametros = {
        "appid": "7058a786edbe467bb14b38cd5bdc54dd",
    }
    dados = []
    for cidade in cidades:
        parametros["q"] = cidade
        resposta_consulta = requests.get(url, params=parametros)

        if resposta_consulta.status_code == 200:
            dado = resposta_consulta.json()
            dados.append(dado)
        else:
            print(f"Error: {resposta_consulta.status_code} - {resposta_consulta.text}")
    return dados


def criar_tabela():
    data_atual = datetime.now()

    valores = consultar_tempo()
    valores = [json.dumps(item) for item in valores]

    dados_df = {
        'Data de Ingestão': [data_atual] * len(valores),
        'Tipo': [f"Clima {cidade}" for cidade in cidades],
        'Valores': valores,
        'Uso': ["Previsão do Tempo"] * len(valores)
    }

    df = pd.DataFrame(dados_df)

    engine = create_engine('sqlite:///dadosClimaticos.db', echo=False)

    df.to_sql('tabela_tempo', con=engine, if_exists='replace', index=False)

    return df


def conectar_db():
    conn = sqlite3.connect('dadosClimaticos.db')
    return conn


@app.route('/')
def inciar_api():
    return 'API Flask aberta. Digite "/tempo" para ver o tempo.'


@app.route('/tempo')
def obter_tempo():
    if 'cached_response' not in app.config:
        app.config['cached_response'] = criar_tabela().to_dict(orient='records')

    return jsonify(app.config['cached_response'])


@app.route('/etl')
def sua_funcao_etl():
    return 'Voce esta na rota /etl'


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)