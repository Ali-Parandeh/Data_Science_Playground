import argparse
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True, help='Path to the image')
args = vars(ap.parse_args())

# load the image and convert it to greysclae
image = cv2.imread(args['image'])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('Original', image)

# apply the series of erosion
# NOTE: kernel is set to none meaning a 3x3 structural element
# is used with 8 neighbouring pixels
# NOTE: In erosion, As the number of iterations increases,
# we’ll see more and more of the PyImageSearch logo eaten away.
#  NOTE: Erosion is most useful for removing small blobs
#  from an image or disconnected two connected components.
for i in range(0, 3):
    eroded = cv2.erode(gray.copy(), None, iterations=i+1)
    cv2.imshow(f'Eroded {i+1} times', eroded)

# close all windows to cleanup the screen
cv2.destroyAllWindows()
cv2.imshow('Original', image)

# apply a series of dilations
# NOTE: Dilations are especially useful when joining broken parts of an object
for i in range(0, 3):
    dilated = cv2.dilate(gray.copy(), None, iterations=i+1)
    cv2.imshow(f'Dilated {i+1} times', dilated)

# close all windows to cleanup the screen and initialise the list
# of kernel sizes that will be applied to the image
cv2.destroyAllWindows()
cv2.imshow('Original', image)
kernel_sizes = [(3, 3), (5, 5), (7, 7)]

# loop over the kernels and apply an opening operation to the image
# Shape of the structue could be cv2.MORPH_CROSS or cv2.MORPH_ELLIPSE too
# NOTE: Performing an opening operation allows us to
# remove small blobs from an image: first an erosion is applied to
# remove the small blobs, then a dilation is applied
# to regrow the size of the original object.
for kernel_size in kernel_sizes:
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernel_size)
    opening = cv2.morphologyEx(gray, cv2.MORPH_OPEN, kernel)
    cv2.imshow(f'Opening: ({kernel_size[0]}, {kernel_size[1]})', opening)

# close all windows to cleanup the screen
cv2.destroyAllWindows()
cv2.imshow('Original', image)

# loop over the kernels and apply a closing operation to the image
# NOTE: A closing is a dilation followed by an erosion.
# NOTE: a closing is used to close holes inside of objects or for
# connecting components together.
for kernel_size in kernel_sizes:
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernel_size)
    closing = cv2.morphologyEx(gray, cv2.MORPH_CLOSE, kernel)
    cv2.imshow(f'Closing: ({kernel_size[0]}, {kernel_size[1]})', closing)


# close all windows to cleanup the screen
cv2.destroyAllWindows()
cv2.imshow('Original', image)

# loop over the kernels and apply a morphological gradient operation to the image
# NOTE: A morphological gradient is the difference between the dilation and erosion.
# It is useful for determining the outline of a particular object of an image
for kernel_size in kernel_sizes:
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernel_size)
    gradient = cv2.morphologyEx(gray, cv2.MORPH_GRADIENT, kernel)
    cv2.imshow(f'Gradient: ({kernel_size[0]}, {kernel_size[1]})', gradient)
    cv2.waitKey(0)
