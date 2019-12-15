# Deleting multiple buckets

# The Get It Done app used to be called Get It Made. Sam always 
# thought it was a terrible name, but it got stuck in her head nonetheless.

# When she was making the pipeline buckets, she used the gim- 
# abbreviation for the old name. She decides to switch her 
# abbreviation to gid- to accurately reflect the app's real (and better) name.

# She has already set up the boto3 S3 client and assigned 
# it to the s3 variable.

# Help Sam delete all the buckets in her account that start 
# with the gim- prefix. Then, help her make a 'gid-staging' and a 'gid-processed' bucket.

import boto3

# Create boto3 client to S3
s3 = boto3.client('s3', region_name='us-east-1', 
                         aws_access_key_id=AWS_KEY_ID, 
                         aws_secret_access_key=AWS_SECRET)


# Get the list_buckets response
response = s3.list_buckets()

# Delete all the buckets with 'gim', create replacements.
for bucket in response['Buckets']:
  if 'gim' in bucket['Name']:
      s3.delete_bucket(Bucket=bucket['Name'])
    
s3.create_bucket(Bucket='gid-staging')
s3.create_bucket(Bucket='gid-processed')
  
# Print bucket listing after deletion
response = s3.list_buckets()
for bucket in response['Buckets']:
    print(bucket['Name'])


# <script.py> output:
#     gid-staging
#     gid-processed

# Excellent! You just did your first recursive bucket operation. 
# You can combine loops and client calls to perform operations on 
# many buckets at once. Just be careful and don't delete something you need.

