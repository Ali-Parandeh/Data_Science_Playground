import argparse
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True, help= 'Path to the image')
args = vars(ap.parse_args())

# load the image, grab its dimensions and show it
image = cv2.imread(args['image'])
(h, w) = image.shape[:2]
cv2.imshow('Original', image)

# images are just numpy arrays. The top-left pixel can be found at (0, 0)
(b, g, r) = image[0, 0]
print("Pixel at (0, 0) - Red: {r}, Green: {g}, Blue: {b}".format(r=r, g= g, b=b))

# lt's change the value of the pixel at (0, 0) and make it red
image[0, 0] = (0, 0 , 255)
(b, g, r) = image[0, 0]
print('Pixel at (0, 0) - Red: {r}, Green: {g}, Blue: {b}'.format(r=r, g=g, b=b))

# compute the center of the image, which is simply the width and height
# divided by two
(cx, cy) = (w // 2, h //2 )

# since we are using the numpy arrays, we can apply slicing and grab large chunks
# of the image -- let's grab the top-left corner
tl = image[0:cy, 0:cx]
cv2.imshow('Top-Left Corner', tl)

# in similar fashion, let's grab the top-right, bottom-right, and bottom-left
# corners and display them
tr = image[0:cy, cx:w]
br = image[cy:h, cx:w]
bl = image[cy:h, 0:cx]
cv2.imshow('Top-Right Corner', tr)
cv2.imshow('Bottom-Right Corner', br)
cv2.imshow('Bottom-Left Corner', bl)

# now let's make the top-left corner of the original image green
image[0:cy, 0:cx] = (0, 255, 0)
# show updated image
cv2.imshow('Updated', image)

# Exercise - What is the approximate value of pixel located at point x=111
# and y = 225

(b1, g1 ,r1) = image[225, 111]
print(f'Pixel at (111, 255) - Red: {r1}, Green: {g1}, Blue: {b1}')

cv2.waitKey(0)