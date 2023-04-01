import numpy as np
import sys
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
        #matrix.pixel(count, y, 1)
        step = input('Step forward or backward? f/b')
        
        #matrix.pixel(count, y, 0)
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
            
            
            
#######################################################################################################

x = np.arange(0, 32, 1)
#print(x)
xblock = np.zeros((16, 2))
yblock = np.zeros((16, 2))
#print(np.shape(xblock))
f = 0
for i in range(16):
    for k in range(2):
        xblock[i, k] = x[f]
        f = f + 1
g = 0
for i in range(16):
    for k in range(2):
        yblock[i, k] = x[g]
        g = g + 1
        
#print(xblock)
#print(yblock)

yblock_index = 0
yblock_index2 = 1

xblock_index = 0
xblock_index2 = 1

on_off = input('Would you like to begin the illumination sequence? y/n')
if on_off == 'y':
    print('On')
while True:
    
    #matrix.pixel(xblock_index, yblock_index)
    #matrix.pixel(xblock_index, yblock_index2)
    #matrix.pixel(xblock_index2, yblock_index)
    #matrix.pixel(xblock_index2, yblock_index)
    
    step = input('Step forward or backward? f/b')
    
    if step == 'f':
        xblock_index = xblock_index + 2
        xblock_index2 = xblock_index + 2
        
    elif step == 'b':
        xblock_index = xblock_index - 2
        xblock_index2 = xblock_index - 2
    
   
    
    if xblock_index > 31:
        yblock_index = yblock_index + 2
        yblock_index2 = yblock_index2 + 2
        xblock_index = xblock_index - 32
        xblock_index2 = xblock_index -32
        
    if xblock_index < 0:
        yblock_index = yblock_index - 2
        yblock_index2 = yblock_index2 - 2
        xblock_index = xblock_index + 32
        xblock_index2 = xblock_index + 32
    
    print([xblock_index] + [yblock_index])
else:
    print('Ok, Exiting')
    sys.exit()