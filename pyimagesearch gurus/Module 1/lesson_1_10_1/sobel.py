# import the necessary packages
import argparse
import cv2

# construct the argument parser and parse arguments
ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True, help='Path to the image')
args = vars(ap.parse_args())

# load the image, convert it to grayscale and display the original image
image = cv2.imread(args['image'])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('Original', image)

# compute the gradients along the X and Y axis, respectively
# NOTE: Specifying a value of dx=1  and dy=0  indicates that
# we want to compute the gradient across the x direction, similar with gy
gx = cv2.Sobel(gray, ddepth=cv2.CV_64F, dx=1, dy=0)
gy = cv2.Sobel(gray, ddepth=cv2.CV_64F, dx=0, dy=1)

'''
computing the Scharr kernel can be done in the exact same manner, only using the cv2.Scharr
function or supplying an optional parameter value of ksize=-1  for the cv2.Sobel  function
gx = cv2.Scharr(gray, ddepth=cv2.CV_64F, dx=1, dy=0)
gy = cv2.Scharr(gray, ddepth=cv2.CV_64F, dx=0, dy=1)
'''

# the gx and gy images are now of the floating point data type
# so we need to take care to convert them back to an unsigned 8-bit
# integer representation so other opencv functions can utilise them
gx = cv2.convertScaleAbs(gx)
gy = cv2.convertScaleAbs(gy)

# combine the sobel x and y representations into a single image
sobel_combined = cv2.addWeighted(gx, 0.5, gy, 0.5, 0)

# show output images
cv2.imshow('Sobel X', gx)
cv2.imshow('Sobel Y', gy)
cv2.imshow('Sobel Combined', sobel_combined)
cv2.waitKey(0)
