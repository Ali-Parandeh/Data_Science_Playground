# import the necessary packages
import cv2
import imutils

# load the the cirles and squares image and convert it to grayscale
image = cv2.imread("../img/circles_and_squares.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# find contours in the image
cnts = cv2.findContours(gray.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)

"""
To control the level of tolerance for the approximation, 
we need to define an (epsilon) value. 
In practice, we define this epsilon relative 
to the perimeter of the shape we are examining. 
Commonly, we’ll define epsilon as some percentage 
(usually between 1-5%) of the original contour perimeter.

This is because the internal contour approximation 
algorithm is looking for points to discard. 
The larger the epsilon value is, the more points 
will be discarded. Similarly, the smaller the epsilon value is, 
the more points will be kept.

So the question becomes: what’s the optimal value for 
epsilon? And how do we go about defining it?

It’s very clear that an epsilon value that will 
work well for some shapes will not work well for others 
(larger shapes versus smaller shapes, for instance). 
This means that we can’t simply hardcode an \epsilon value into our code 
— it must be computed dynamically based on the individual contour.

Thus, we define \epsilon relative to the perimeter length so 
we understand how large the contour region actually is. 
Doing this ensures that we achieve a consistent approximation 
for all shapes inside the image.
"""

# loop over the contours
for c in cnts:
	# approximate the contour
	peri = cv2.arcLength(c, True)
	approx = cv2.approxPolyDP(c, 0.01 * peri, True)

	# if the approximated contour has 4 vertices, then we are examining
	# a rectangle
	if len(approx) == 4:
		# draw the outline of the contour and draw the text on the image
		cv2.drawContours(image, [c], -1, (0, 255, 255), 2)
		(x, y, w, h) = cv2.boundingRect(approx)
		cv2.putText(image, "Rectangle", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX,
			0.5, (0, 255, 255), 2)

# show the output image
cv2.imshow("Image", image)
cv2.waitKey(0)
