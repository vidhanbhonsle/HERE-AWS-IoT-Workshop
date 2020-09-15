from flask import Flask,render_template
from flask_mqtt import Mqtt
import ssl
import urllib.request as request

app  = Flask(__name__)

app.config['MQTT_BROKER_URL'] = 'id-region.amazonaws.com'
app.config['MQTT_BROKER_PORT'] = 8883
app.config['MQTT_CLIENT_ID'] = "xxxx"
app.config['MQTT_KEEPALIVE'] = 60
app.config['MQTT_TLS_ENABLED'] = True
app.config['MQTT_TLS_CA_CERTS'] = "root-CA.crt"
app.config['MQTT_TLS_CERTFILE'] = "xxxx.cert.pem"
app.config['MQTT_TLS_KEYFILE'] = "xxxx.private.key"
app.config['MQTT_TLS_CIPHERS'] = None
app.config['MQTT_TLS_CERT_REQS'] = ssl.CERT_REQUIRED
app.config['MQTT_TLS_VERSION'] = ssl.PROTOCOL_TLSv1_2

mqtt = Mqtt(app)

lat = 0
lng = 0

@mqtt.on_connect()
def handle_connect(client, userdata, flags, rc):
    print ('connected and waiting for msg')
    mqtt.subscribe('iot')

@mqtt.on_message()
def handle_mqtt_message(client, userdata, msg):
    global lat, lng
    data = eval(msg.payload.decode())
    lat = data['latitude']
    lng = data['longitude']

@app.route('/')
def index():
    return render_template('home.html')
@app.route('/getlatlng')
def getlatlng_page():
    global lat, lng
    print("called ajax : " , str(lat)+','+str(lng))
    return str(lat)+','+str(lng)

if __name__ == '__main__':
    app.run( use_reloader=False, debug=True)