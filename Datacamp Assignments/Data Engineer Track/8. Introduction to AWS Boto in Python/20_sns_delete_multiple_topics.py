# Get the current list of topics
topics = sns.list_topics()['Topics']

for topic in topics:
  # For each topic, if it is not marked critical, delete it
  if "critical" not in topic['TopicArn']:
    sns.delete_topic(TopicArn=topic['TopicArn'])
    
# Print the list of remaining critical topics
print(sns.list_topics()['Topics'])

# <script.py> output:
#     [{'TopicArn': 'arn:aws:sns:us-east-1:123456789012:trash_critical'}, 
#     {'TopicArn': 'arn:aws:sns:us-east-1:123456789012:streets_critical'}, 
#     {'TopicArn': 'arn:aws:sns:us-east-1:123456789012:water_critical'}]