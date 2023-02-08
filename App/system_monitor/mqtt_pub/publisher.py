import json
import time
import configparser
from paho.mqtt import client as mqtt_client
import requests

config = configparser.ConfigParser()
config.read("config.ini")

# broker = config["MQTT"]["MQTTBroker"]
# port = int(config["MQTT"]["port"])
client_id = config["MQTT"]["client_id"]
# system_url = config["URL"]["system_url"]
# docker_url = config["URL"]["docker_url"]

sendAsMQTT = False
sendSystem = True
sendDocker = False

topic = "/KPMS/5248524/SystemMonitor/Status"
topic1 = "/KPMS/5248524/SystemMonitor/Docker/PostgreSQL/CPU"
topic2 = "/KPMS/5248524/SystemMonitor/System/RAM"


def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        global FLAG_CONNECTED
        if rc == 0:
            FLAG_CONNECTED = 1
            print("Connected to MQTT Broker!")
            client.subscribe(topic)
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    # client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


# Incase of disconnection subscribe to a Topic
def on_disconnect(client, userdata, rc):
    def on_disconnect(client, userdata, rc):
        print("Connected with result code " + str(rc))
        client.subscribe(topic)

    client = mqtt_client.Client(client_id)
    # client.username_pw_set(username, password)
    client.on_connect = on_disconnect
    client.connect(broker, port)
    return client


def publish(client):
    message_count = 0
    # Clean one to multiplicate
    ses = requests.session()
    while True:
        # response = requests.get(url=system_url)
        req = ses.get(system_url)
        data = req.json()
        # message_data = yaml.safe_dump(data,allow_unicode=True, default_flow_style=False)
        time.sleep(1)
        if sendDocker:
            # while True:
            # message_dict = json.dumps(data)
            res = ",".join("{}={}".format(*i) for i in data.items()).replace('{}', ' ').replace('{', ' ').replace('}',
                                                                                                                  ' ').replace(
                " , ", ' ')
            # message_dict = {data: message_count}
            # message = json.dumps(res)
            result = client.publish(topic1, res)
            # result: [0, 1]
            status = result[0]
            if status == 0:
                print("Send '{message}' to topic '{topic}' ".format(message=res, topic=topic1))
            else:
                print("Failed to send message to topic {topic}".format(topic=topic1))
            message_count += 1
            time.sleep(1)

        elif sendSystem:
            res = ",".join("{}={}".format(*i) for i in data.items()).replace('{}', ' ').replace('{', ' ').replace('}',
                                                                                                                  ' ').replace(
                " , ", ' ')

            result = client.publish(topic2, res)
            # result: [0, 1]
            status = result[0]
            if status == 0:
                print("Send '{message}' to topic '{topic}' ".format(message=res, topic=topic2))
            else:
                print("Failed to send message to topic {topic}".format(topic=topic2))
            message_count += 1
            time.sleep(1)
        else:
            res = ",".join("{}={}".format(*i) for i in data.items()).replace('{}', ' ').replace('{', ' ').replace('}',
                                                                                                                  ' ').replace(
                " , ", ' ')

            result = client.publish(topic, res)
            status = result[0]
            if status == 0:
                print("Send '{message}' to topic '{topic}' ".format(message=res, topic=topic))
            else:
                print("Failed to send message to topic {topic}".format(topic=topic))
            message_count += 1
            time.sleep(1)


def run():
    client = connect_mqtt()
    client.loop_start()
    time.sleep(1)
    if FLAG_CONNECTED:
        publish(client)
    else:
        client.loop_stop()


if __name__ == '__main__':
    run()
