import json
import paho.mqtt.client as paho
import os
import socket
import ssl
from time import sleep
import random
from random import uniform

connflag = False

def on_connect(client, userdata, flags, rc):
    global connflag
    connflag = True
    print("Connection returned result: " + str(rc) )

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))



mqttc = paho.Client()

mqttc.on_connect = on_connect
mqttc.on_message = on_message

latitude = 12.9716
longitude = 77.5946

awshost = "id-region.amazonaws.com"
awsport = 8883
clientId = "xxxx"
thingName = "xxxx"
caPath = "root-CA.crt"
certPath = "xxxx.cert.pem"
keyPath = "xxxx.private.key"

mqttc.tls_set(caPath, certfile=certPath, keyfile=keyPath, cert_reqs=ssl.CERT_REQUIRED, tls_version=ssl.PROTOCOL_TLSv1_2, ciphers=None)

mqttc.connect(awshost, awsport, keepalive=60)

mqttc.loop_start()

while 1==1:
    sleep(5)
    if connflag == True:
        new_lat = latitude+random.random()/100
        new_lon = longitude+random.random()/100
        
        payload = json.dumps({'latitude':new_lat, 'longitude':new_lon})
        mqttc.publish("iot", payload, qos=0)
        print("msg sent: " + "%s" % payload )
    else:
        print("waiting for connection...")