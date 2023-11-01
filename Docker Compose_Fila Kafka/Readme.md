# Docker Compose e Kafka Producer/Consumer

![Docker Logo](https://www.docker.com/sites/default/files/d8/2019-07/vertical-logo-monochromatic.png)

## Introdução
Este projeto é um exemplo de como usar o Docker Compose para orquestrar um ambiente Kafka com ZooKeeper. Além disso, inclui scripts Python para produzir e consumir mensagens de um tópico específico, além de uma tradução simples das mensagens de um serviço de conselhos.

## Docker Compose
O arquivo `docker-compose.yml` descreve a configuração do ambiente. Ele cria dois serviços:

- ZooKeeper: Um serviço de coordenação para Kafka.
- Kafka: O broker do Kafka.

### Por que estamos usando Docker Compose?
O Docker Compose é uma ferramenta para definir e executar aplicativos multicontêiner em um ambiente Docker. Neste projeto, usamos o Docker Compose para configurar e executar facilmente um ambiente Kafka local com um único comando.

## Scripts
### script_produtor.py
Este script Python é responsável por produzir mensagens em um tópico Kafka chamado 'ponderada'.

![Python Logo](https://www.python.org/static/community_logos/python-logo-master-v3-TM.png)

Bibliotecas usadas:

- confluent-kafka: Uma biblioteca Python para interagir com o Kafka.

#### Como executar o script:
1. Certifique-se de ter o Docker instalado.
2. Execute o ambiente Kafka usando o Docker Compose com o comando `docker-compose up`.
3. Abra um novo terminal e execute `python script_produtor.py` para produzir mensagens.

### script_consumidor.py
Este script Python é responsável por consumir mensagens do tópico 'ponderada' e, em seguida, traduzi-las usando a API de conselhos.

![Python Logo](https://www.python.org/static/community_logos/python-logo-master-v3-TM.png)

Bibliotecas usadas:

- confluent-kafka: Uma biblioteca Python para interagir com o Kafka.
- googletrans: Uma biblioteca Python para tradução de texto.

#### Como executar o script:
1. Certifique-se de ter o Docker instalado.
2. Execute o ambiente Kafka usando o Docker Compose com o comando `docker-compose up`.
3. Abra um novo terminal e execute `python script_consumidor.py` para consumir mensagens e traduzi-las.

## Instruções para o usuário
### Pré-requisitos
Certifique-se de ter o Docker instalado em seu computador.

### Passos para executar o projeto
1. Clone este repositório para sua máquina.
2. Navegue até o diretório do projeto.
3. Execute o ambiente Kafka com o comando `docker-compose up`.
4. Abra um terminal e execute `python script_produtor.py` para produzir mensagens.
5. Abra outro terminal e execute `python script_consumidor.py` para consumir mensagens e traduzi-las.

## Referências
- [Docker Compose Documentação](https://docs.docker.com/compose/)
- [Confluent Kafka Python](https://docs.confluent.io/platform/current/clients/confluent-kafka-python/html/index.html)
- [Googletrans - Biblioteca Python para Tradução](https://pypi.org/project/googletrans/)
- [API de Conselhos](https://api.adviceslip.com/)
 
Este projeto foi desenvolvido como parte do portfólio pessoal e para fins educacionais. Se você tiver alguma dúvida ou precisar de assistência, sinta-se à vontade para entrar em contato.
