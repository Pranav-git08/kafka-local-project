from confluent_kafka import Producer
import json
import time

config = {'bootstrap.servers': 'localhost:9092'}
producer = Producer(config)

def delivery_report(err, msg):
    if err is not None:
        print(f"Delivery failed: {err}")
    else:
        print(f"Delivered to {msg.topic()} [{msg.partition()}]")

print("Starting Producer. Type Ctrl+C to stop.")

try:
    count = 0
    while True:
        data = {'sensor_id': 'sensor_01', 'temp': 20 + (count % 10)}
        producer.produce('test-topic', json.dumps(data).encode('utf-8'), callback=delivery_report)
        producer.poll(0)
        time.sleep(1)
        count += 1
except KeyboardInterrupt:
    pass
finally:
    producer.flush()
