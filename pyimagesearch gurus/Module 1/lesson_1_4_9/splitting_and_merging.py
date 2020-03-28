# import the necessary packages
import numpy as np
import argparse
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

# Load the image and grab each channel: Red, Green, and Blue. It's
# important to note that OpenCV stores an image as NumPy array with
# its channels in reverse order! When we call cv2.split, we are
# actually getting the channels as Blue, Green, Red!
image = cv2.imread(args['image'])
(B, G, R) = cv2.split(image)

# show each channel individually
cv2.imshow('Red', R)
cv2.imshow('Green', G)
cv2.imshow('Blue', B)

# merge the image back together again
merged = cv2.merge([B, G, R])
cv2.imshow('Merged', merged)
cv2.destroyAllWindows()

# visualise each channel in colour
zeros = np.zeros(image.shape[:2], dtype='uint8')
cv2.imshow('Red', cv2.merge([zeros, zeros, R]))
cv2.imshow('Green', cv2.merge([zeros, G, zeros]))
cv2.imshow('Blue', cv2.merge([B, zeros, zeros]))
cv2.waitKey(0)

# Exercise:
# What is the value of the Red channel at x=180, y=94?
print(R[94, 180])

# The value of the Blue channel at x=13, y=78?
print(B[78, 13])

# And the Green channel at x=80, y=5?
print(G[5, 80])
