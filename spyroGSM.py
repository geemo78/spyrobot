import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)

buzzer=16
sprinkler=23
GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzer,GPIO.OUT)
GPIO.setup(sprinkler,GPIO.OUT)

GPIO.output(buzzer,GPIO.HIGH)
GPIO.output(sprinkler,GPIO.HIGH)
    
def alarm():
    
    GPIO.output(buzzer,GPIO.LOW)
    print ("The alarm has been activated")
    sleep(0.3)
    GPIO.output(buzzer,GPIO.HIGH)
     

def rain():

    GPIO.output(sprinkler,GPIO.LOW)
    print ("The sprinkler has been activated")

def alarmrain():
    GPIO.output(sprinkler,GPIO.LOW)
    sleep(5)
    
    GPIO.output(buzzer,GPIO.LOW)
    sleep(3)
    GPIO.output(buzzer,GPIO.HIGH)

def norain():
    GPIO.output(sprinkler,GPIO.HIGH)

if __name__ == "__main__":
    alarm()
    rain()
    sleep(2)
    norain()
