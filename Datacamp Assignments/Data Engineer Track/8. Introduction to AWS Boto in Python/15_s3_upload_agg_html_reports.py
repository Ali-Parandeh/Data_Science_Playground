# Upload aggregated reports for February

# In the last exercise, Sam downloaded the files 
# for the month from the raw data bucket.

# Then she combined them all into one DataFrame that 
# showcases all of the month's requests and requests type.

# She stored this DataFrame in the variable all_reqs 
# and used pandas's groupby functionality to count 
# requests by service name, generating a new DataFrame agg_df:

# service_name	count
# 0	72 Hour Violation	2910
# 1	Chain Link Fence Repair	90
# 2	Collections Truck Spill	30
# 3	Container Left Out	120
# 4	Dead Animal	360

# She has already created the boto3 S3 client in the s3 variable.

# Help her publish this month's request statistics.

# Write agg_df to CSV and HTML files, and upload them to S3 as public files.


import boto3

# Create boto3 client to S3
s3 = boto3.client('s3', region_name='us-east-1', 
                         aws_access_key_id=AWS_KEY_ID, 
                         aws_secret_access_key=AWS_SECRET)
                         

# Write agg_df to a CSV and HTML file with no border
agg_df.to_csv('./feb_final_report.csv')
agg_df.to_html('./feb_final_report.html', border=0)

# Upload the generated CSV to the gid-reports bucket
s3.upload_file(Filename='./feb_final_report.csv', 
	Key='2019/feb/final_report.html', Bucket='gid-reports',
    ExtraArgs = {'ACL': 'public-read'})

# Upload the generated HTML to the gid-reports bucket
s3.upload_file(Filename='./feb_final_report.html', 
	Key='2019/feb/final_report.html', Bucket='gid-reports',
    ExtraArgs = {'ContentType': 'text/html', 
                 'ACL': 'public-read'})

# You generated HTML and CSV, and uploaded them to S3. You also helped Sam upload the chart