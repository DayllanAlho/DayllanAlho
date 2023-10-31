from confluent_kafka import Producer

producer = Producer({'bootstrap.servers': 'kafka:9092'})

def delivery_report(err, msg):
    if err is not None:
        print('Mensagem não enviada: {}'.format(err))
    else:
        print('Mensagem enviada para tópico [{}]'.format(msg.topic()))

# Envie uma mensagem para o tópico "meu-topico" (ou o tópico que você criou)
producer.produce('meu-topico', key='chave', value='Minha mensagem', callback=delivery_report)

# Espere até que todos os relatórios de entrega estejam prontos
producer.flush()
