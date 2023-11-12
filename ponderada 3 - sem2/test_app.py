import sqlite3
import pandas as pd
import requests
from app import consultar_tempo, criar_tabela, conectar_db, app


def testar_conexao_com_db():
    conn = conectar_db()
    assert conn is not None
    assert isinstance(conn, sqlite3.Connection)


def testar_conteudo_da_tabela():
    tabela = criar_tabela()
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tabela_tempo")
    resultados = cursor.fetchall()
    conn.close()
    assert len(resultados) == len(tabela)


def testar_resposta_json():
    with app.test_client() as client:
        resposta = client.get('/tempo')
        assert resposta.status_code == 200
        dados_json = resposta.json  # Correção aqui
        assert any('Data de Ingestão' in item for item in dados_json)
        assert any('Tipo' in item for item in dados_json)
        assert any('Valores' in item for item in dados_json)
        assert any('Uso' in item for item in dados_json)


def testar_etl():
    with app.test_client() as client:
        resposta_etl = client.get('/etl')
        assert resposta_etl.status_code == 200
        assert resposta_etl.data == b'Voce esta na rota /etl'



if __name__ == '__main__':
    # Executar os testes
    testar_conexao_com_db()
    testar_conteudo_da_tabela()
    testar_resposta_json()
    testar_etl()
    print("Todos os testes passaram!")
