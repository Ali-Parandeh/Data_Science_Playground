# import the necessary packages
import numpy as np
import argparse
import cv2
import imutils

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

# load the image and convert it to grayscale
image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# find find external contours in the image
cnts = cv2.findContours(gray.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
clone = image.copy()

"""CALCULATING CENTROID & CENTRE OF MASS
The “centroid” or “center of mass” is the center (x, y)-coordinate 
of an object in an image. This (x, y)-coordinate is actually calculated 
based on the image moments, which are based on the weighted average of 
the (x, y)-coordinates/pixel intensity along the contour.
"""

# loop over the contours
for c in cnts:
    # compute the moments of the contour which can be used to compute the
    # centrold or 'centre of mass' of the region
    M = cv2.moments(c)
    cx = int(M['m10'] / M['m00'])
    cy = int(M['m01'] / M['m00'])

    # draw the centre of the contour on the image
    cv2.circle(clone, (cx, cy), 10, (0, 255, 0), -1)

# show the output image
cv2.imshow('Centroids', clone)
clone = image.copy()

"""CALCULATING AREA & PERIMETER OF CONTOURS
NOTE: Just like the contour area, we can use the perimeter as 
a method to quantify the shape of an object. However, 
the perimeter has a more important role to play in contour approximations

NOTE: area is defined as the number of white pixels that appear inside the contour
"""

# loop over the contours again
for (i, c) in enumerate(cnts):
    # Compute the area and the perimeter of the contour
    area = cv2.contourArea(c)
    perimeter = cv2.arcLength(c, True)
    print(f'Contour #{i+1} -- area: :{area} -- perimeter: {perimeter}')
    
    # draw the contour on the image
    cv2.drawContours(clone, [c], -1, (0, 255, 0), 2)
    
    # compute the centre of the contour and draw the contour number
    M = cv2.moments(c)
    cx = int(M['m10'] / M['m00'])
    cy = int(M['m01'] / M['m00'])
    cv2.putText(clone, f'#{i+1}', (cx -20, cy), cv2.FONT_HERSHEY_SIMPLEX, 
                1.25, (255, 255, 255), 4)
    
# show the output image
cv2.imshow('Contours', clone)

"""BOUNDING BOX
A bounding box is exactly what it sounds like — 
an upright rectangle that “bounds” and “contains” the 
entire contoured region of the image. However, 
it does not consider the rotation of the shape
"""

# clone the image
clone = image.copy()

# loop over the contours
for c in cnts:
    # fit the bounding box to the contour
    (x, y, w, h) = cv2.boundingRect(c)
    cv2.rectangle(clone, (x, y), (x + w, y + h), (0, 255, 0), 2)

# show the output image
cv2.imshow('Bounding boxes', clone)

clone = image.copy()

"""ROTATED BOUNDING BOX
NOTE: The cv2.minAreaRect function takes the contour 
and returns a tuple with 3 values. The first value of the tuple 
is the starting (x, y)-coordinates of the rotated bounding box. 
The second value is the width and height of the bounding box. 
And the final value angle of rotation of the shape.

NOTE: since we want to draw a rotated bounding box rather than a 
standard bounding box we won’t be able to leverage the cv2.rectangle 
function. Instead, we’ll pass the output of cv2.minAreaRect 
to the cv2.boxPoints which converts the (x, y)-coordinates, 
width and height, and angle of rotation into a set of coordinates points.
"""

# loop over the contours
for c in cnts:
    # fit the rotated bounding box to the contour and draw the rotated bounding box
    box = cv2.minAreaRect(c)
    print(box)
    box = np.int0(cv2.boxPoints(box))
    cv2.drawContours(clone, [box], -1, (0, 255, 0), 2)

# show the output image
cv2.imshow('Rotated Bounding Boxes', clone)

clone = image.copy()

"""FITTING AN ELLIPSE
Fitting an ellipse to a contour is much like fitting a rotated rectangle to a contour.
A contour must have at least 5 points for an ellipse to be computed
"""

# loop over the contours
for c in cnts:
    # to fit an ellipse, our contour must have at least 5 points
    if len(c) >= 5:
    # fit and ellipse to the contour
        ellipse = cv2.fitEllipse(c)
        cv2.ellipse(clone, ellipse, (0, 255, 0), 2)

# show the output image
cv2.imshow('Ellipse', clone)

"""EXERCISE
Find contour properties of shapes using OpenCV
"""

clone = image.copy()

for (i, c) in enumerate(cnts):

    cv2.drawContours(clone, [c], -1, (0, 255, 0), 2)

    M = cv2.moments(c)
    cx = int(M['m10'] / M['m00'])
    cy = int(M['m01'] / M['m00'])

    cv2.putText(clone, f'#{i+1}', (cx -20, cy), cv2.FONT_HERSHEY_SIMPLEX,
                1.25, (255, 255, 255), 4)

    print(f'Centroid of shape #{i + 1} is {(cx, cy)}')

    area = cv2.contourArea(c)
    perimeter = cv2.arcLength(c, True)

    print(f'Properties of the shape #{i+ 1} are -- area: {area} and perimeter: {perimeter}')

    box = cv2.boundingRect(c)

    print(f'Bounding box of shape #{i + 1} is {box}')

    (x, y, w, h) = box

    cv2.rectangle(clone,  (x, y), (x + w, y + h), (0, 255, 2), 2)

    circle = cv2.minEnclosingCircle(c)
    centre, radius = circle
    print(f'Minimum enclosing circle of shape #{i + 1} is {radius}\n')

    cv2.circle(clone, tuple(map(int, centre)), int(radius), (0, 0, 255), 2)

cv2.imshow('Contour Properties', clone)
cv2.waitKey(0)


