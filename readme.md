# Ponderada OpenWeather

![OpenWeather Logo](https://openweathermap.org/themes/openweathermap/assets/img/logo_white_cropped.png)

## Introdução

Este projeto Ponderada OpenWeather utiliza Flask para criar uma API simples que consome a API do OpenWeather para fornecer informações climáticas de várias cidades. Além disso, o projeto inclui scripts para produzir dados climáticos ponderados e uma interface de banco de dados SQLite para armazenar essas informações.

## Estrutura do Projeto

O projeto é dividido em três partes principais:

- **app.py**: O arquivo principal contendo as definições de rotas e lógica da API.
- **test_app.py**: Arquivo de teste para garantir o bom funcionamento das funcionalidades principais.
- **dadosClimaticos.db**: Banco de dados SQLite para armazenar dados climáticos ponderados.

## Funcionalidades

### API de Clima

O arquivo `app.py` contém as seguintes rotas:

- `/`: Rota principal da API que fornece uma mensagem de boas-vindas.
- `/tempo`: Rota que retorna os dados climáticos ponderados armazenados no banco de dados.
- `/etl`: Rota de exemplo que retorna uma mensagem indicando que o processo ETL foi realizado.

### Testes

O arquivo `test_app.py` contém testes unitários para garantir que as funcionalidades principais do projeto estejam operacionais.

## Como Usar

### Pré-requisitos

Certifique-se de ter o Python instalado em seu computador.

### Instalação de Dependências

Instale as dependências necessárias executando o comando:

```bash
pip install -r requirements.txt
```

### Executando o Projeto
1. Clone este repositório para sua máquina.
2. Navegue até o diretório do projeto:
```
cd Ponderada-OpenWeather
```
3. Execute o aplicativo Flask:

```
python app.py
```

4. Abra um navegador e acesse http://127.0.0.1:5000/ para ver a mensagem de boas-vindas.
5. Acesse http://127.0.0.1:5000/tempo para obter os dados climáticos ponderados.
6. Para executar os testes:

```
pytest test_app.py
```

## Observações
- Este projeto utiliza Flask para criar uma API simples e SQLite para armazenar dados climáticos ponderados.
- Os testes unitários ajudam a garantir o funcionamento correto das funcionalidades do projeto.
- Certifique-se de ter uma conexão com a internet ao acessar a rota /tempo, pois ela consome a API do OpenWeather.

# Agradecimentos
Agradeço aos meus colegas de turma que me ajudaram a entender tal atividade:
  - Patrick Vitoriano
  - Giovanna Furlan
  - Lucas Britto