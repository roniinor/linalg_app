import os
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

if __name__ == '__main__':
    print(strPic())

