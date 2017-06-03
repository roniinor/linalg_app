import os
import random
from PIL import Image
from django.conf import settings

def ascPixel(p):
    if (p < 192):
        if (p < 127):
            if (p < 64):
                return "X"
            else:
                return "I"
        else:
            return "-"
    else:
        return "."
        
def strPic():

    strPicture = ""
    #web root path
    img = Image.open(os.path.join(settings.STATIC_ROOT + '/images/munch.png'))
    #local path
    #img = Image.open('static/images/munch.png')
    
    for c in range(img.width):    
        for r in range(img.height):
            strPicture += ascPixel(img.getpixel((r,c))[0])
        strPicture += "</br>"
    
    return strPicture
    
    
def matrixFunction():
    return "some other matrix function - placeholder for now"

def randomNumList(numNumbers, digits):
    nl = []
    for nn in range(numNumbers):
        n = random.randint(1,9)     # most sig dig 1-9 
        # all other digits 0-9
        for i in range(1, digits):
            n = 10 * n + random.randint(0,9)
        nl.append(n)
    return nl

# return a list of n questions, each a string of the form e.g. '23 x 67 = ' 
# each question followed by the answer
def twoDigitMultiplyQAList(n):
    qal = []
    for i in range(n):
        rp = randomNumList(2, 2)
        q = str(rp[0]) + " x " + str(rp[1]) + " = "
        qal.append(q)
        qans = rp[0] * rp[1]
        qal.append(str(qans))
    return qal


if __name__ == '__main__':
    print(strPic())

