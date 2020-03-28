# import the necessary packages
import cv2

# load the image and show it
image = cv2.imread("../img/florida_trip.png")
cv2.imshow("Original", image)

# cropping an image is accomplished using simple NumPy array slices --
# let's crop the face from the image
face = image[85:250, 85:220]
cv2.imshow("Face", face)

# ...and now let's crop the entire body
body = image[90:450, 0:290]
cv2.imshow("Body", body)

# crop the people in the background
people = image[173:235, 13:81]
cv2.imshow('People', people)

# crop boat/building structure
people = image[124:212, 225:380]
cv2.imshow('Buildings/Boat', people)
cv2.waitKey(0)
