# mandelbrot.py
# Lab 9
#
# Name: Marc Sulsenti
# I pledge my honor that I have abided by the Stevens Honor System

# keep this import line...
from cs5png import PNGImage

# start your Lab 9 functions here:
def mult(c,n):
    """Multiplies two integers c , n utilziing a for loop"""
    output = 0
    for i in range(n):
        output +=c
    return output


def update(c,n):
    """runs the operation z=z**2+c n times, returning final z"""
    z=0
    for i in range(n):
        z=z**2
        z+=c
    return z


def inMSet(c,n):
    """takes in c for the update step of the operation z=z**2+c
n, the max number of times to run that step. returns false is abs(z)
is > 2, returns true if abs(z) never gets larger then 2. (For n iterations)"""
    z=0
    for i in range(n):
        z=z**2
        z+=c
        if abs(z) > 2:
            return False
    return True

    
def weWantThisPixel(col,row):
    """Returns true if the wanted pixel is the pixel at col,row. False otherwise."""
    if col%10==0 or row%10==0:
        return True
    else:
        return False

    
def test():
    """function that demonstrates how
one should create and save a PNG image"""
    width = 300
    height = 200
    image = PNGImage(width,height)

    for col in range(width):
        for row in range(height):
            if weWantThisPixel(col,row) == True:
                image.plotPoint(col,row)
    image.saveFile()
    
def scale(pix,pixMax,floatMin,floatMax):
    """scale takes in the
    pix - the current pixel column or row
    floatMin - the min floating point value
    floatMax - the max floating point value
    then returns the floating point value that corresponds
    to pix """
    ratio = float(pix)/pixMax
    spread = floatMax-floatMin
    distFromMin = ratio*spread
    return distFromMin+floatMin

def mset():
    """creates a 300x200 image of the Mandelbrot set"""
    width = 3000
    height= 2000
    image = PNGImage(width,height)

    for col in range(width):
        for row in range(height):
            x = scale(col,width, -2.0,1.0)
            y = scale(row,height,-1.0,1.0)
            c = x + (y*1j)
            if inMSet(c,25):
                image.plotPoint(col,row)
    image.saveFile()
