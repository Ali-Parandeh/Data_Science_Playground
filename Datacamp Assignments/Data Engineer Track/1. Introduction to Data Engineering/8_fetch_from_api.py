import requests

# Fetch the Hackernews post
resp = requests.get("https://hacker-news.firebaseio.com/v0/item/16222426.json")
# <Response [200]>

# Print the response parsed as JSON
print(resp.json())
# {'by': 'neis', 'descendants': 0, 'id': 16222426, 'score': 17, 'time': 1516800333, 'title': 'Duolingo-Style Learning for Data Science: DataCamp for Mobile', 'type': 'story', 'url': 'https://medium.com/datacamp/duolingo-style-learning-for-data-science-datacamp-for-mobile-3861d1bc02df'}


# Assign the score of the test to post_score
post_score = resp.json()['score']
print(post_score) #  17