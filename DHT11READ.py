import Adafruit_DHT


while True:
    humidity, temperature = Adafruit_DHT.read_retry(11, 27)  
    print ("Humidity = {} %; Temperature = {} C".format(humidity, temperature))
