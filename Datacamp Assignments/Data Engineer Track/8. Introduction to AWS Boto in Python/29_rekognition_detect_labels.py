# Use the Rekognition client to detect the labels for image1. Return a maximum of 1 label.
# Detect the labels for image2 and print the response's labels..

import boto3

# Create boto3 client to rekog
rekog = boto3.client('rekognition', region_name='us-east-1', 
                         aws_access_key_id=AWS_KEY_ID, 
                         aws_secret_access_key=AWS_SECRET)


image1 = {'S3Object': {'Bucket': 'datacamp-gid-images', 'Name': 'report_1010.jpg'}}
image2 = {'S3Object': {'Bucket': 'datacamp-gid-images', 'Name': 'report_1111.jpg'}}

# Use Rekognition client to detect labels
image1_response = rekog.detect_labels(
    # Specify the image as an S3Object; Return one label
    Image=image1, MaxLabels=1)

# Print the labels
print(image1_response['Labels'])

# Use Rekognition client to detect labels
image2_response = rekog.detect_labels(Image = image2, MaxLabels =1)

# Print the labels
print(image2_response['Labels'])

# <script.py> output:
#     [{'Confidence': 99.85968017578125, 'Instances': [], 'Name': 'Walkway', 'Parents': [{'Name': 'Path'}]}]
#     [{'Confidence': 96.95977020263672, 'Instances': [{'BoundingBox': 
#     {'Height': 0.3252439796924591, 'Left': 0.668968915939331, 'Top': 0.14526571333408356, 
#     'Width': 0.1563364714384079}, 'Confidence': 96.95977020263672}], 
#     'Name': 'Cat', 'Parents': [{'Name': 'Pet'}, {'Name': 'Mammal'}, {'Name': 'Animal'}]}]