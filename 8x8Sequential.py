import numpy as np
import sys
import board
from adafruit_ht16k33.matrix import Matrix8x8

i2c = board.I2C()
matrix = Matrix8x8(i2c)

#put the 8x8 matrix code here

def on(x, y):
    matrix.pixel(x, y, 1)
    
while True:
    y=0
    count = 0
    onoff = input('Would you like to start the illumination sequence:y/n')
    if onoff == 'y':
        print('on')
    else:
        print('Ok, exitting')
        sys.exit()
    
    
    while True:
        matrix.pixel(count, y, 1)
        step = input('Step forward or backward? f/b')
        
        matrix.pixel(count, y, 0)
        if step == 'f':
            count = count + 1
        elif step == 'b':
            count = count - 1
        else:
            print('Please input a valid step direction')
        
        
        if count >= 8:
            y = y + 1
            count = count - 8
            print([count] + [y])
        elif count < 0:
            y = y - 1
            count = count + 8
            print([count] + [y])
        else:
            print([count] + [y])         
            
            
            
