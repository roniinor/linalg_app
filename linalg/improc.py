from skimage import io, color, data
img = io.imread('static/images/checks-gs.png')
dimensions = color.guess_spatial_dimensions(img)
print (dimensions)
print (img.shape)
img_grayscale = color.rgb2gray(img)
io.imsave('static/images/checks-gs.png',img_grayscale)
io.imshow(img)


