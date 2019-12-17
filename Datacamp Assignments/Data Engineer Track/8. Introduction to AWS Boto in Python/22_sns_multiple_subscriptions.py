# For each element in the Email column of contacts, create a subscription to the 'streets_critical' Topic.
# List subscriptions for the 'streets_critical' Topic and convert them to a DataFrame.
# Preview the DataFrame.

import boto3

# Create boto3 client to S3
sns = boto3.client('sns', region_name='us-east-1', 
                         aws_access_key_id=AWS_KEY_ID, 
                         aws_secret_access_key=AWS_SECRET)

str_critical_arn = 'arn:aws:sns:us-east-1:123456789012:streets_critical'

print(contacts)
#                 Name                      Email        Phone Department
# 0         John Smith                js@fake.com  11224567890      trash
# 1  Janessa Goldsmith            whoami@fake.com  11534567890    streets
# 2      Evelyn Monroe             Evely@fake.com  11234067890      water
# 3             Max Pe      masdfsx@maksimize.com  11234517890      water
# 4          Fanny Mae         fanndyma3@fake.com  11234597890      trash
# 5  Janessa Goldsmith      whddsfsdoami@fake.com  11534567890      water
# 6             Max Pe  msdfsdfsdax@maksimize.com  11234517890    streets

# For each email in contacts, create subscription to street_critical
for email in contacts['Email']:
    sns.subscribe(TopicArn = str_critical_arn,
                # Set channel and recipient
                Protocol = 'email',
                Endpoint = email)

# List subscriptions for streets_critical topic, convert to DataFrame
response = sns.list_subscriptions_by_topic(
  TopicArn = str_critical_arn)
subs = pd.DataFrame(response['Subscriptions'])

# Preview the DataFrame
subs.head()

#                 Endpoint  ...                                           TopicArn
# 0            js@fake.com  ...  arn:aws:sns:us-east-1:123456789012:streets_cri...
# 1        whoami@fake.com  ...  arn:aws:sns:us-east-1:123456789012:streets_cri...
# 2         Evely@fake.com  ...  arn:aws:sns:us-east-1:123456789012:streets_cri...
# 3  masdfsx@maksimize.com  ...  arn:aws:sns:us-east-1:123456789012:streets_cri...
# 4     fanndyma3@fake.com  ...  arn:aws:sns:us-east-1:123456789012:streets_cri...

# [5 rows x 5 columns]