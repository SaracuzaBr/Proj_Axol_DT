import pika
import json
import sys
import os

# Adicionamos o caminho para importar as configurações de banco
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from database import SessionLocal
import models

def callback(ch, method, properties, body):
    """Função executada toda vez que uma mensagem chega da fila."""
    data = json.loads(body)
    print(f" [x] Processando dado: {data}")
    
    db = SessionLocal()
    try:
        # Criando o registro no banco via SQLAlchemy
        new_reading = models.SensorReading(
            machine_id=data['machine_id'],
            temperature=data['temperature'],
            vibration=data['vibration']
        )
        db.add(new_reading)
        db.commit()
        print(f" [v] Salvo no Banco com sucesso!")
    except Exception as e:
        print(f" [!] Erro ao salvar: {e}")
        db.rollback()
    finally:
        db.close()

def start_worker():
    # 1. Conecta ao RabbitMQ
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    # 2. Garante que a fila existe
    channel.queue_declare(queue='sensor_data')

    # 3. Configura o consumo
    channel.basic_consume(queue='sensor_data', on_message_callback=callback, auto_ack=True)

    print(' [*] Worker aguardando mensagens. Para sair pressione CTRL+C')
    channel.start_consuming()

if __name__ == "__main__":
    start_worker()