import RPi.GPIO as GPIO
import time
from time import sleep

GPIO.setwarnings(False)
debug_messages = 1
if debug_messages : print("Debug Messages are 'ON'")
else : print("Debug Messages are 'OFF'")
hardware_test_message = 1
if hardware_test_message : print("Hardware test Message are 'ON'")
else : print("Hardware test Messages are 'OFF'")
GPIO.setmode(GPIO.BOARD)

redRGBPin = 11
greenRGBPin = 13
blueRGBPin = 15
GPIO.setup(redRGBPin,GPIO.OUT)
GPIO.setup(greenRGBPin,GPIO.OUT)
GPIO.setup(blueRGBPin,GPIO.OUT)

Freq = 1000

REDRGB = GPIO.PWM(redRGBPin, Freq)
GREENRGB = GPIO.PWM(greenRGBPin, Freq)
BLUERGB = GPIO.PWM(blueRGBPin, Freq)

REDRGB.start(1)
GREENRGB.start(1)
BLUERGB.start(1)

def rgbCheck(rgb):
    if hardware_test_messages : print("rgb =",rgb)
    rgb = rgb.upper()
    my_color_dic = {"RED":"FF:00:00","GREEN":"00:FF:00","BLUE":"00:00:FF"}
    for color,value in my_color_dic:
        print(color)
        if color == rgb:
            print(rgb)
    return rgb

def rgbWrite(r,g,b):
    REDRGB.ChangeDutyCycle(r)
    GREENRGB.ChangeDutyCycle(g)
    BLUERGB.ChangeDutyCycle(b)