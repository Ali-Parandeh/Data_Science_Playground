# For each row in the DataFrame, detect the dominant language.
# Assign the first selected language to the 'lang' column.
# Count the total number of posts in Spanish.

import boto3

# Create boto3 client to comprehend
comprehend = boto3.client('comprehend', region_name='us-east-1', 
                         aws_access_key_id=AWS_KEY_ID, 
                         aws_secret_access_key=AWS_SECRET)

# For each dataframe row
for index, row in dumping_df.iterrows():
    # Get the public description field
    description =dumping_df.loc[index, 'public_description']
    if description != '':
        # Detect language in the field content
        resp = comprehend.detect_dominant_language(Text=description)
        
        # resp
        # {'Languages': [{'LanguageCode': 'en', 'Score': 0.9935020208358765}],
        #  'ResponseMetadata': {'HTTPHeaders': {'content-length': '64',
        #    'content-type': 'application/x-amz-json-1.1',
        #    'date': 'Tue, 18 Jun 2019 22:26:02 GMT',
        #    'x-amzn-requestid': '0dd39064-9218-11e9-954e-ed8a7be44183'},
        #   'HTTPStatusCode': 200,
        #   'RequestId': '0dd39064-9218-11e9-954e-ed8a7be44183',
        #   'RetryAttempts': 0}}
        # Assign the top choice language to the lang column.

        dumping_df.loc[index, 'lang'] = resp['Languages'][0]['LanguageCode']
        
# Count the total number of spanish posts
spanish_post_ct = len(dumping_df[dumping_df.lang == 'es'])
# Print the result
print("{} posts in Spanish".format(spanish_post_ct))


# <script.py> output:
#     9 posts in Spanish