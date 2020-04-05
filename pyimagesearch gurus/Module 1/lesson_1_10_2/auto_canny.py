'''
Canny edge detector includes smoothing, the computation of image gradients,
non-maxima suppression, and hysteresis thresholding.
'''

# import the necessary packages
import argparse
import imutils
import cv2

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path to the image")
args = vars(ap.parse_args())

# load the image, convert it to grayscale, and blur it slightly
image = cv2.imread(args['image'])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (3, 3), 0)

"""
NOTE: A weak edge can still be considered an “edge” 
(according to the Canny edge detector) 
if it is connected to a strong edge.
"""

# apply Canny edge detection using a wide threshold,
# tight threshold, and automatically determined threshold
wide = cv2.Canny(blurred, 10, 200)
tight = cv2.Canny(blurred, 255, 250)

# constructing a range of sigma values to test which performs the best
sigma_list = [0.1, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
for sigma in sigma_list:
    auto = imutils.auto_canny(blurred, sigma=sigma)
    cv2.imshow(f'Auto - sigma: {sigma}', auto)

# show the images
cv2.imshow('Original', image)
cv2.imshow('Wide', wide)
cv2.imshow('Tight', tight)
cv2.waitKey(0)

'''
one of the biggest drawbacks of the Canny edge detector is tuning the 
upper and lower thresholds for the hysteresis step. If the threshold was too wide, 
It detect too many edges. And if the threshold was too tight, 
it would not detect many edges at all
'''