import sqlalchemy

# Complete the connection URI
connection_uri = "postgresql://repl:password@localhost:5432/datacamp_application"
db_engine = sqlalchemy.create_engine(connection_uri)

# Get user with id 4387
user1 = pd.read_sql("SELECT * FROM rating WHERE user_id = 4387", db_engine)

''' 
Out[7]: 
    user_id  course_id  rating
0      4387          3       4 
'''

# Get user with id 18163
user2 = pd.read_sql("SELECT * FROM rating WHERE user_id = 18163", db_engine)

# Get user with id 8770
user3 = pd.read_sql("SELECT * FROM rating WHERE user_id = 8770", db_engine)

# Use the helper function to compare the 3 users
print_user_comparison(user1, user2, user3)


''' 
<script.py> output:
    Course id overlap between users:
    ================================
    User 1 and User 2 overlap: {32, 96, 36, 6, 7, 44, 95}
    User 1 and User 3 overlap: set()
    User 2 and User 3 overlap: set() 
    '''