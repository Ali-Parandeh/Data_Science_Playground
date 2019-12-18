# Detect the sentiment of 'public_description' for every row.
# Store the result in the 'sentiment' column.

import boto3

# Create boto3 client to comprehend
comprehend = boto3.client('comprehend', region_name='us-east-1', 
                         aws_access_key_id=AWS_KEY_ID, 
                         aws_secret_access_key=AWS_SECRET)

for index, row in dumping_df.iterrows():
      	# Get the translated_desc into a variable
    description = dumping_df.loc[index, 'public_description']
    if description != '':
      	# Get the detect_sentiment response
        response = comprehend.detect_sentiment(
          Text=description, 
          LanguageCode='en')

        # response
        # {'ResponseMetadata': {'HTTPHeaders': {'content-length': '162',
        # 'content-type': 'application/x-amz-json-1.1',
        # 'date': 'Wed, 19 Jun 2019 12:26:19 GMT',
        # 'x-amzn-requestid': '70f7266a-928d-11e9-a344-d353a8b9fbf7'},
        # 'HTTPStatusCode': 200,
        # 'RequestId': '70f7266a-928d-11e9-a344-d353a8b9fbf7',
        # 'RetryAttempts': 0},
        # 'Sentiment': 'NEGATIVE',
        # 'SentimentScore': {'Mixed': 0.016489867120981216,
        # 'Negative': 0.19806478917598724,
        # 'Neutral': 0.6771729588508606,
        # 'Positive': 0.10827238112688065}}

        # Get the sentiment key value into sentiment column
        dumping_df.loc[index, 'sentiment'] = response['Sentiment']
# Preview the dataframe
dumping_df.head()

#    service_request_id  ... sentiment
# 0  93494               ...  POSITIVE
# 1  101502              ...  NEGATIVE
# 2  101520              ...  MIXED   
# 3  101576              ...  NEUTRAL 
# 4  101616              ...  NEGATIVE

# [5 rows x 4 columns]