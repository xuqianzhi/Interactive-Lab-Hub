import paho.mqtt.client as mqtt
import uuid
import adafruit_apds9960.apds9960
import busio

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

sensor.enable_color = True
r, g, b, a = sensor.color_data

topic = "IDD/detect"  
reset = 1
while True:
    print(r, g, b, a)
    # if proximity == 0:
    #     reset = 1
    # elif reset == 1 and proximity != 0:
    #     reset = 0
    #     client.publish(topic, val)