import numpy as np
import cv2

# initialise our canvas as 300x300 with 3 channels, Red, Green,
# and Blue, with a black background
canvas = np.zeros((300, 300, 3), dtype='uint8')

# draw a green line from the top-left corner of our canvas to the
# bottom-right
green = (0, 255, 0)
cv2.line(canvas, (0, 0), (300, 300), green)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

# now, draw a 3 pixel thick red lne from the top-right corner to the
# bottom-left
red = (0, 0, 255)
cv2.line(canvas, (300, 0), (0, 300), red, 3)
cv2.imshow('Canvas', canvas)
cv2.waitKey(0)

# draw a green 50x50 pixel square, starting at 10x10 and ending at 60x60
cv2.rectangle(canvas, (10,10), (60, 60), green)
cv2.imshow('Canvas', canvas)
cv2.waitKey(0)

# draw another rectangle, this time we'll make it red and 5 pixels thick
cv2.rectangle(canvas, (50, 200), (200, 225), red, 5)
cv2.imshow('Canvas', canvas)
cv2.waitKey(0)

# let's draw one last rectangle: blue and filled in
blue = (255, 0, 0)
cv2.rectangle(canvas, (200,50), (225, 125), blue, -1)
cv2.imshow('Canvas', canvas)
cv2.waitKey(0)