from kafka import KafkaProducer
from random import random, randint
from datetime import datetime
import json

topicName = 'test'
producer = KafkaProducer(bootstrap_servers='kafka:9092')
key = None

headers = []

def create_msg(qtd_msg):
    msgs = []
    for i in range(qtd_msg):
        msgs.append({
            'codigo_cliente': i,
            'agencia': '00019',
            'valor_transacao': random() * 100,
            'tipo_transacao': ['DEPOSITO', 'SAQUE'][randint(0,1)],
            'data': datetime.now().isoformat(),
            'saldo_conta': random() * 150
        })
    return msgs

for msg in create_msg(10):
    message_data = json.dumps(msg).encode('utf-8')
    producer.send(topicName, message_data, key, headers)

producer.flush()