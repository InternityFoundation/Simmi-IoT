import Adafruit_DHT
from ISStreamer.Streamer import Streamer
import time
import sys
import RPi.GPIO as GPIO

led = 5
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(led,GPIO.OUT)
st="danger"
pt="All Good "
streamer = Streamer(bucket_name="FireAlarm", bucket_key="WHHMYQPJ9C49", access_key="ist_-PLw5iSTr7Vju5PC7-Xo_FyMCo2f-keG")
while True:
    humidity, temperature= Adafruit_DHT.read_retry(11,4)
    print("humidity ={}% ; temperature = {}C ".format(humidity,temperature))
    if temperature>=21.0:
        streamer.log("FIRE_ALERT",st)
        streamer.log("humidity", humidity)
        streamer.log("Temperature", temperature)
        GPIO.output(led,GPIO.HIGH)
        
        time.sleep(1)
    if temperature<21.0:
        streamer.log("FIRE_ALERT" , pt)
        streamer.log("humidity", humidity)
        streamer.log("Temperature", temperature)
        GPIO.output(led,GPIO.LOW)
        time.sleep(1)
GPIO.cleanup()
