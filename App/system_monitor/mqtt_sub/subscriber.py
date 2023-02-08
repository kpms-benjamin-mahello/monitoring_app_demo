import configparser
import json
# import insert_api

from paho.mqtt import client as mqtt_client

config = configparser.ConfigParser()
config.read("config.ini")

broker = config["MQTT"]["MQTTBroker"]
port = int(config["MQTT"]["port"])
client_id = config["MQTT"]["client_id"]

topic1 = "/KPMS/5248524/SystemMonitor/Status"
topic2 = "/KPMS/5248524/SystemMonitor/Docker/PostgreSQL/CPU"
topic3 = "/KPMS/5248524/SystemMonitor/System/RAM"


def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
            client.subscribe([(topic1, 1), (topic2, 1), (topic3, 1)])

        elif rc == 1:
            print("Wrong protocol version , return code %d\n", rc)
        elif rc == 2:
            print("Identification failed , return code %d\n", rc)
        elif rc == 3:
            print("Server not reachable , return code %d\n", rc)
        elif rc == 4:
            print("Incorrect username or password , return code %d\n", rc)
        else:
            print("Invalid , return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    # client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def on_message(client, userdata, message):
    try:
        print("Received `{payload}` from `{topic}` topic".format(payload=message.payload.decode(), topic=message.topic))
    except Exception as e:
        print("Error in on_message:" + str(e))


def run():
    Connected = False  # global variable for the state of the connection
    client = connect_mqtt()
    client.on_message = on_message
    client.loop_forever()


if __name__ == '__main__':
    run()
