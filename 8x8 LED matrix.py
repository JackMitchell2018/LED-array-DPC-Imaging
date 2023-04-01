import board
from adafruit_ht16k33.matrix import Matrix8x8

i2c = board.I2C()
matrix = Matrix8x8(i2c)

def on(x, y):
    matrix.pixel(x, y, 1)
    
def off(x, y):
    matrix.pixel(x, y, 0)
    
print(matrix.columns/2)
while True:
    try:
        Illum_pattern = int(input('Input your illumination pattern: /nTop:1 , Bottom:2, Left:3, Right:4, Brightfield:5'))   
        if Illum_pattern == 1: #top
            for xpixel in range(matrix.rows):
                for ypixel in range(matrix.columns):
                    if ypixel <4:
                        on(xpixel, ypixel)
                    else:
                        off(xpixel, ypixel)
                       
        elif Illum_pattern == 2: #bottom
             for xpixel in range(matrix.rows):
                for ypixel in range(matrix.columns):
                    if ypixel >=4:
                        on(xpixel, ypixel)
                    else:
                        off(xpixel, ypixel)
                       
        elif Illum_pattern == 3: #left
             for xpixel in range(matrix.rows):
                for ypixel in range(matrix.columns):
                    if xpixel <4:
                        on(xpixel, ypixel)
                    else:
                        off(xpixel, ypixel)
                        
                       
        elif Illum_pattern == 4: #right
             for xpixel in range(matrix.rows):
                for ypixel in range(matrix.columns):
                    if xpixel >=4:
                        on(xpixel, ypixel)
                    else:
                        off(xpixel, ypixel)

        elif Illum_pattern == 5: #Brightfield
            for xpixel in range(matrix.rows):
                for ypixel in range(matrix.columns):
                    on(xpixel, ypixel)

    except KeyboardInterrupt:
        for xpixel in range(matrix.rows):
            for ypixel in range(matrix.columns):
                off(xpixel, ypixel)
        print('User Interrupt')
        break
            
    except ValueError:
        print('Please input an integer value corresponding with one of the 5 illumination patterns')