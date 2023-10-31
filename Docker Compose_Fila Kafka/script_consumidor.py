from confluent_kafka import Consumer, KafkaError

# Configurações do consumidor Kafka
conf = {
    'bootstrap.servers': 'kafka:9092',  # Endereço do servidor Kafka
    'group.id': 'my-consumer-group',
    'auto.offset.reset': 'earliest'  # Começa a ler a partir do início do tópico
}

print(conf)

# Cria um consumidor Kafka
consumer = Consumer(conf)

# Tópico do qual você deseja consumir mensagens
topic = 'meu-topico'  # Use o mesmo tópico que no produtor

# Se inscreve no tópico
consumer.subscribe([topic])

# Loop para consumir mensagens
while True:
    msg = consumer.poll(1.0)

    if msg is None:
        continue
    if msg.error():
        if msg.error().code() == KafkaError._PARTITION_EOF:
            print('Fim da partição, continuando...')
        else:
            print('Erro no consumo: {}'.format(msg.error()))
    else:
        print('Mensagem recebida: {}'.format(msg.value()))
