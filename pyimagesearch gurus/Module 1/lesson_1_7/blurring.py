# import the necessary packages
import argparse
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

# load the image, display it and initialise the list of kernel sizes
image = cv2.imread(args['image'])
cv2.imshow('Original', image)
kernel_sizes = [(3, 3), (9, 9), (15, 15)]

"""AVERAGE BLURRING
An average filter does exactly what you think it might do —
takes an area of pixels surrounding a central pixel,
averages all these pixels together, and replaces the central pixel with the average.
"""

# loop over the kernel sizes and apply an average blur to the image
for (kx, ky) in kernel_sizes:
    blurred = cv2.blur(image, (kx, ky))
    cv2.imshow(f'Average ({kx}, {ky})', blurred)

"""GAUSSIAN BLURRING
Gaussian blurring is similar to average blurring,
but instead of using a simple mean, we are now using
a weighted mean, where neighborhood pixels that are
closer to the central pixel contribute more “weight”
to the average. 

And as the name suggests, Gaussian smoothing
is used to remove noise that approximately follows a Gaussian distribution.
The end result is that our image is less blurred,
but more naturally blurred, than using the average method.

Again, as the size of your kernel increases, your image will
become progressively more blurred. This could easily lead to a point where you
lose the edges of important structural objects in the image.
"""

# close all windows to clean up the screen
cv2.destroyAllWindows()
cv2.imshow('Original', image)

# loop over the kernel size and apply a Gaussian blur to the image
for (kx, ky) in kernel_sizes:

    # The last parameter is our sigma, the standard deviation of
    # the Gaussian distribution. By setting this value to 0, we are
    # instructing OpenCV to automatically compute sigma based on
    # kernel size. In most cases, you’ll want to let your sigma be computed for you
    blurred = cv2.GaussianBlur(image, (kx, ky), 0)
    cv2.imshow(f'Gaussian ({kx}, {ky})', blurred)

"""MEDIAN BLURRING
median blur method has been most effective when removing salt-and-pepper noise.
unlike average blurring and Gaussian blurring where the kernel size could be
rectangular, the kernel size for the median must be square.
(unlike the averaging method), instead of replacing the central pixel
with the average of the neighborhood, we instead replace the central
pixel with the median of the neighborhood.

methods such as averaging and Gaussian compute means or weighted means 
for the neighborhood — this average pixel intensity may or may not be 
present in the neighborhood. But by definition, the median pixel must 
exist in our neighborhood. By replacing our central pixel with a median 
rather than an average, we can substantially reduce noise.

for damaged images or photos captured under highly sub-optimal conditions, 
a median blur can really help as a pre-processing step prior to passing 
the image along to other methods, such as thresholding and edge detection.
"""

# close all windows to clean up the screen
cv2.destroyAllWindows()
cv2.imshow('Original', image)

for k in (3, 9, 15):
    blurred = cv2.medianBlur(image, k)
    cv2.imshow(f'Median {k}', blurred)

"""BILATERAL BLURRING
In order to reduce noise while still maintaining edges, we can use bilateral blurring. 
bilateral blurring accomplishes this by introducing two Gaussian distributions.

The first Gaussian function only considers spatial neighbors. 
That is, pixels that appear close together in the (x, y)-coordinate
space of the image. The second Gaussian then models the pixel intensity 
of the neighborhood, ensuring that only pixels with similar intensity are
included in the actual computation of the blur.

If pixels in the same (small) neighborhood have a similar pixel value, 
then they likely represent the same object. But if two pixels in the 
same neighborhood have contrasting values, then we could be examining 
the edge or boundary of an object — and we would like to preserve this edge.

this method is able to preserve edges of an image, 
while still reducing noise. The largest downside to this method is 
that it is considerably slower than its averaging, Gaussian, 
and median blurring counterparts.

PARAMS:
1. diameter: The larger diameter is, the more pixels will 
be included in the blurring computation. Think of this 
parameter as a square kernel size.

2. colour standard deviation:  A larger value for sigma_colour 
means that more colors in the neighborhood will be considered 
when computing the blur. If we let sigma_colour get too large in 
respect to the diameter, then we essentially have broken the assumption  
of bilateral filtering — that only pixels of similar color should contribute 
significantly to the blur.

3. space standard deviation: A larger value of sigma_space means that pixels 
farther out from the central pixel diameter will influence the blurring calculation.

The effect bilateral filtering on your edges will be dramatically smoothed detail 
and texture, while still preserving boundaries and edges.
"""

# close all windows to clean up the screen
cv2.destroyAllWindows()
cv2.imshow('Original', image)
params = [(11, 21, 7), (11, 41, 21), (11, 61, 39)]

# loop over the diameter, sigma colour, and sigma space
for (diameter, sigma_colour, sigma_space) in params:
    # apply bilateral filtering and display the image
    blurred = cv2.bilateralFilter(image, diameter, sigma_colour, sigma_space)
    title = f'Blurred d={diameter}, sc={sigma_colour}, ss={sigma_space}'
    cv2.imshow(title, blurred)
    cv2.waitKey(0)

"""SUMMARY
The simple average method is fast, but may not preserve edges in images.

Applying a Gaussian blur is better at preserving edges, 
but is slightly slower than the average method.

A median filter is primarily used to reduce salt-and-pepper 
style noise as the median statistic is much more robust and less sensitive 
to outliers than other statistical methods such as the mean.

Finally, the bilateral filter preserves edges, but is substantially slower 
than the other methods. Bilateral filtering also boasts the most parameters 
to tune which can become a nuisance to tune correctly.
"""
