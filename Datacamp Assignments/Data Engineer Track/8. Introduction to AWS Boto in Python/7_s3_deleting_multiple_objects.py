# Spring cleaning

# In City governments, record retention is a huge issue, 
# and many government officials prefer not to keep records 
# in existence past the mandated retention dates.

# As time has passed, the City Council asked Sam to clean 
# out old CSV files from previous years that have passed 
# the retention period. 2018 is safe to delete.

# Sam has initialized the client and assigned it to the s3 variable. 
# Help her clean out all records for 2018 from S3!


# List only objects that start with '2018/final_'
response = s3.list_objects(Bucket='gid-staging', 
                           Prefix='2018/final_')

# Iterate over the objects
if 'Contents' in response:
  for obj in response['Contents']:
      # Delete the object
      s3.delete_object(Bucket='gid-staging', Key=obj['Key'])

# Print the keys of remaining objects in the bucket
response = s3.list_objects(Bucket='gid-staging')

print(response)

# {'Contents': [{'ETag': '"1519c57b81bb9257756c04dee24dd728"',
#    'Key': '2018/final_report_01_00',
#    'LastModified': datetime.datetime(2019, 12, 15, 21, 44, 32, 238000, tzinfo=tzlocal()),
#    'Owner': {'DisplayName': 'webfile',
#     'ID': '75aa57f09aa0c8caeab4f8c24e99d10f8e7faeebf76c078efc7c6caea54ba06a'},
#    'Size': 209,
#    'StorageClass': 'STANDARD'},
#   {'ETag': '"1519c57b81bb9257756c04dee24dd728"',
#    'Key': '2018/final_report_01_01',
#    'LastModified': datetime.datetime(2019, 12, 15, 21, 44, 32, 243000, tzinfo=tzlocal()),
#    'Owner': {'DisplayName': 'webfile',
#     'ID': '75aa57f09aa0c8caeab4f8c24e99d10f8e7faeebf76c078efc7c6caea54ba06a'},
#    'Size': 209,
#    'StorageClass': 'STANDARD'},
#   {'ETag': '"1519c57b81bb9257756c04dee24dd728"',
#    'Key': '2018/final_report_01_02',
#    'LastModified': datetime.datetime(2019, 12, 15, 21, 44, 32, 249000, tzinfo=tzlocal()),
#    'Owner': {'DisplayName': 'webfile',
#     'ID': '75aa57f09aa0c8caeab4f8c24e99d10f8e7faeebf76c078efc7c6caea54ba06a'},
#    'Size': 209,
#    'StorageClass': 'STANDARD'},
#   {'ETag': '"1519c57b81bb9257756c04dee24dd728"',
#    'Key': '2018/final_report_01_03',
#    'LastModified': datetime.datetime(2019, 12, 15, 21, 44, 32, 254000, tzinfo=tzlocal()),
#    'Owner': {'DisplayName': 'webfile',
#     'ID': '75aa57f09aa0c8caeab4f8c24e99d10f8e7faeebf76c078efc7c6caea54ba06a'},
#    'Size': 209,
#    'StorageClass': 'STANDARD'},
#   {'ETag': '"1519c57b81bb9257756c04dee24dd728"',
#    'Key': '2018/final_report_01_04',
#    'LastModified': datetime.datetime(2019, 12, 15, 21, 44, 32, 259000, tzinfo=tzlocal()),
#    'Owner': {'DisplayName': 'webfile',
#     'ID': '75aa57f09aa0c8caeab4f8c24e99d10f8e7faeebf76c078efc7c6caea54ba06a'},
#    'Size': 209,
#    'StorageClass': 'STANDARD'},
#   {'ETag': '"1519c57b81bb9257756c04dee24dd728"',
#    'Key': '2018/final_report_01_05',
#    'LastModified': datetime.datetime(2019, 12, 15, 21, 44, 32, 265000, tzinfo=tzlocal()),
#    'Owner': {'DisplayName': 'webfile',
#     'ID': '75aa57f09aa0c8caeab4f8c24e99d10f8e7faeebf76c078efc7c6caea54ba06a'},
#    'Size': 209,
#    'StorageClass': 'STANDARD'},
#   {'ETag': '"1519c57b81bb9257756c04dee24dd728"',
#    'Key': '2018/final_report_01_06',
#    'LastModified': datetime.datetime(2019, 12, 15, 21, 44, 32, 270000, tzinfo=tzlocal()),
#    'Owner': {'DisplayName': 'webfile',
#     'ID': '75aa57f09aa0c8caeab4f8c24e99d10f8e7faeebf76c078efc7c6caea54ba06a'},
#    'Size': 209,
#    'StorageClass': 'STANDARD'}],
#  'Delimiter': 'None',
#  'IsTruncated': False,
#  'MaxKeys': 1000,
#  'Name': 'gid-staging',
#  'Prefix': '2018/final_',
#  'ResponseMetadata': {'HTTPHeaders': {},
#   'HTTPStatusCode': 200,
#   'RetryAttempts': 0}}

for obj in response['Contents']:
  	print(obj['Key'])

# <script.py> output:
#     2019/final_report_01_00
#     2019/final_report_01_01
#     2019/final_report_01_02
#     2019/final_report_01_03
#     2019/final_report_01_04