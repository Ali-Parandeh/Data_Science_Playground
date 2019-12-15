# Does it even exist?

# Your a social media company with a huge problem. Your NoSQL database 
# cluster was upgraded to 1.0.0-beta because it had some really cool new features. 
# Around this same time files started disappearing in production and social media 
# posts were suddenly vanishing. It turns out the beta version of the database was 
# actually deleting data between cluster nodes, not syncing data. Even worse, 
# the backups were never tested and the same backup from a year previous was 
# being run over and over again. You have a list of all social media posts 
# that should exist in production, and you need to write a script that 
# audits which files actually exist.

# Write a script using pathlib that validates if a list of files exists 
# on disk. Remember you can explore pathlib.Path in IPython.

# 1. Read in a posts_index.txt file to find paths.
# 2. Create pathlib.Path objects and use .exists() to check if the path is valid.
# 3. Use post.strip() to clean up the output of path you pass to pathlib.Post.


import pathlib

# Read the index of social media posts
with open("posts_index.txt") as posts:
  for post in posts.readlines():
    # Create a pathlib object
    path = pathlib.Path(post.strip())
    
    # Check if the social media post still exists on disk
    if path.exists():
      print(f"Found active post: {post}")
    else:
      print(f"Post is missing: {post}")

# <script.py> output:
#     Found active post: socialposts/2019/june/post1.txt
    
#     Post is missing: socialposts/2019/june/post2.txt
    
#     Found active post: socialposts/2019/june/post3.txt
    
#     Found active post: socialposts/2019/june/post4.txt
    
#     Post is missing: socialposts/2019/june/post5.txt
    
#     Post is missing: socialposts/2019/june/post6.txt
    
#     Post is missing: socialposts/2019/june/post7.txt
    
#     Post is missing: socialposts/2019/june/post8.txt
    
#     Found active post: socialposts/2019/june/post9.txt
    
#     Post is missing: socialposts/2019/june/post10.txt


# You found out which posts still exists! You used the pathlib module 
# to create path objects and then used the exists method to validate each path.