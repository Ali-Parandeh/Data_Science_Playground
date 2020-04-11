# import the necessary packages
import numpy as np
import cv2
import imutils

# load the Tetris block image, convert it to grayscale, and threshold
# the image
image = cv2.imread("../img/more_shapes_example.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
thresh = cv2.threshold(gray, 10, 255, cv2.THRESH_BINARY)[1]  # grab array

# show the original and thresholded images
cv2.imshow("Original", image)
cv2.imshow("Thresh", thresh)

# find external contours in the thresholded image and allocate memory
# for the convex hull image
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
hull_image = np.zeros(gray.shape[:2], dtype="uint8")

# loop over the contours
for (i, c) in enumerate(cnts):
    # compute the area of the contour along with the bounding box
    # to compute teh aspect ratio
    area = cv2.contourArea(c)
    (x, y, w, h) = cv2.boundingRect(c)

    # compute the aspect ratio of the contour, which is simply the width
    # divided by the height of the bounding box
    aspect_ratio = w / float(h)

    # use the area of the contour, which is simply the width
    # the extent
    extent = area / float(w * h)

    # compute the convex hull of the contour, then use the area of the
    # original contour and the area of convex hull to compute the
    # solidity
    hull = cv2.convexHull(c)
    hull_area = cv2.contourArea(hull)
    solidity = area / float(hull_area)

    # visualise the original contours and the convex hull and initialise
    # the name of the shape
    cv2.drawContours(hull_image, [hull], -1, 255, -1)
    cv2.drawContours(image, [c], -1, (240, 0, 159), 3)
    shape = ""

    if aspect_ratio == 1.0 and solidity >= 0.95:
        shape = "CIRCLE"

    if aspect_ratio >= 3.0:
        shape = 'RECTANGLE'

    if extent < 0.7:
        shape = 'ARROW'


    # draw the shape name on the image
    cv2.putText(image, shape, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                (240, 0, 159), 2)

    # show the contour properties
    print("Contour #{} -- aspect_ratio={:.2f}, extent={:.2f}, solidity={:.2f}, shape={}"
          .format(i + 1, aspect_ratio, extent, solidity, shape))

    # show the output images
    cv2.imshow("Convex Hull", hull_image)
    cv2.imshow("Image", image)
    cv2.waitKey(0)
