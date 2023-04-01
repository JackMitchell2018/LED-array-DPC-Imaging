#!/usr/bin/env python
from samplebase import SampleBase
import time
import numpy as np


class GrayscaleBlock(SampleBase):
    def __init__(self, *args, **kwargs):
        super(GrayscaleBlock, self).__init__(*args, **kwargs)

    def run(self):
        width = 32
        height = 32
        c = 255
        d = np.arange(10,20)
        print(d.shape)
        
    
        def BotLeft():
            for y in range(int(16), 32):
                for x in range(int(16), 32):
                    self.matrix.SetPixel(x, y, 255, 255, 255)
        def TopRight():
            for y in range(0, 16):
                for x in range(0, 16):
                    self.matrix.SetPixel(x, y, 255, 255, 255)
                    
        def TopLeft():
            for xo in range(0, 16):
                for yo in range(16, 32):
                    self.matrix.SetPixel(xo, yo, 255, 255, 255)
                    
        
        def BotRight():
            for x in range(16, 32):
                for y in range(0, 16):
                    self.matrix.SetPixel(x, y, 255, 255, 255)
                    
        def Brightfield():
            for y in range(height):
                for x in range(width):
                    self.matrix.SetPixel(x, y, c, c, c)
                    
        def off():  
            for y in range(height):
                for x in range(width):
                    self.matrix.SetPixel(x, y, 0, 0, 0)
                    
        
                

        while True:
            pattern = int(input('1:Top, 2:Bottom, 3:Left, 4:Right 5:Brightfield'))
            
            if pattern == 1:
                off()
                TopLeft()
                TopRight()
            
            elif pattern == 2:
                off()
                BotRight()
                BotLeft()
                
            elif pattern == 3:
                off()
                TopLeft()
                BotLeft()
                
            elif pattern == 4:
                off()
                TopRight()
                BotRight()
            
            elif pattern == 5:
                off()
                Brightfield()
                        
            

# Main function
if __name__ == "__main__":
    grayscale_block = GrayscaleBlock()
    if (not grayscale_block.process()):
        grayscale_block.print_help()

