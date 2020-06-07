def setnorth():   
    for i in range(num_steps):
      for pin in range(0, 4):
        xpin = StepPins[pin]
        if Seq[StepCounter][pin]!=0:
          GPIO.output(xpin, True)
        else:
          GPIO.output(xpin, False)
      StepCounter += StepDir
      if GPIO.input(hallpin) == 0:
        north = 1
        break
      if (StepCounter>=StepCount):
        StepCounter = 0
      if (StepCounter<0):
        StepCounter = StepCount+StepDir
      time.sleep(WaitTime)
    if north != 1:
      StepDir = 1
      num_steps = 4096
      for i in range(num_steps):
        for pin in range(0, 4):
          xpin = StepPins[pin]
          if Seq[StepCounter][pin]!=0:
            GPIO.output(xpin, True)
          else:
            GPIO.output(xpin, False)
        StepCounter += StepDir
        if GPIO.input(hallpin) == 0:
          break
        if (StepCounter>=StepCount):
          StepCounter = 0
        if (StepCounter<0):
          StepCounter = StepCount+StepDir
        time.sleep(WaitTime)

# Move Stepper
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
