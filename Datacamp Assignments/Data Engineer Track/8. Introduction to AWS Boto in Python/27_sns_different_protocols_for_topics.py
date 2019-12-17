# Get the topic name by using the 'Department' field in the contacts DataFrame.
# Use the topic name to create the critical and extreme TopicArns for a user's department.
# Subscribe the user's email address to the critical topic.
# Subscribe the user's phone number to the extreme topic.

import boto3

# Create boto3 client to S3
sns = boto3.client('sns', region_name='us-east-1', 
                         aws_access_key_id=AWS_KEY_ID, 
                         aws_secret_access_key=AWS_SECRET)

print(contacts)
#                 Name                      Email        Phone Department
# 0         John Smith                js@fake.com  11224567890      trash
# 1  Janessa Goldsmith            whoami@fake.com  11534567890    streets
# 2      Evelyn Monroe             Evely@fake.com  11234067890      water
# 3             Max Pe      masdfsx@maksimize.com  11234517890      water
# 4          Fanny Mae         fanndyma3@fake.com  11234597890      trash
# 5  Janessa Goldsmith      whddsfsdoami@fake.com  11534567890      water
# 6             Max Pe  msdfsdfsdax@maksimize.com  11234517890    streets

for index, user_row in contacts.iterrows():
      # Get topic names for the users's dept
  critical_tname = '{}_critical'.format(user_row['Department'])
  extreme_tname = '{}_extreme'.format(user_row['Department'])
  
  # Get or create the TopicArns for a user's department.
  critical_arn = sns.create_topic(Name=critical_tname)['TopicArn']
  extreme_arn = sns.create_topic(Name=extreme_tname)['TopicArn']
  
  # Subscribe each users email to the critical Topic
  sns.subscribe(TopicArn = critical_arn, 
                Protocol='email', Endpoint=user_row['Email'])
  # Subscribe each users phone number for the extreme Topic
  sns.subscribe(TopicArn = extreme_arn, 
                Protocol='sms', Endpoint=str(user_row['Phone']))