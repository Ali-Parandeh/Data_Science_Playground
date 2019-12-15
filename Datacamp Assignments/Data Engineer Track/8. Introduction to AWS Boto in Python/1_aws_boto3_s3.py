import boto3

# Generate the boto3 client for interacting with S3
s3 = boto3.client('s3', region_name='us-east-1', 
                        # Set up AWS credentials 
                        aws_access_key_id=AWS_KEY_ID, 
                         aws_secret_access_key=AWS_SECRET)
# List the buckets
buckets = s3.list_buckets()

# Print the buckets
print(buckets)

# <script.py> output:
#     {'ResponseMetadata': {'HTTPStatusCode': 200, 'HTTPHeaders': {}, 'RetryAttempts': 0}, 
#     'Buckets': [{'Name': 'datacamp-hello', 'CreationDate': 
#     datetime.datetime(2006, 2, 3, 16, 45, 9, tzinfo=tzlocal())}, 
#     {'Name': 'datacamp-uploads', 'CreationDate': datetime.datetime(2006, 2, 3, 16, 45, 9, tzinfo=tzlocal())}, 
#     {'Name': 'datacamp-transfer', 'CreationDate': datetime.datetime(2006, 2, 3, 16, 45, 9, tzinfo=tzlocal())}]
#     , 'Owner': {'DisplayName': 'webfile', 'ID': 'bcaf1ffd86f41161ca5fb16fd081034f'}}