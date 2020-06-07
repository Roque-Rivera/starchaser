import sys
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.OUT)
p = GPIO.PWM(2, 50)
#p.start(7.5)
#time.sleep(1)
# Read angle from command line
if len(sys.argv)>1:
  angle = float(sys.argv[1])
else:
  angle = 90

duty = angle / 18 + 2
p.start(duty)
#p.ChangeDutyCycle(duty)
time.sleep(3)
p.stop()