import paho.mqtt.client as mqtt
import time
import configparser

# Load configuration from config.ini
config = configparser.ConfigParser()
config.read("config.ini")

# MQTT configuration
broker = config["MQTT"]["MQTTBroker"]
port = int(config["MQTT"]["port"])
client_id = config["MQTT"]["client_id"]

sendAsMQTT = config.getboolean('MQTT', 'sendAsMQTT')

# Topic configuration
topic1 = config.get('Topic', 'topic1')
topic2 = config.get('Topic', 'topic2')
topic3 = config.get('Topic', 'topic3')

sendAsMQTT = config.getboolean('MQTT', 'sendAsMQTT')
sendSystem = config.getboolean('MQTT', 'sendSystem')
sendDocker = config.getboolean('MQTT', 'sendDocker')

# MQTT client
client = mqtt.Client(client_id)

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

def on_publish(client, userdata, mid):
    print("Message published with ID: ", mid)

# Connect to MQTT broker
client.on_connect = on_connect
client.on_publish = on_publish
client.connect(broker, port)
client.loop_start()

# Send status via MQTT
def send_status(status):
    if sendAsMQTT:
        topic1 = config.get('Topic', 'topic1')
        (result, mid) = client.publish(topic1, status)

    elif sendSystem:
        topic2 = config.get('Topic', 'topic2')
        (result, mid) = client.publish(topic2, status)

    elif sendDocker:
        topic3 = config.get('Topic', 'topic3')
        (result, mid) = client.publish(topic3, status)

    else:
        print("No MQTT topic selected")

# Schedule MQTT tasks
while True:
    send_status("status updated")
    time.sleep(5)
