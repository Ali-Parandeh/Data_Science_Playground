# Opening a private file

# The City Council wants to see the bigger trend and have asked Sam to 
# total up all the requests since the beginning of 2019. In order to 
# do this, Sam has to read daily CSVs from the 'gid-requests' bucket 
# and concatenate them. However, the gid-requests files are private. 
# She has access to them via her key, but the world cannot access them.

# In this exercise, you will help Sam see the bigger picture by 
# reading these private files into pandas and concatenating them into one DataFrame!

# She has already initialized the boto3 S3 client and assigned it 
# to the s3 variable. She has listed all the objects in gid-requests in the response variable.


import boto3, datetime
import pandas as pd
from datetime import tzlocal

# Create boto3 client to S3
s3 = boto3.client('s3', region_name='us-east-1', 
                         aws_access_key_id=AWS_KEY_ID, 
                         aws_secret_access_key=AWS_SECRET)

df_list =  [ ] 
response = {'Contents': [{'ETag': '"1519c57b81bb9257756c04dee24dd728"',
   'Key': '2019/final_report_01_00.csv',
   'LastModified': datetime.datetime(2019, 12, 15, 23, 53, 28, 291000, tzinfo=tzlocal()),
   'Owner': {'DisplayName': 'webfile',
    'ID': '75aa57f09aa0c8caeab4f8c24e99d10f8e7faeebf76c078efc7c6caea54ba06a'},
   'Size': 209,
   'StorageClass': 'STANDARD'},
  {'ETag': '"1519c57b81bb9257756c04dee24dd728"',
   'Key': '2019/final_report_01_01.csv',
   'LastModified': datetime.datetime(2019, 12, 15, 23, 53, 28, 297000, tzinfo=tzlocal()),
   'Owner': {'DisplayName': 'webfile',
    'ID': '75aa57f09aa0c8caeab4f8c24e99d10f8e7faeebf76c078efc7c6caea54ba06a'},
   'Size': 209,
   'StorageClass': 'STANDARD'},
  {'ETag': '"1519c57b81bb9257756c04dee24dd728"',
   'Key': '2019/final_report_01_02.csv',
   'LastModified': datetime.datetime(2019, 12, 15, 23, 53, 28, 301000, tzinfo=tzlocal()),
   'Owner': {'DisplayName': 'webfile',
    'ID': '75aa57f09aa0c8caeab4f8c24e99d10f8e7faeebf76c078efc7c6caea54ba06a'},
   'Size': 209,
   'StorageClass': 'STANDARD'},
  {'ETag': '"1519c57b81bb9257756c04dee24dd728"',
   'Key': '2019/final_report_01_03.csv',
   'LastModified': datetime.datetime(2019, 12, 15, 23, 53, 28, 304000, tzinfo=tzlocal()),
   'Owner': {'DisplayName': 'webfile',
    'ID': '75aa57f09aa0c8caeab4f8c24e99d10f8e7faeebf76c078efc7c6caea54ba06a'},
   'Size': 209,
   'StorageClass': 'STANDARD'},
  {'ETag': '"1519c57b81bb9257756c04dee24dd728"',
   'Key': '2019/final_report_01_04.csv',
   'LastModified': datetime.datetime(2019, 12, 15, 23, 53, 28, 308000, tzinfo=tzlocal()),
   'Owner': {'DisplayName': 'webfile',
    'ID': '75aa57f09aa0c8caeab4f8c24e99d10f8e7faeebf76c078efc7c6caea54ba06a'},
   'Size': 209,
   'StorageClass': 'STANDARD'}],
 'Delimiter': 'None',
 'IsTruncated': False,
 'MaxKeys': 1000,
 'Name': 'gid-requests',
 'Prefix': 'None',
 'ResponseMetadata': {'HTTPHeaders': {},
  'HTTPStatusCode': 200,
  'RetryAttempts': 0}}

for file in response['Contents']:
    # For each file in response load the object from S3
    obj = s3.get_object(Bucket='gid-requests', Key=file['Key'])
    # Load the object's StreamingBody with pandas
    obj_df = pd.read_csv(obj['Body'])
    # Append the resulting DataFrame to list
    df_list.append(obj_df)

# Concat all the DataFrames with pandas
df = pd.concat(df_list)

# Preview the resulting DataFrame
df.head()

#         service_name  request_count
# 0  72 Hour Violation              8
# 1   Graffiti Removal              2
# 2  Missed Collection             12
# 3   Street Light Out             21
# 4            Pothole             33

# You just loaded and combined multiple private files. Making it rain private files!

