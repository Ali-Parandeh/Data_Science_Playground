# import the necesary packages
import numpy as np
import argparse
import cv2
import imutils

# construct the argument parser and parse arguments
ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True, help='Path to the Image')
args = vars(ap.parse_args())

"""
NOTE: For better accuracy you’ll normally want to utilize a binary image rather than a grayscale image. 
"""

# load the image and convert it to grayscale
image = cv2.imread(args['image'])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# show the original image
cv2.imshow('Original', image)


"""
NOTE: he cv2.findContours function is destructive to the input image 
(meaning that it manipulates it) so if you intend on using your input image again, 
be sure to clone it using the copy()  method prior to passing it into cv2.findContours.

NOTE: cv2.findContours to return a list of all contours in the image by passing 
in the cv2.RETR_LIST flag. This flag will ensure that all contours are returned. 
Other methods exist, such as returning only the external most contours.

NOTE: pass in the cv2.CHAIN_APPROX_SIMPLE  flag. 
If this flag was not specified and instead cv2.CHAIN_APPROX_NONE flag was used, 
cv2 would have been storing every single (x, y)-coordinate along the contour. 
In general, this not advisable. It’s substantially slower and takes up 
significantly more memory. By compressing the horizontal, vertical, 
and diagonal segments into only end-points, cv2 is able to 
reduce memory consumption significantly without any substantial loss in contour accuracy.

cv2.findContours  function returns a tuple of values.
NOTE: The problem with the returning tuple is that it is 
in a different format for OpenCV 2.4, OpenCV 3, OpenCV 3.4, 
OpenCV 4.0.0-pre, OpenCV 4.0.0-alpha, and OpenCV 4.0.0 (official). 
The latest version of imutils package accommodates for the different return signatures


The first argument passed in the cv2.drawContours function is the image to have the contours drawn on. 
The second parameter is the list of contours found using the cv2.findContours function.
The third parameter is the index of the contour inside the cnts list that is requested to be drawn. 
To only draw the first contour, supply a value of 0. 
To only draw the second contour supply a value of 1. 
Passing in a value of -1 for this argument instructs the cv2.drawContours  
function to draw all contours in the cnts list. 
Try to always supply a value of -1 and just supply the single contour manually. 
Doing this is slightly more Pythonic and easier to read.

the last two arguments to the cv2.drawContours function is the color of the contour 
(in this case green), and the thickness of the contour line (2 pixels)
The cnts  variable is simply a Python list, len() can be on it to 
get the number of contour entries in the list.
"""

# find all the contours in the image and draw all contours on the image
cnts = cv2.findContours(gray.copy(), mode=cv2.RETR_LIST, method=cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
clone = image.copy()
cv2.drawContours(clone, cnts, -1, color = (0, 255, 0), thickness=2)
print(f'Found {len(cnts)} contours')

# show the output image
cv2.imshow('All Contours', clone)

# re-clone the image and close all open windows
clone = image.copy()
cv2.destroyAllWindows()


"""
NOTE: simply re-cloning the input image so that it is not destroying the original when being drawn on. 
To access each individual contour, loop over each of the contours.

NOTE: specifying the contour index value other than -1 inside 
the cv2.drawContours function is counter-productive.
Consider drawing the first two contours and nothing else. 
Either manually make two calls to cv2.findContours or 
use a for loop and supply the contour index value i?
Simply put, that’s not very Pythonic when all needed is to supply Python array slices
to draw only a single contour, get in the habit of always supplying a value of -1 
for contour index and then wrapping a single contour c as a list.
"""

# loop over the contours individually and draw each of them
for (i, c) in enumerate(cnts):
    print(f'Drawing contour #{i+1}')
    cv2.drawContours(clone, [c], -1, (0, 255, 0), 2)
    cv2.imshow('Single Contour', clone)

# re-clone the image and close all open windows
clone = image.copy()
cv2.destroyAllWindows()

"""
NOTE: Supplying a value of cv2.RETR_EXTERNAL for the contour detection mode instructs OpenCV 
to return only the external most contours of each shape in the image, 
meaning that if one shape is enclosed in another, then the contour is ignored.
"""

# find all the contours in the image and draw all contours on the image
cnts = cv2.findContours(gray.copy(), mode=cv2.RETR_EXTERNAL, method=cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
cv2.drawContours(clone, cnts, -1, color = (0, 255, 0), thickness=2)
print(f'Found {len(cnts)} contours')

# show the output image
cv2.imshow('All Contours', clone)

# re-clone the image and close all open windows
clone = image.copy()
cv2.destroyAllWindows()


"""
Using both contours and masks together
Create an empty NumPy array with the same dimensions of our original image. 
This empty NumPy array will serve as the mask  for the current shape to examine.
draw the contour on the mask.
White is represented by (255, 255, 255) but if working with a RGB image - with a mask that 
has only a single (grayscale) channel — thus only need to supply a value of 255 to get white.
Use bitwise_AND between the input image and the mask to hide all other shapes but the one interested in.

A bitwise AND is true only if both input pixels are greater than zero. 
By supplying a mask  to the cv2.bitwise_and function, OpenCV only investigates 
regions of the image where the corresponding mask is non-zero.
"""

# loop over the contours individually
for c in cnts:
    # construct a mask by drawing only the current contour
    mask = np.zeros(gray.shape, dtype="uint8")
    # thickness of -1 means solid shape, but thickness of 10 means solid border of 10px
    cv2.drawContours(mask, [c], -1, 255, thickness=-1)

    # show the images
    cv2.imshow("Image", image)
    cv2.imshow("Mask", mask)
    cv2.imshow("Image + Mask", cv2.bitwise_and(image, image, mask=mask))
    cv2.waitKey(0)