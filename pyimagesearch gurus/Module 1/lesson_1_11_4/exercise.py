# import the necessary packages
import cv2
import imutils

# load the the cirles and squares image and convert it to grayscale
image = cv2.imread("../img/dog_contour.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# find contours in the image
cnts = cv2.findContours(gray.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)

# loop over the contours
for c in cnts:
    # approximate the contour
    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.1 * peri, True)

    # draw the outline of the contour and draw the text on the image
    cv2.drawContours(image, [approx], -1, (0, 255, 255), 2)
    (x, y, w, h) = cv2.boundingRect(approx)

    # show difference between original and approximate contours
    print("original: {}, approx: {}".format(len(c), len(approx)))

    cv2.putText(image, "Contour", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX,
        0.5, (0, 255, 255), 2)

# show the output image
cv2.imshow("Image", image)
cv2.waitKey(0)
