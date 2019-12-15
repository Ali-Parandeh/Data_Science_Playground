import boto3

# Create boto3 client to S3
s3 = boto3.client('s3', region_name='us-east-1', 
                         aws_access_key_id=AWS_KEY_ID, 
                         aws_secret_access_key=AWS_SECRET)

# Get the list_buckets response
response = s3.list_buckets()

print(response)
# {'Buckets': [{'CreationDate': datetime.datetime(2006, 2, 3, 16, 45, 9, tzinfo=tzlocal()),
#    'Name': 'gim-staging'},
#   {'CreationDate': datetime.datetime(2006, 2, 3, 16, 45, 9, tzinfo=tzlocal()),
#    'Name': 'gim-processed'},
#   {'CreationDate': datetime.datetime(2006, 2, 3, 16, 45, 9, tzinfo=tzlocal()),
#    'Name': 'gim-test'}],
#  'Owner': {'DisplayName': 'webfile', 'ID': 'bcaf1ffd86f41161ca5fb16fd081034f'},
#  'ResponseMetadata': {'HTTPHeaders': {},
#   'HTTPStatusCode': 200,
#   'RetryAttempts': 0}}

# Iterate over Buckets from .list_buckets() response
for bucket in response['Buckets']:
      
  	# Print the Name for each bucket
    print(bucket['Name'])



# <script.py> output:
#     gim-staging
#     gim-processed
#     gim-test