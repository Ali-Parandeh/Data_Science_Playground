# For every contact, send an ad-hoc SMS to the contact's phone number.
# The message sent should include the contact's name.

print(contacts)

#                 Name                      Email        Phone Department
# 0         John Smith                js@fake.com  11224567890      trash
# 1  Janessa Goldsmith            whoami@fake.com  11534567890    streets
# 2      Evelyn Monroe             Evely@fake.com  11234067890      water
# 3             Max Pe      masdfsx@maksimize.com  11234517890      water
# 4          Fanny Mae         fanndyma3@fake.com  11234597890      trash
# 5  Janessa Goldsmith      whddsfsdoami@fake.com  11534567890      water
# 6             Max Pe  msdfsdfsdax@maksimize.com  11234517890    streets

import boto3
streets_v_count = 125

# Create boto3 client to S3
sns = boto3.client('sns', region_name='us-east-1', 
                         aws_access_key_id=AWS_KEY_ID, 
                         aws_secret_access_key=AWS_SECRET)

# Loop through every row in contacts
for idx, row in contacts.iterrows():
    
    # Publish an ad-hoc sms to the user's phone number
    response = sns.publish(
        # Set the phone number
        PhoneNumber = str(row['Phone']),
        # The message should include the user's name
        Message = 'Hello {}'.format(row['Name'])
    )
   
    print(response)

# <script.py> output:
#     {'MessageId': '1d1e369b-9ec7-5341-a198-63e3749e4608', 'ResponseMetadata': 
#     {'RequestId': '7902d2b2-9081-5aab-aa5c-87ca7ad85fe2', 'HTTPStatusCode': 200, 'HTTPHeaders': 
#     {'x-amzn-requestid': '7902d2b2-9081-5aab-aa5c-87ca7ad85fe2', 'content-type': 
#     'text/xml', 'content-length': '294', 'date': 'Mon, 10 Jun 2019 23:30:33 GMT'}, 'RetryAttempts': 0}}
#     {'MessageId': '1d1e369b-9ec7-5341-a198-63e3749e4608', 'ResponseMetadata': 
#     {'RequestId': '7902d2b2-9081-5aab-aa5c-87ca7ad85fe2', 'HTTPStatusCode': 200, 'HTTPHeaders': 
#     {'x-amzn-requestid': '7902d2b2-9081-5aab-aa5c-87ca7ad85fe2', 'content-type': 
#     'text/xml', 'content-length': '294', 'date': 'Mon, 10 Jun 2019 23:30:33 GMT'}, 'RetryAttempts': 0}}
#     {'MessageId': '1d1e369b-9ec7-5341-a198-63e3749e4608', 'ResponseMetadata': 
#     {'RequestId': '7902d2b2-9081-5aab-aa5c-87ca7ad85fe2', 'HTTPStatusCode': 200, 'HTTPHeaders': 
#     {'x-amzn-requestid': '7902d2b2-9081-5aab-aa5c-87ca7ad85fe2', 'content-type': 
#     'text/xml', 'content-length': '294', 'date': 'Mon, 10 Jun 2019 23:30:33 GMT'}, 'RetryAttempts': 0}}
#     {'MessageId': '1d1e369b-9ec7-5341-a198-63e3749e4608', 'ResponseMetadata': 
#     {'RequestId': '7902d2b2-9081-5aab-aa5c-87ca7ad85fe2', 'HTTPStatusCode': 200, 'HTTPHeaders': 
#     {'x-amzn-requestid': '7902d2b2-9081-5aab-aa5c-87ca7ad85fe2', 'content-type': 
#     'text/xml', 'content-length': '294', 'date': 'Mon, 10 Jun 2019 23:30:33 GMT'}, 'RetryAttempts': 0}}
#     {'MessageId': '1d1e369b-9ec7-5341-a198-63e3749e4608', 'ResponseMetadata': 
#     {'RequestId': '7902d2b2-9081-5aab-aa5c-87ca7ad85fe2', 'HTTPStatusCode': 200, 'HTTPHeaders': 
#     {'x-amzn-requestid': '7902d2b2-9081-5aab-aa5c-87ca7ad85fe2', 'content-type': 
#     'text/xml', 'content-length': '294', 'date': 'Mon, 10 Jun 2019 23:30:33 GMT'}, 'RetryAttempts': 0}}
#     {'MessageId': '1d1e369b-9ec7-5341-a198-63e3749e4608', 'ResponseMetadata': 
#     {'RequestId': '7902d2b2-9081-5aab-aa5c-87ca7ad85fe2', 'HTTPStatusCode': 200, 'HTTPHeaders': 
#     {'x-amzn-requestid': '7902d2b2-9081-5aab-aa5c-87ca7ad85fe2', 'content-type': 
#     'text/xml', 'content-length': '294', 'date': 'Mon, 10 Jun 2019 23:30:33 GMT'}, 'RetryAttempts': 0}}
#     {'MessageId': '1d1e369b-9ec7-5341-a198-63e3749e4608', 'ResponseMetadata': 
#     {'RequestId': '7902d2b2-9081-5aab-aa5c-87ca7ad85fe2', 'HTTPStatusCode': 200, 'HTTPHeaders': 
#     {'x-amzn-requestid': '7902d2b2-9081-5aab-aa5c-87ca7ad85fe2', 'content-type': 
#     'text/xml', 'content-length': '294', 'date': 'Mon, 10 Jun 2019 23:30:33 GMT'}, 'RetryAttempts': 0}}
