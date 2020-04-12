# import the nececessary packages
import numpy as np
import argparse
import cv2
import imutils

def sort_contours(cnts, method='left-to-right'):
    # initialise the reverse flag and sort index
    reverse = False
    i = 0

    # handle if we need to sort in reverse
    if method == 'right-to-left' or method == 'bottom-to-top':
        reverse = True

    # handle if we are sorting against the y-coordinate rather than
    # the x coordinate of the bounding box
    if method == 'top-to-bottom' or method == 'bottom-to-top':
        i = 1

    # construct the list of bounding boxes and sort them from top to bottom
    bounding_boxes = [cv2.boundingRect(c) for c in cnts]

    # NOTE: The sorting key is based on x or y axis of bounding boxes
    (cnts, bounding_boxes) = zip(*sorted(zip(cnts, bounding_boxes),
                                         key= lambda b: b[1][i],
                                         reverse=reverse))
    # return the list of sorted contours and bounding boxes
    return (cnts, bounding_boxes)

def draw_contour(image, c, i):
    # compute the center of the contour area and draw a circle
	# representing the center
    M = cv2.moments(c)
    cX = int(M["m10"] / M["m00"])
    cY = int(M["m01"] / M["m00"])

    # draw the countour number on the image
    cv2.putText(image, "#{}".format(i + 1), (cX - 20, cY), cv2.FONT_HERSHEY_SIMPLEX,
		1.0, (255, 255, 255), 2)

    # return the image with the contour number drawn on it
    return image

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the input image")
ap.add_argument("-m", "--method", required=True, help="Sorting method")
args = vars(ap.parse_args())

# load the image and initialize the accumulated edge image
image = cv2.imread(args["image"])
cv2.imshow('Original', image)

accumEdged = np.zeros(image.shape[:2], dtype="uint8")
channels = ['Blue', 'Green', 'Red']

# loop over the blue, green, and red channels, respectively
for (i, chan) in enumerate(cv2.split(image)):
    # blur the channel, extract edges from it, and accumulate the set
    # of edges for the image
    chan = cv2.medianBlur(chan, 11)
    edged = cv2.Canny(chan, 50, 200)
    accumEdged = cv2.bitwise_or(accumEdged, edged)
    cv2.imshow(f'channel {channels[i]}', chan)

# show the accumulated edge map
cv2.imshow("Edge Map", accumEdged)

blur = cv2.medianBlur(image, 11)
image_edges = cv2.Canny(blur, 50, 200)
cv2.imshow('Edge Map All Channels in one go', image_edges)

cv2.waitKey(0)

# find contours in the accumulated image, keeping only the largest
# ones
cnts= cv2.findContours(accumEdged.copy(), cv2.RETR_EXTERNAL,
	cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:5]
orig = image.copy()

# loop over the (unsorted) contours and draw them
for (i, c) in enumerate(cnts):
    orig = draw_contour(orig, c, i)

# show the original, unsorted contour image
cv2.imshow("Unsorted", orig)

# sort the contours according to the provided method
(cnts, boundingBoxes) = sort_contours(cnts, method=args["method"])

# loop over the (now sorted) contours and draw them
for (i, c) in enumerate(cnts):
    draw_contour(image, c, i)

# show the output image
cv2.imshow("Sorted", image)
cv2.waitKey(0)
