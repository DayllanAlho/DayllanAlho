import time
import requests
from confluent_kafka import Producer

def fetch_advice_from_api():
    url = "https://api.adviceslip.com/advice"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json().get("slip", {}).get("advice")
    else:
        return None

def delivery_report(err, msg):
    if err is not None:
        print(f'Erro ao entregar a mensagem: {err}')
    else:
        print(f'Conselho enviado ao tópico {msg.topic()} - Partição {msg.partition()}\n')

def main():
    conf = {
        'bootstrap.servers': 'localhost:9092',
    }

    producer = Producer(conf)

    while True:
        advice = fetch_advice_from_api()

        if advice is not None:
            message = f"Conselho: {advice}"
            producer.produce('ponderada', value=message, callback=delivery_report)
            producer.flush()
            print(message, '\n')
            time.sleep(5)
        else:
            print("Falha ao obter conselho da API")

if __name__ == '__main__':
    main()
