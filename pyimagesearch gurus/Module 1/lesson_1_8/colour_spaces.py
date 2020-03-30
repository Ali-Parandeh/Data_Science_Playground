# import the necessary packages
import argparse
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

# load the original image and display it (RGB)
image = cv2.imread(args["image"])
cv2.imshow("RGB", image)

# loop over each of the individual channels and display them
for (name, chan) in zip(('B', 'G', 'R'), cv2.split(image)):
    cv2.imshow(name, chan)

# close all windows.
cv2.destroyAllWindows()

# convert the image to the HSV colour space and show it
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
cv2.imshow('HSV', hsv)

# loop over each of the individual channels and display them
for (name, chan) in zip(('H', 'S', 'V'), cv2.split(hsv)):
    cv2.imshow(name, chan)

# wait for a keypress, then close all windows.
cv2.destroyAllWindows()

# convert the image to the L*a*b* colour space and show it
lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
cv2.imshow('L*a*b*', lab)

# loop over each of the individual channels and display them
for (name, chan) in zip(("L*", "a*", "b*"), cv2.split(lab)):
    cv2.imshow(name, chan)

# wait for a keypress, then close all open windows
cv2.destroyAllWindows()

# show the original and grayscale versions of the image
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original", image)
cv2.imshow("Grayscale", gray)
cv2.destroyAllWindows()

# EXERCISE: Convert the following RGB triplet to grayscale: (156, 107, 81)
# when converting to grayscale, each RGB channel is weighted based on eye's sensitivity to colour
# Y = 0.299 * R + 0.587 * G + 0.114 * B
(r, g, b) = (156, 107, 81)
gray_pixel = r*0.299 + g*0.587 + b*0.114
print(gray_pixel)
