# For every DataFrame row, detect the dominant language.
# Use the detected language to determine the sentiment of the description.
# Group the DataFrame by the 'sentiment' and 'lang' columns in that order.

import boto3

# Create boto3 client to comprehend
comprehend = boto3.client('comprehend', region_name='us-east-1', 
                         aws_access_key_id=AWS_KEY_ID, 
                         aws_secret_access_key=AWS_SECRET)


for index, row in scooter_requests.iterrows():
      	# For every DataFrame row
    desc = scooter_requests.loc[index, 'public_description']
    if desc != '':
      	# Detect the dominant language
        resp = comprehend.detect_dominant_language(Text=desc)
        lang_code = resp['Languages'][0]['LanguageCode']
        scooter_requests.loc[index, 'lang'] = lang_code
        # Use the detected language to determine sentiment
        scooter_requests.loc[index, 'sentiment'] = comprehend.detect_sentiment(
          Text=desc, 
          LanguageCode=lang_code)['Sentiment']
# Perform a count of sentiment by group.
counts = scooter_requests.groupby(['sentiment', 'lang']).count()
counts.head()


#                 service_request_id  service_name  public_description
# sentiment lang                                                      
# MIXED     en    2                   2             2                 
#           tl    8                   8             8                 
#           vi    4                   4             4                 
# NEGATIVE  en    1                   1             1                 
#           es    2                   2             2