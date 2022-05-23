### Taken from https://pypi.python.org/pypi/paho-mqtt
### Requires Paho-MQTT package, install by:
### pip install paho-mqtt

import paho.mqtt.client as paho
from paho import mqtt

MQTT_URL   = "efe545b723c6413a94f9b2910b00c39a.s1.eu.hivemq.cloud"
MQTT_TOPIC = "vominhtri/pi/#"

def on_connect(client, userdata, flags, rc, properties=None):
    print("Connected with result code " + str(rc))
    print("Subscribed to " + MQTT_TOPIC)
    client.subscribe(MQTT_TOPIC)

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))
    print()

client = paho.Client(client_id="", userdata=None, protocol=paho.MQTTv5)

# enable TLS
client.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS)
# set username and password
client.username_pw_set("vominhtri", "Vominhtrithcsdhtp1")

client.on_connect = on_connect
client.on_message = on_message

print("connecting to " + MQTT_URL)
client.connect(MQTT_URL, 8883, 60)
client.loop_forever()