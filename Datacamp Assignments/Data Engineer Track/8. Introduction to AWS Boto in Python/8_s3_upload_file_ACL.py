
# Uploading a public report
# As you saw in Chapter 1, Get It Done is an App that lets residents 
# report problems like potholes and broken sidewalks.

# The data from the app is a very hot topic political issue. 
# Residents keep saying that the City does not distribute work 
# evenly across neighborhoods when issues are reported. 
# The City Council wants to be transparent with the public 
# and has asked Sam to publish the aggregated Get It Done 
# reports and make them publicly available.

# Sam has initialized the boto3 S3 client and assigned 
# it to the s3 variable.

# In this exercise, you will help her increase government 
# transparency by uploading public reports to the gid-staging bucket.

import boto3

# Create boto3 client to S3
s3 = boto3.client('s3', region_name='us-east-1', 
                         aws_access_key_id=AWS_KEY_ID, 
                         aws_secret_access_key=AWS_SECRET)


# Upload the final_report.csv to gid-staging bucket
s3.upload_file(
  # Complete the filename
  Filename='./final_report.csv', 
  # Set the key and bucket
  Key='2019/final_report_2019_02_20.csv', 
  Bucket='gid-staging',
  # During upload, set ACL to public-read
  ExtraArgs = {'ACL': 'public-read'})

# You have just uploaded an object that's public from the very beginning.