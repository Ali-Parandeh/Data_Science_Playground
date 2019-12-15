# Putting files in the cloud

# Sam has already created the gid-staging bucket. 
# She has already downloaded the files from the URLs, 
# analyzed them, and wrote the results to final_report.csv.

# She has also already initialized the boto3 S3 client 
# and assigned it to the s3 variable.

# Help Sam upload final_report.csv to the gid-staging bucket!

import boto3

# Create boto3 client to S3
s3 = boto3.client('s3', region_name='us-east-1', 
                         aws_access_key_id=AWS_KEY_ID, 
                         aws_secret_access_key=AWS_SECRET)


# Upload final_report.csv to gid-staging
s3.upload_file(Bucket='gid-staging',
              # Set filename and key
               Filename='final_report.csv', 
               Key='2019/final_report_01_01.csv')

# Get object metadata and print it
response = s3.head_object(Bucket='gid-staging', 
                       Key='2019/final_report_01_01.csv')

print(response)
# {'ContentLength': 209,
#  'ETag': '"1519c57b81bb9257756c04dee24dd728"',
#  'LastModified': datetime.datetime(2019, 12, 15, 21, 41, 49, tzinfo=tzutc()),
#  'Metadata': {},
#  'ResponseMetadata': {'HTTPHeaders': {'content-length': '209',
#    'content-md5': 'FRnFe4G7kld1bATe4k3XKA==',
#    'etag': '"1519c57b81bb9257756c04dee24dd728"',
#    'last-modified': 'Sun, 15 Dec 2019 21:41:49 GMT'},
#   'HTTPStatusCode': 200,
#   'RetryAttempts': 0}}

# Print the size of the uploaded object
print(response['ContentLength'])


# <script.py> output:
#     209