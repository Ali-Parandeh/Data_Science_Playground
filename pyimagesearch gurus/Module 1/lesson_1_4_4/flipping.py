# import the necessary packages
import argparse
import cv2
import imutils

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help = "Path to the image")
args = vars(ap.parse_args())

# load the image and show it
image = cv2.imread(args["image"])
cv2.imshow("Original", image)

# flip the image horizontally
flipped = cv2.flip(image, 1)
cv2.imshow('Flipped Horizontally', flipped)

# flip the image vertically
flipped = cv2.flip(image, 0)
cv2.imshow('Flipped Vertically', flipped)

# flip the image along both axes
flipped = cv2.flip(image, -1)
cv2.imshow('Flipped Horizontally and Vertically', flipped)

# Exercise: Use OpenCV to flip the image horizontally —
# what is the value of the pixel located at x=259, y=235?
flipped = cv2.flip(image, 1)
(b, g, r) = flipped[235, 259]
print(f'The value of pixel at (259, 235) is Red: {r}, Green: {g}, Blue: {b}')

# Use the original image from the previous question
# and flip it horizontally, followed by a 45 degree
# counter-clockwise rotation, and lastly a vertical flip.
# What is (approximately) the pixel value located at x=441, y=189?
flipped = cv2.flip(image, 1)
rotated = imutils.rotate(flipped, 45)
flipped_and_rotated = cv2.flip(rotated, 0)
(b, g, r) = flipped_and_rotated[189, 441]
print(f'The value of pixel at (441, 189) is Red: {r}, Green: {g}, Blue: {b}')
