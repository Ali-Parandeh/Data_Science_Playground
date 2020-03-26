import argparse
import cv2

# Construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True, help = 'Path to the image')
ap.add_argument('-o', '--output', required=True, help = 'Path to saving the image')
args = vars(ap.parse_args())

# load the image and show some basic information on it
image = cv2.imread(args['image'])
print('width: %d pixels' % (image.shape[1]))
print('height: %d pixels' % (image.shape[0]))
print('channels: %d' % (image.shape[2]))

# Show he image and wait for a keypress.
# 0 Means any key press will un pause execution
cv2.imshow('Image', image)
cv2.waitKey(0)

# save the image - OpenCV handles converting filetypes
# automatically
cv2.imwrite(args['output'], image)

# python lesson_1_1/load_display_save.py --image \
# lesson_1_1/grand_canyon.png \
# --output lesson_1_1/grand_canyon_output.jpg\
