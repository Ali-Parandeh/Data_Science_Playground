# import the necessary packages
import argparse
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

# load the image and convert it to grayscale
image = cv2.imread(args['image'])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# construct a rectangular kernel and apply a blackhat operation which
# enables us to find dark regions on a light background
# applying a rectangular element that is almost 3x wider than it is tall.
# NOTE: Because a license plate is roughly 3x wider than it is tall!
rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (13, 5))
black_hat = cv2.morphologyEx(gray, cv2.MORPH_BLACKHAT, rect_kernel)

# similarly a tophat (also called a whitehat) operation which
# enables us to find light regions in a dark background
top_hat = cv2.morphologyEx(gray, cv2.MORPH_TOPHAT, rect_kernel)

# show the output images
cv2.imshow('Original', image)
cv2.imshow('Blackhat', black_hat)
cv2.imshow('Tophat', top_hat)
cv2.waitKey(0)
