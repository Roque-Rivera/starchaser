# Import required libraries
import time
import datetime
import RPi.GPIO as GPIO
import sys
from RPi import GPIO
from time import sleep

# Initialize all sensors/motors
# Servo
PIN = 2
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN, GPIO.OUT)
servo = GPIO.PWM(PIN, 50)

# Hall

# Stepper
StepPins = [17,22,23,24]
for pin in StepPins:
  GPIO.setup(pin,GPIO.OUT)
  GPIO.output(pin, False)
## Define advanced sequence
## as shown in manufacturers datasheet
Seq = [[1,0,0,1],
       [1,0,0,0],
       [1,1,0,0],
       [0,1,0,0],
       [0,1,1,0],
       [0,0,1,0],
       [0,0,1,1],
       [0,0,0,1]]
# 
