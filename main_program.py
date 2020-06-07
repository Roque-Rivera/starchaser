# Starchaser. A newbie python attempt to make a raspberry pi based star pointer

# Import needed libraries
import sys # to read params from cli
import RPi.GPIO as GPIO # GPIO on RPI
import time # Needed to know how to deal with time
import datetime

# Functions
# Hall sensor
def detectedNorth(hallpin):
  if GPIO.input(hallpin) == 0:
    print("North Detected")

# Initialize all sensors/motors
GPIO.setmode(GPIO.BCM)

# Hall Sensor
hallpin = 25
GPIO.setup(hallpin , GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(hallpin, GPIO.FALLING, callback=detectedNorth, bouncetime=2000)

## Servo for altitude
#PIN = 2
#GPIO.setmode(GPIO.BCM)
#GPIO.setup(PIN, GPIO.OUT)
#servo = GPIO.PWM(PIN, 50)

# Stepper for azimut
StepPins = [17,22,23,24]
for pin in StepPins:
  GPIO.setup(pin,GPIO.OUT)

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
StepCount = len(Seq)
StepDir = 1
StepCounter = 0
WaitTime = 1/float(1000)

# Search North
def setnorth():
    global StepCounter
    for i in range(2048):
      for pin in range(0, 4):
        xpin = StepPins[pin]
        if Seq[StepCounter][pin]!=0:
          GPIO.output(xpin, True)
        else:
          GPIO.output(xpin, False)
      StepCounter = StepCounter - 1
      if GPIO.input(hallpin) == 0:
        break
      if (StepCounter>=StepCount):
        StepCounter = 0
      if (StepCounter<0):
        StepCounter = StepCount - 1
      time.sleep(WaitTime)
    if GPIO.input(hallpin) != 0:
      for i in range(4096):
        for pin in range(0, 4):
          xpin = StepPins[pin]
          if Seq[StepCounter][pin]!=0:
            GPIO.output(xpin, True)
          else:
            GPIO.output(xpin, False)
        StepCounter = StepCounter + 1
        if GPIO.input(hallpin) == 0:
          break
        if (StepCounter>=StepCount):
          StepCounter = 0
        if (StepCounter<0):
          StepCounter = StepCount + 1
        time.sleep(WaitTime)

def stepper(num_steps, StepDir):
    global StepCounter
    for i in range(num_steps):
      for pin in range(0, 4):
        xpin = StepPins[pin]
        if Seq[StepCounter][pin]!=0:
          GPIO.output(xpin, True)
        else:
          GPIO.output(xpin, False)
      StepCounter += StepDir
      if (StepCounter>=StepCount):
        StepCounter = 0
      if (StepCounter<0):
        StepCounter = StepCount+StepDir
      time.sleep(WaitTime)


def main():
  # Wrap main content in a try block so we can
  # catch the user pressing CTRL-C and run the
  # GPIO cleanup function. This will also prevent
  # the user seeing lots of unnecessary error
  # messages.

  # Get initial reading
  # detectedNorth(hallpin)

  try:
    # Loop until users quits with CTRL-C
    while True :
      if GPIO.input(hallpin) != 0:
        setnorth()
      time.sleep(15)

  except KeyboardInterrupt:
    # Reset GPIO settings
    GPIO.cleanup()

if __name__=="__main__":
   main()