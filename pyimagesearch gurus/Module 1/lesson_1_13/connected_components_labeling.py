# import the necessary packages
from skimage.filters import threshold_local
from skimage import measure
import numpy as np
import cv2

# load the license plate image from disk
plate = cv2.imread('../img/license_plate.png')

# extract the Value component from the HSV color space and apply adaptive thresholding
# to reveal the characters on the license plate
V = cv2.split(cv2.cvtColor(plate, cv2.COLOR_BGR2HSV))[2]
thresh = cv2.adaptiveThreshold(V, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                               cv2.THRESH_BINARY_INV, 17, 3)

# show the images
cv2.imshow('Licence Plate', plate)
cv2.imshow('Thresh', thresh)

# perform connected components analysis on the thresholded images and initialize the
# mask to hold only the "large" components we are interested in
labels = measure.label(thresh, neighbors=8, background=0)
mask = np.zeros(thresh.shape, dtype='uint8')
print(f'[INFO] found {np.unique(labels)} blobs')

# loop over the unique components
for (i, label) in enumerate(np.unique(labels)):
    # if the label is background, ignore it
    if label == 0:
        print(f'[INFO] label: 0 (background)')

    # otherwise, construct the label mask to display only connected components for
    # the current label
    print(f'[INFO] label: {i} (foreground)')
    label_mask = np.zeros(thresh.shape, dtype='uint8')
    label_mask[labels == label] = 255
    num_pixels = cv2.countNonZero(label_mask)

    # if the number of pixels in the component is sufficiently large, add it to our
    # mask of "large" blobs
    if num_pixels > 500 and num_pixels < 1500:
        mask = cv2.add(mask, label_mask)
        
    # show the label mask
    cv2.imshow('Label', label_mask)
    cv2.waitKey(0)

# show the large components in the image
cv2.imshow('Large Blobs', mask)
cv2.waitKey(0)

