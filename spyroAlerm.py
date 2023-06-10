import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
buzzer=23
sprinkler=16
GPIO.setup(buzzer,GPIO.OUT)
    
def alarm():
    for i in range(200):
        GPIO.output(buzzer,GPIO.HIGH)
        print ("The alarm has been activated")

alarm()
