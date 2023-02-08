import paho.mqtt.client as mqtt
import configparser

# Load configuration from config.ini
config = configparser.ConfigParser()
config.read("config.ini")

# MQTT configuration
broker = config["MQTT"]["MQTTBroker"]
port = int(config["MQTT"]["port"])
client_id = config["MQTT"]["client_id"]

# Topic configuration
topic1 = config.get('Topic', 'topic1')
topic2 = config.get('Topic', 'topic2')
topic3 = config.get('Topic', 'topic3')

# MQTT client
client = mqtt.Client(client_id)


# Connect to MQTT broker
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT Broker!")
        client.subscribe(topic1)
        client.subscribe(topic2)
        client.subscribe(topic3)
    else:
        print("Failed to connect, return code %d\n", rc)


client.on_connect = on_connect


# Callback function when a message is received
def on_message(client, userdata, message):
    print("Received message '" + str(message.payload.decode("utf-8")) + "' on topic '" + message.topic + "'")


client.on_message = on_message

# Connect to MQTT broker
client.connect(broker, port)

# Start MQTT loop
client.loop_forever()
