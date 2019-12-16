# Update index to include February

# Read the daily Get It Done request logs for February.
# Combined them into a single DataFrame.
# Generated a DataFrame with aggregated metrics (request counts by type)
# Wrote that DataFrame to a CSV and HTML final report files.

# Now, she wants these files to be accessible 
# through the directory listing. Currently, 
# it only shows links for January reports: 
# Screenshot of Get It Done reports listing

# She has created the boto3 S3 client and stored it in the s3 variable.

# Help Sam generate a new directory listing 
# with the February's uploaded reports and store it in a DataFrame.


import boto3
import pandas as pd

# Create boto3 client to S3
s3 = boto3.client('s3', region_name='us-east-1', 
                         aws_access_key_id=AWS_KEY_ID, 
                         aws_secret_access_key=AWS_SECRET)

# List the gid-reports bucket objects starting with 2019/
objects_list = s3.list_objects(Bucket='gid-reports', Prefix='2019/')

# {'Contents': [{'ETag': '"9a682c7e6fd151d18912c319b3fac8dc"',
#    'Key': '2019/feb/final_chart.html',
#    'LastModified': datetime.datetime(2019, 12, 16, 1, 3, 2, 295000, tzinfo=tzlocal()),
#    'Owner': {'DisplayName': 'webfile',
#     'ID': '75aa57f09aa0c8caeab4f8c24e99d10f8e7faeebf76c078efc7c6caea54ba06a'},
#    'Size': 6759,
#    'StorageClass': 'STANDARD'},
#   {'ETag': '"1519c57b81bb9257756c04dee24dd728"',
#    'Key': '2019/feb/final_report.csv',
#    'LastModified': datetime.datetime(2019, 12, 16, 1, 3, 2, 288000, tzinfo=tzlocal()),
#    'Owner': {'DisplayName': 'webfile',
#     'ID': '75aa57f09aa0c8caeab4f8c24e99d10f8e7faeebf76c078efc7c6caea54ba06a'},
#    'Size': 209,
#    'StorageClass': 'STANDARD'},
#   {'ETag': '"03baa6b325d75dff02ef83af39a8205f"',
#    'Key': '2019/feb/final_report.html',
#    'LastModified': datetime.datetime(2019, 12, 16, 1, 3, 2, 291000, tzinfo=tzlocal()),
#    'Owner': {'DisplayName': 'webfile',
#     'ID': '75aa57f09aa0c8caeab4f8c24e99d10f8e7faeebf76c078efc7c6caea54ba06a'},
#    'Size': 536,
#    'StorageClass': 'STANDARD'},
#   {'ETag': '"9a682c7e6fd151d18912c319b3fac8dc"',
#    'Key': '2019/jan/final_chart.html',
#    'LastModified': datetime.datetime(2019, 12, 16, 1, 3, 2, 284000, tzinfo=tzlocal()),
#    'Owner': {'DisplayName': 'webfile',
#     'ID': '75aa57f09aa0c8caeab4f8c24e99d10f8e7faeebf76c078efc7c6caea54ba06a'},
#    'Size': 6759,
#    'StorageClass': 'STANDARD'},
#   {'ETag': '"1519c57b81bb9257756c04dee24dd728"',
#    'Key': '2019/jan/final_report.csv',
#    'LastModified': datetime.datetime(2019, 12, 16, 1, 3, 2, 274000, tzinfo=tzlocal()),
#    'Owner': {'DisplayName': 'webfile',
#     'ID': '75aa57f09aa0c8caeab4f8c24e99d10f8e7faeebf76c078efc7c6caea54ba06a'},
#    'Size': 209,
#    'StorageClass': 'STANDARD'},
#   {'ETag': '"03baa6b325d75dff02ef83af39a8205f"',
#    'Key': '2019/jan/final_report.html',
#    'LastModified': datetime.datetime(2019, 12, 16, 1, 3, 2, 280000, tzinfo=tzlocal()),
#    'Owner': {'DisplayName': 'webfile',
#     'ID': '75aa57f09aa0c8caeab4f8c24e99d10f8e7faeebf76c078efc7c6caea54ba06a'},
#    'Size': 536,
#    'StorageClass': 'STANDARD'}],
#  'Delimiter': 'None',
#  'IsTruncated': False,
#  'MaxKeys': 1000,
#  'Name': 'gid-reports',
#  'Prefix': '2019/',
#  'ResponseMetadata': {'HTTPHeaders': {},
#   'HTTPStatusCode': 200,
#   'RetryAttempts': 0}}

# Convert the response contents to DataFrame
objects_df = pd.DataFrame(objects_list['Contents'])


# [5 rows x 6 columns]

# Create a column "Link" that contains Public Object URL
base_url = "http://gid-reports.s3.amazonaws.com/"
objects_df['Link'] = base_url + objects_df['Key']

# Preview the resulting DataFrame
objects_df.head()

#                                  ETag                         Key  ...  Size StorageClass
# 0  "9a682c7e6fd151d18912c319b3fac8dc"  2019/feb/final_chart.html   ...  6759  STANDARD   
# 1  "1519c57b81bb9257756c04dee24dd728"  2019/feb/final_report.csv   ...  209   STANDARD   
# 2  "03baa6b325d75dff02ef83af39a8205f"  2019/feb/final_report.html  ...  536   STANDARD   
# 3  "9a682c7e6fd151d18912c319b3fac8dc"  2019/jan/final_chart.html   ...  6759  STANDARD   
# 4  "1519c57b81bb9257756c04dee24dd728"  2019/jan/final_report.csv   ...  209   STANDARD   