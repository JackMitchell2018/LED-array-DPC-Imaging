from samplebase import SampleBase
import time
import numpy as np


class GrayscaleBlock(SampleBase):
    def __init__(self, *args, **kwargs):
        super(GrayscaleBlock, self).__init__(*args, **kwargs)

    def run(self):
        width = 32
        height = 32

        #Defining x and y indicies
        x = np.arange(0, 32, 1)
        xblock = np.zeros((16, 2))
        yblock = np.zeros((16, 2))
        #Looping through and assigning indexes to 16x2 arrays making blocks of 4 when combined
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

        ###################
        yblock_index = 0
        yblock_index2 = 1

        xblock_index = 0
        xblock_index2 = 1
        ###################
        
        on_off = input('Would you like to begin the illumination sequence? y/n')
        if on_off == 'y':
            print('On')
        while True:
            print([xblock_index]+[xblock_index2])
            self.matrix.SetPixel(xblock_index, yblock_index, 255, 255, 255)
            self.matrix.SetPixel(xblock_index, yblock_index2, 255, 255, 255)
            self.matrix.SetPixel(xblock_index2, yblock_index, 255, 255, 255)
            self.matrix.SetPixel(xblock_index2, yblock_index2, 255, 255, 255)
            
            step = input('Step forward or backward? f/b')
            
            self.matrix.SetPixel(xblock_index, yblock_index, 0, 0, 0)
            self.matrix.SetPixel(xblock_index, yblock_index2, 0, 0, 0)
            self.matrix.SetPixel(xblock_index2, yblock_index, 0, 0, 0)
            self.matrix.SetPixel(xblock_index2, yblock_index2, 0, 0, 0)
            
            if step == 'f':
                xblock_index = xblock_index + 2
                xblock_index2 = xblock_index2 + 2
                
            elif step == 'b':
                xblock_index = xblock_index - 2
                xblock_index2 = xblock_index2 - 2
                
            elif step == 'skip':
                xblock_index = int(input('To Where?:x1'))
                xblock_index2 = xblock_index + 1
                yblock_index = int(input('To where?:y1'))
                yblock_index2 = yblock_index + 1
                        
            
            if xblock_index > 31:
                yblock_index = yblock_index + 2
                yblock_index2 = yblock_index2 + 2
                xblock_index = xblock_index - 32
                xblock_index2 = xblock_index2 -32
                
            if xblock_index < 0:
                yblock_index = yblock_index - 2
                yblock_index2 = yblock_index2 - 2
                xblock_index = xblock_index + 32
                xblock_index2 = xblock_index2 + 32
            
            print([xblock_index] + [yblock_index])
        else:
            print('Ok, Exiting')
            sys.exit()
    
# Main function
if __name__ == "__main__":
    grayscale_block = GrayscaleBlock()
    if (not grayscale_block.process()):
        grayscale_block.print_help()