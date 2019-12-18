# For each row in the DataFrame, translate it to English.
# Store the original language in the original_lang column.
# Store the new translation in the translated_desc column.

import boto3

# Create boto3 client to translate
translate = boto3.client('translate', region_name='us-east-1', 
                         aws_access_key_id=AWS_KEY_ID, 
                         aws_secret_access_key=AWS_SECRET)


Print(dumping_df.columns)
# Index(['service_request_id', 'service_name', 'public_description'], dtype='object')

for index, row in dumping_df.iterrows():
      	# Get the public_description into a variable
    description = dumping_df.loc[index, 'public_description']
    if description != '':
      	# Translate the public description
        resp = translate.translate_text(
            Text=description, 
            SourceLanguageCode='auto', TargetLanguageCode='en')
            
        # resp
        # {'ResponseMetadata': {'HTTPHeaders': {'cache-control': 'no-cache',
        # 'connection': 'keep-alive',
        # 'content-length': '89',
        # 'content-type': 'application/x-amz-json-1.1',
        # 'date': 'Wed, 19 Jun 2019 12:19:25 GMT',
        # 'x-amzn-requestid': '7a8b7fb0-928c-11e9-9b6e-b34a2c3e7e9d'},
        # 'HTTPStatusCode': 200,
        # 'RequestId': '7a8b7fb0-928c-11e9-9b6e-b34a2c3e7e9d',
        # 'RetryAttempts': 0},
        # 'SourceLanguageCode': 'en',
        # 'TargetLanguageCode': 'en',
        # 'TranslatedText': 'Homeless active camp litter erx'}

        # Store original language in original_lang column
        dumping_df.loc[index, 'original_lang'] = resp['SourceLanguageCode']
        # Store the translation in the translated_desc column
        dumping_df.loc[index, 'translated_desc'] = resp['TranslatedText']
# Preview the resulting DataFrame
dumping_df = dumping_df[['service_request_id', 'original_lang', 'translated_desc']]
dumping_df.head()

#    service_request_id original_lang                                    translated_desc
# 0               93494            es                            There is a lot of trash
# 1              101502            en  Couch, 4 chairs, mattress, carpet padding. thi...
# 2              101520           NaN                                                NaN
# 3              101576            en  On the South Side of Paradise Valley Road near...
# 4              101616            es                    There is a fridge on the street