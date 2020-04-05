# import the necessary packages
import argparse
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True, help='Path to the image')
args = vars(ap.parse_args())

'''
Almost always apply edge detection to a single channel, grayscale image.
this ensures that there will be less noise during the edge detection process
'''

# load the image, convert it to grayscale, and blur it slightly
image = cv2.imread(args['image'])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

# show the original and blurred images
cv2.imshow('Original', image)
cv2.imshow('Blurred', blurred)

'''
Pass lower and upper thresholds to the Canny Edge detector
'''

# compute the 'wide', 'mid-range', and 'tight' threshold for the edges
wide = cv2.Canny(blurred, 10, 200)
mid = cv2.Canny(blurred,30, 150)
tight = cv2.Canny(blurred, 240, 250)

# show the edge maps
cv2.imshow('Wide Edge Map', wide)
cv2.imshow('Mid Edge Map', mid)
cv2.imshow('Tight Edge Map', tight)
cv2.waitKey(0)
