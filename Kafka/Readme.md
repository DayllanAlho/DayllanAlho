# Docker Compose e Kafka Produtor/Consumidor

![Docker Logo](https://github.com/DayllanAlho/DayllanAlho/blob/dev/Kafka/Imagens/Logo%20do%20Docker%20Compose.png)

## Introdução

Essa atividade ponderada é um exemplo de como utilizar do Docker Compose para orquestrar um ambiente Kafka com ZooKeeper. Além disso, inclui scripts Python para produzir e consumir mensagens de um tópico específico, além de uma tradução simples das mensagens de um serviço de conselhos.

## Docker Compose

O arquivo `docker-compose.yml` descreve a configuração do ambiente. Ele cria dois serviços:

- :white_flower: **ZooKeeper**: Um serviço de coordenação para Kafka.
- :whale: **Kafka**: O broker do Kafka.

### :interrobang: Por que estamos usando Docker Compose?

O Docker Compose é uma ferramenta para definir e executar aplicativos multicontêiner em um ambiente Docker. Neste projeto, usamos o Docker Compose para configurar e executar facilmente um ambiente Kafka local com um único comando.

## :newspaper: Scripts

### :snake: `script_produtor.py`

Este script Python é responsável por produzir mensagens em um tópico Kafka chamado 'ponderada'.

![Python Logo](https://www.python.org/static/community_logos/python-logo-master-v3-TM.png)

**Bibliotecas usadas:**

- :package: `confluent-kafka`: Uma biblioteca Python para interagir com o Kafka.

#### :wrench: Como executar o script:

1. Certifique-se de ter o Docker instalado.
2. Execute o ambiente Kafka usando o Docker Compose com o comando `docker-compose up`.
3. Abra um novo terminal e execute `python script_produtor.py` para produzir mensagens.

### :snake: `script_consumidor.py`

Este script Python é responsável por consumir mensagens do tópico 'ponderada' e, em seguida, traduzi-las usando a API de conselhos.

![Python Logo](https://www.python.org/static/community_logos/python-logo-master-v3-TM.png)

**Bibliotecas usadas:**

- :package: `confluent-kafka`: Uma biblioteca Python para interagir com o Kafka.
- :package: `googletrans`: Uma biblioteca Python para tradução de texto.

#### :wrench: Como executar o script:

1. Certifique-se de ter o Docker instalado.
2. Execute o ambiente Kafka usando o Docker Compose com o comando `docker-compose up`.
3. Abra um novo terminal e execute `python script_consumidor.py` para consumir mensagens e traduzi-las.

## Instruções para o usuário

### Pré-requisitos

Certifique-se de ter o Docker instalado em seu computador.

### :books: Bibliotecas utilizadas

Para executar os scripts Python, você pode precisar instalar algumas bibliotecas. Você pode instalá-las usando o comando `pip install <nome_da_biblioteca>`. As bibliotecas usadas são:

- `confluent-kafka`
- `googletrans`

### :footprints: Passos para executar o projeto

1. Clone este repositório para sua máquina.
2. Navegue até o diretório do projeto.
3. Execute o ambiente Kafka com o comando `docker-compose up`.
4. Abra um terminal e execute `python script_produtor.py` para produzir mensagens.
5. Abra outro terminal e execute `python script_consumidor.py` para consumir mensagens e traduzi-las.

### :mag: Observações

- Você pode optar por executar o projeto em uma máquina virtual, mas preferi fazer com o VS Code, pois tinha mais afinidade com essa IDE.

## :eyeglasses: Referências

- [Docker Compose Documentação](https://docs.docker.com/compose/)
- [Confluent Kafka Python](https://docs.confluent.io/platform/current/clients/confluent-kafka-python/html/index.html)
- [Googletrans - Biblioteca Python para Tradução](https://pypi.org/project/googletrans/)
- [API de Conselhos](https://api.adviceslip.com/)
- [Exemplo de configuração Kafka (github.com/mrugankray)](https://github.com/mrugankray/Big-Data-Cluster/blob/main/kafka-zookeper.yaml)
- [Exemplo de configuração Kafka e Python (github.com/felipesilvamelo28)](https://github.com/felipesilvamelo28/kafka-example)
- [Outro exemplo de configuração Docker Compose (github.com/mrugankray)](https://github.com/mrugankray/Big-Data-Cluster/blob/main/all-docker-compose.yaml)