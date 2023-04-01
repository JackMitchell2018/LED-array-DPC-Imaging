#!/usr/bin/env python
from samplebase import SampleBase
import time
import numpy as np
import sys


class GrayscaleBlock(SampleBase):
    def __init__(self, *args, **kwargs):
        super(GrayscaleBlock, self).__init__(*args, **kwargs)

    def run(self):
        width = 32
        height = 32
                
        xcomp = np.zeros([32,32])
        ycomp = np.zeros([32,32])
        act_rad = np.zeros([32,32])
        
        for x in range(32):
            for y in range(32):
                xcomp[x,y] = (x-15)
                ycomp[x,y] = (y-15)
                if xcomp[x,y]>0:
                    xcomp[x,y] = xcomp[x,y]-1
                if ycomp[x,y]>0:
                    ycomp[x,y] = ycomp[x,y]-1
                
                xcomp[x,y] = (np.absolute(xcomp[x,y]) * 4e-3) + 4e-3
                ycomp[x,y] = (np.absolute(ycomp[x,y]) * 4e-3) + 4e-3
                
                act_rad[x,y] = np.sqrt((xcomp[x,y])**2 + (ycomp[x,y])**2)
        
        def off():  
                for y in range(32):
                    for x in range(32):
                        self.matrix.SetPixel(x, y, 0, 0, 0)
        def on():
            for y in range(32):
                for x in range(32):
                    self.matrix.SetPixel(x, y, 255, 255, 255)             
        def annulus(r):
            #This is just a place holder, calculate the outer radius later
            outer= 60e-3
            rad = r * 1e-3
            for x_ann in range(32):
                for y_ann in range(32):
                    if rad < act_rad[x_ann,y_ann] < outer:
                        self.matrix.SetPixel(x_ann, y_ann, 255, 255, 255)
            time.sleep(5)
             
        def top():
            for x_ann in range(0, 32):
                for y_ann in range(16, 32):
                    self.matrix.SetPixel(x_ann, y_ann, 0, 0, 0)
        def bot():
            for x_ann in range(0, 32):
                for y_ann in range(0, 16):
                    self.matrix.SetPixel(x_ann, y_ann, 0, 0, 0)
        def left():
            for x_ann in range(16, 32):
                for y_ann in range(0, 32):
                    self.matrix.SetPixel(x_ann, y_ann, 0, 0, 0)
        def right():
            for x_ann in range(0, 16):
                for y_ann in range(0, 32):
                    self.matrix.SetPixel(x_ann, y_ann, 0, 0, 0)
                                        
        while True:
            ans = input('Would you like to begin the illumination? [y/n]')
            rad = int(input('Please input inner radius in mm'))
            if ans == 'y':
                while True:
                    try:
                        
                        pattern = int(input('Input your illumination pattern: /nTop:1 , Bottom:2, Left:3, Right:4, Brightfield:5, Reset radius:6'))
                        
                        if pattern == 1:
                            off()
                            annulus(rad)
                            top()
                        elif pattern == 2:
                            off()
                            annulus(rad)
                            bot()
                        elif pattern == 3:
                            off()
                            annulus(rad)
                            left()
                        elif pattern == 4:
                            off()
                            annulus(rad)
                            right()
                        elif pattern == 5:
                            off()
                            annulus(rad)
                        elif pattern == 6:
                            off()
                            break
                        
                    
                
                    except KeyboardInterrupt:
                        print('Exiting')
                        sys.exit()         

# Main function
if __name__ == "__main__":
    grayscale_block = GrayscaleBlock()
    if (not grayscale_block.process()):
        grayscale_block.print_help()