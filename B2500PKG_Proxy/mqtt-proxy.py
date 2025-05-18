import json
import os
import paho.mqtt.client as mqtt

CONFIG_PATH = "/data/options.json"
DEVICE_BROKER = "localhost"
HA_BROKER = "homeassistant"

with open(CONFIG_PATH, "r") as f:
    config = json.load(f)

devices = config.get("devices", [])
clients = []

def create_proxy(port, username, password, index):
    client_id = f"mst_190{index+1}"

    device_client = mqtt.Client(client_id + "_in")
    ha_client = mqtt.Client(client_id + "_out")

    if username:
        device_client.username_pw_set(username, password)
        ha_client.username_pw_set(username, password)

    def on_device_message(client, userdata, msg):
        ha_client.publish(msg.topic, msg.payload)

    def on_ha_message(client, userdata, msg):
        device_client.publish(msg.topic, msg.payload)

    device_client.on_message = on_device_message
    ha_client.on_message = on_ha_message

    device_client.connect(DEVICE_BROKER, port)
    device_client.subscribe("#")
    device_client.loop_start()

    ha_client.connect(HA_BROKER, 1883)
    ha_client.subscribe("#")
    ha_client.loop_start()

    return device_client, ha_client

for i, dev in enumerate(devices):
    dc, pc = create_proxy(dev["port"], dev.get("username", ""), dev.get("password", ""), i)
    clients.append((dc, pc))

try:
    while True:
        pass
except KeyboardInterrupt:
    for dc, pc in clients:
        dc.loop_stop()
        pc.loop_stop()
        dc.disconnect()
        pc.disconnect()
