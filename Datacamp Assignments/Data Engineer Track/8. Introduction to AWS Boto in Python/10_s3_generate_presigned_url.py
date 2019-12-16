# Generating a presigned URL

# Sam got a special request from City Council to analyze whether the City 
# is prioritizing requests in District 11, while de-prioritizing 
# requests in the less affluent district 12. They asked her to keep 
# this report confidential, as they would like to see it before it goes public to the media.

# Sam has generated the report and is ready to share it with the City 
# council, but making it public makes her too paranoid. She decided to 
# provide the Council with a presigned URL so they can temporarily access the report for 1 hour.

# She has already initialized the boto3 S3 client and assigned it to the s3 variable.

# Help her generate a presigned URL valid for 1 hour to 'final_report.csv' 
# in the 'gid-staging' bucket. Then, print it out for the City Council!

import boto3

# Create boto3 client to S3
s3 = boto3.client('s3', region_name='us-east-1', 
                         aws_access_key_id=AWS_KEY_ID, 
                         aws_secret_access_key=AWS_SECRET)
                         
# Generate presigned_url for the uploaded object
share_url = s3.generate_presigned_url(
  # Specify allowable operations
  ClientMethod='get_object',
  # Set the expiration time
  ExpiresIn=3600,
  # Set bucket and shareable object's name
  Params={'Bucket': 'gid-staging','Key': 'final_report.csv'}
)

# Print out the presigned URL
print(share_url)

# <script.py> output:
#     https://gid-staging.s3.amazonaws.com/
#     final_report.csv?AWSAccessKeyId=IAmAFakeKey&Signature=C0qfmi7R9iBJQQ%2F1%2B9a8tES5ZbY%3D&Expires=1576457339