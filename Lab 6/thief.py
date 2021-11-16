import paho.mqtt.client as mqtt
import uuid
import adafruit_apds9960.apds9960
import busio
import board
import time
import random

#Every client needs a random ID
client = mqtt.Client(str(uuid.uuid1()))

#configure network encryption etc
client.tls_set()
client.username_pw_set('idd', 'device@theFarm')

client.connect( 
    'farlab.infosci.cornell.edu',
    port = 8883)

i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_apds9960.apds9960.APDS9960(i2c)

sensor.enable_proximity = True
sensor.enable_color = True
threshold = 800

topic = "IDD/detect"  
reset = 1
initial_delay = True
while True:
    if initial_delay:
        time.sleep(3)
        initial_delay = False
    r, g, b, a = sensor.color_data
    if reset == 1 and a < threshold:
        reset = 0
        client.publish(topic, "YoyoStolen!" + str(random.uniform(0, 1)))

    time.sleep(0.1)