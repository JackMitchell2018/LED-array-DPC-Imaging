#!/usr/bin/env/python

#Import required libaries
import sys
from time import sleep
import RPi.GPIO as GPIO

#Setup change to GPIO number
#For physicl pin numbering use GPIO.BOARD
GPIO.setmode(GPIO.BCM)

#Define pins that the  motor is connected to
#For M0
StepPins = [17,18,27,22]

for pin in StepPins:
    print("Setup Pins")
    GPIO.setup(pin, GPIO.OUT) #Set GPIO pins to output
    GPIO.output(pin, 0) #switches pin to 0V
    
#Define a pin sequence (from Gemma)
seq = [[1,0,0,0],
       [1,1,0,0],
       [0,1,0,0],
       [0,1,1,0],
       [0,0,1,0],
       [0,0,1,1],
       [0,0,0,1],
       [1,0,0,1]]

#Define a step counter size of the sequence
StepCount = len(seq) #8

#define motor direction.
#(1, 2, clockwise) (-1, -2, anticlockwise) 
StepDir = -1

#Define the waitime (controls speed of the motor)
if len(sys.argv)>1:
    WaitTime = int(sys.argv[1])/1000
else:
    WaitTime = 0.005

#Initialise step count
StepCounter =  0

#Loop

while True:
    print(StepCounter)
    print(seq[StepCounter])
   ################################### 
    for pin in range(0,4):
        xpin = StepPins[pin]
        if seq[StepCounter][pin]!=0:
            print("Enable GPIO %i" %(xpin))
            GPIO.output(xpin,True)
        else:
              GPIO.output(xpin,False)
              
        StepCounter += StepDir
              
        if (StepCounter>=StepCount):
              StepCounter=0
        if (StepCounter<0):
              StepCounter = StepCount + StepDir
              
        sleep(WaitTime)
    
    
    