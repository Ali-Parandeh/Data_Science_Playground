import numpy as np
import argparse
import imutils
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True, help='Path to the image')
args = vars(ap.parse_args())

# load the image and show it
image = cv2.imread(args['image'])
cv2.imshow('Original', image)

# grab the dimensions of the image and calculate the centre of the image
(h, w) = image.shape[:2]
(cx, cy) = (w//2, h//2)

# rotate the image by 45 degrees
# (w,h) tells openCV to draw a canvas that size
M = cv2.getRotationMatrix2D((cx, cy), 45, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow('Rotated by 45 degrees', rotated)

# rotate our image by -90 degrees
M = cv2.getRotationMatrix2D((cx, cy), -90, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow('Rotated by -90 degrees', rotated)

# rotate our image around arbitrary point rather than the centre
M = cv2.getRotationMatrix2D((cx - 50, cy - 50), 45, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow('Rotated by offset and 45 degrees', rotated)

# finally let's use helper function in imutils to rotate the image by
# 180 degrees (flipping it upside down)
rotated = imutils.rotate(image, 180)
cv2.imshow('Rotated by 180 degrees', rotated)

# exercise: let's rotate the image by 30 degrees clockwise
# What is the value of pixel at x=335, and y = 254
rotated = imutils.rotate(image, -30)
(b, g, r) = rotated[254, 335]
print(f'The pixel at (335, 254) is Red: {r}, Green: {g}, Blue: {b}')

# exercise: let's rotate the image by 110 degrees counter-clockwise
# What is the value of pixel at x=312, and y = 136
rotated = imutils.rotate(image, 110)
(b, g, r) = rotated[136, 312]
print(f'The pixel at (312, 136) is Red: {r}, Green: {g}, Blue: {b}')

# Change the call to cv2.getRotationMatrix2D to rotate
# the image 88 degrees counter-clockwise about coordinate (50, 50).
# What is the value of the pixel located at point (10, 10)?
M = cv2.getRotationMatrix2D((50, 50), 88, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
(b, g, r) = rotated[10, 10]
print(f'The pixel at (10, 10) is Red: {r}, Green: {g}, Blue: {b}')
print(f'The version of current OpenCV installation is: {cv2.__version__}')