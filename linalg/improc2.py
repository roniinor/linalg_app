from skimage import data, novice
img = novice.open('static/images/munch.png')
print("W, H : ", img.width, img.height)
i = 0
for px in img.xy_array:
    print(i, px)
    i = i + 1

img.show()


