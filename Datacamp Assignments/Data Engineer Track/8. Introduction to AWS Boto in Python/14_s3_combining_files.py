import boto3, datetime
from datetime import tzlocal
import pandas as pd

# Create boto3 client to S3
s3 = boto3.client('s3', region_name='us-east-1', 
                         aws_access_key_id=AWS_KEY_ID, 
                         aws_secret_access_key=AWS_SECRET)

df_list = [] 
request_files = [{'ETag': '"4a6628ab33eec7eed7fb0f339913c56a"',
  'Key': '2019_feb_1_gid_requests',
  'LastModified': datetime.datetime(2019, 12, 16, 0, 53, 52, 847000, tzinfo=tzlocal()),
  'Owner': {'DisplayName': 'webfile',
   'ID': '75aa57f09aa0c8caeab4f8c24e99d10f8e7faeebf76c078efc7c6caea54ba06a'},
  'Size': 104628,
  'StorageClass': 'STANDARD'},
 {'ETag': '"4a6628ab33eec7eed7fb0f339913c56a"',
  'Key': '2019_feb_2_gid_requests',
  'LastModified': datetime.datetime(2019, 12, 16, 0, 53, 52, 853000, tzinfo=tzlocal()),
  'Owner': {'DisplayName': 'webfile',
   'ID': '75aa57f09aa0c8caeab4f8c24e99d10f8e7faeebf76c078efc7c6caea54ba06a'},
  'Size': 104628,
  'StorageClass': 'STANDARD'},
 {'ETag': '"4a6628ab33eec7eed7fb0f339913c56a"',
  'Key': '2019_feb_3_gid_requests',
  'LastModified': datetime.datetime(2019, 12, 16, 0, 53, 52, 858000, tzinfo=tzlocal()),
  'Owner': {'DisplayName': 'webfile',
   'ID': '75aa57f09aa0c8caeab4f8c24e99d10f8e7faeebf76c078efc7c6caea54ba06a'},
  'Size': 104628,
  'StorageClass': 'STANDARD'},
 {'ETag': '"4a6628ab33eec7eed7fb0f339913c56a"',
  'Key': '2019_feb_4_gid_requests',
  'LastModified': datetime.datetime(2019, 12, 16, 0, 53, 52, 862000, tzinfo=tzlocal()),
  'Owner': {'DisplayName': 'webfile',
   'ID': '75aa57f09aa0c8caeab4f8c24e99d10f8e7faeebf76c078efc7c6caea54ba06a'},
  'Size': 104628,
  'StorageClass': 'STANDARD'}]

# Load each object from s3
for file in request_files:
    s3_day_reqs = s3.get_object(Bucket='gid-requests', 
                                Key=file['Key'])
    # Read the DataFrame into pandas, append it to the list
    day_reqs = pd.read_csv(s3_day_reqs['Body'])
    df_list.append(day_reqs)

# Concatenate all the DataFrames in the list
all_reqs = pd.concat(df_list)

# Preview the DataFrame
all_reqs.head()


#    service_request_id  ...                                 public_description
# 0             2553572  ...                           72hr plus tire violation
# 1             2553573  ...            Graffiti Reported at 3927 El Cajon Blvd
# 2             2553570  ...                                       Missed trash
# 3             2553568  ...  ALL 4 STREET LIGHTS ON THE SIGNAL STANDARDS AR...
# 4             2553565  ...                                                NaN

# [5 rows x 18 columns]