import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
buzzer=17
sprinkler=16 
GPIO.setup(buzzer,GPIO.OUT)
    
def alarm():
    for i in range(10000):
        GPIO.output(buzzer,GPIO.HIGH)
        print (f"{i}The alarm has been activated")

    GPIO.output(buzzer,GPIO.LOW)     

alarm()
