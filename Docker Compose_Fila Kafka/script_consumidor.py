from confluent_kafka import Consumer
from googletrans import Translator

def translate_text(text):
    translator = Translator()
    translated_text = translator.translate(text, src='en', dest='pt')
    return translated_text.text

def consume_advice():
    conf = {
        'bootstrap.servers': 'localhost:9092',
        'group.id': 'meu_grupo_consumidor',
        'auto.offset.reset': 'earliest',
    }

    consumer = Consumer(conf)
    consumer.subscribe(['ponderada'])

    try:
        while True:
            msg = consumer.poll(5.0)
            if msg is None:
                continue
            if msg.error():
                print(f"Erro ao consumir mensagem: {msg.error()}")
            else:
                advice = msg.value().decode('utf-8')
                print(f"Mensagem em inglês: {advice}\n\n\n")
                
                translated_advice = translate_text(advice)
                print(f"Mensagem traduzida para o português: {translated_advice}\n")

    except KeyboardInterrupt:
        pass
    finally:
        consumer.close()

if __name__ == '__main__':
    consume_advice()
