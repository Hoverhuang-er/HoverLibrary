""" 
dht22.py 

Temperature/Humidity monitor using Raspberry Pi and DHT22. 

""" 

import sys 
import RPi.GPIO as GPIO 
from time import sleep 
import Adafruit_DHT 
import urllib2 

myAPI = "<your API code here>" 

def getSensorData(): 
   RH, T = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, 23) #23 refers to GPIO 23, or pin 16 on the RPi
   return (str(RH), str(T)) 

def main(): 
   print 'starting...' 
   baseURL = 'https://api.thingspeak.com/update?api_key=%s' % myAPI 

   while True: 
       try: 
           RH, T = getSensorData() 
           f = urllib2.urlopen(baseURL + 
                               "&field1=%s&field2=%s" % (RH, T)) 
           print f.read() 
           f.close() 
           sleep(300) #uploads DHT22 sensor values every 5 minutes 
       except: 
           print 'exiting.' 
           break 

# call main 
if __name__ == '__main__': 
   main() 
