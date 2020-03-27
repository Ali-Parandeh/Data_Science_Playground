import argparse
import imutils
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True, help='Path to the image')
args = vars(ap.parse_args())

# load the image and show it
image = cv2.imread(args["image"])
cv2.imshow("Original", image)

# we need to keep in mind the aspect ratio so the image does not
# look distorted -- therefore, we calculate the ratio of the new image
# to the old image. Let's make our new image have a width of 150 pixels
r = 150.0 / image.shape[1]
dim = (150, int(image.shape[0] * r))

# perform the actual resize of the image
resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
cv2.imshow('Resized (width)', resized)

# what if we wanted to adjust the height of the image? We can apply
# the same concept, again keeping in mind the aspect ratio, but instead
# calculating the ratio based on height -- let's make the height of the
# resized image 50 pixels
r = 50.0 / image.shape[0]
dim = (int(image.shape[1] * r), 50)

# perform the resizing
resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
cv2.imshow("Resized (Height)", resized)

# using imutils resize function
resized = imutils.resize(image, width=800)
cv2.imshow('Resized via function',resized)

# construct the list of interpolation methods
methods = [
    ('cv2.INTER_NEAREST', cv2.INTER_NEAREST),
    ('cv2.INTER_LINEAR', cv2.INTER_LINEAR),
    ('cv2.INTER_AREA', cv2.INTER_AREA),
    ('cv2.INTER_CUBIC', cv2.INTER_CUBIC),
    ('cv2.INTER_LANCZOS4', cv2.INTER_LANCZOS4)
]

# loop over the interpolation methods
for (name, method) in methods:
    # increase the size of the image by x3 using the current
    # interpolation methods
    resized = imutils.resize(image, width=image.shape[1] * 3, inter=method)
    # cv2.imshow(f"Method: {name}", resized)
    # cv2.waitKey(0)

resized = imutils.resize(image, width = 100, inter=cv2.INTER_NEAREST)
(b, g, r) = resized[74, 20]
print(f'Value of pixel at (20, 74) is Red: {r}, Green: {g}, Blue: {b}')

resized = imutils.resize(image,
                         width = image.shape[1]*2,
                         inter=cv2.INTER_NEAREST)
(b, g, r) = resized[367, 170]
print(f'Value of pixel at (170, 367) is Red: {r}, Green: {g}, Blue: {b}')