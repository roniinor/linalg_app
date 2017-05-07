import os
from skimage import io, color
from django.conf import settings

def ascPixel(p):
    if (p < 0.5):
        return "-"
    else:
        return "X"
        
def strPic():

    strPicture = ""
    img = io.imread(os.path.join(settings.STATIC_ROOT + '/images/munch.png'))
    imgg = color.rgb2grey(img)

    for r in imgg:
        for p in r:
            strPicture += ascPixel(p)
        strPicture += "</br>"
    return strPicture

if __name__ == '__main__':
    print(strPic())

