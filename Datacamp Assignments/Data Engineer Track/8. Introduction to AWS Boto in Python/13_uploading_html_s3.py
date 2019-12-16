# Upload an HTML file to S3

# When the Streets Operations manager heard of what Sam has been 
# working on, he asked her to build him a dashboard of Get It Done requests.

# He wants to use the dashboard to staff and schedule his team accordingly.

# Sam generated a nice dashboard html file with the Python bokeh charting library:

# She wants to serve it as a website, providing an interactive dashboard to members of Streets Operations.

# Letting S3 serve the dashboard as a site lets her write a 
# script that continuously updates the generated HTML file and 
# keeps the Streets Operations team updated on the latest requests.

# She has already initialized the boto3 S3 client and assigned it to the s3 variable.


import boto3

# Create boto3 client to S3
s3 = boto3.client('s3', region_name='us-east-1', 
                         aws_access_key_id=AWS_KEY_ID, 
                         aws_secret_access_key=AWS_SECRET)
                         
# Upload the lines.html file to S3
s3.upload_file(Filename='lines.html', 
               # Set the bucket name
               Bucket='datacamp-public', Key='index.html',
               # Configure uploaded file
               ExtraArgs = {
                 # Set proper content type
                 'ContentType':'text/html',
                 # Set proper ACL
                 'ACL': 'public-read'})

# Print the S3 Public Object URL for the new file.
print("http://{}.s3.amazonaws.com/{}".format('datacamp-public', 'index.html'))

# <script.py> output:
#     http://datacamp-public.s3.amazonaws.com/index.html