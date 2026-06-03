import paho.mqtt.client as mqtt
import random
import time
import json

BROKER = "YOUR_Public_ID should be pasted here"
PORT = 1883
TOPIC = "sensor/multi"

client = mqtt.Client()

print("Connecting...")
client.connect(BROKER, PORT, 60)

while True:

    data = {
        "temperature": random.randint(20, 40),
        "humidity": random.randint(40, 90),
        "pressure": random.randint(990, 1020)
    }

    payload = json.dumps(data)

    client.publish(TOPIC, payload)

    print("Sent:", payload)

    time.sleep(2)