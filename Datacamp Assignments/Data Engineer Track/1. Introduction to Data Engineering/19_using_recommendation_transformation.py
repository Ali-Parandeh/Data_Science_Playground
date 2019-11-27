''' 
Decision rules for producing recommendations:

1. Use technology a student has rated the most.
2. Exclude courses a student has already rated.
3. Find the three top-rated courses from eligible courses.
 '''

# Complete the transformation function
def transform_recommendations(avg_course_ratings, courses_to_recommend):
    # Merge both DataFrames
    merged = courses_to_recommend.merge(avg_course_ratings) 
    # Sort values by rating and group by user_id
    grouped = merged.sort_values("rating", ascending = False).groupby('user_id')
    # Produce the top 3 values and sort by user_id
    recommendations = grouped.head(3).sort_values("user_id").reset_index()
    final_recommendations = recommendations[["user_id", "course_id","rating"]]
    # Return final recommendations
    return final_recommendations

# Use the function with the predefined DataFrame objects
recommendations = transform_recommendations(avg_course_ratings, courses_to_recommend)



''' 
In [2]: avg_course_ratings.head(1)
Out[2]: 
   course_id  rating
0         46     4.8

In [3]: courses_to_recommend.head(1)
Out[3]: 
   user_id  course_id
0        1         64

In [5]: courses_to_recommend.merge(avg_course_ratings).head(1)
Out[5]: 
   user_id  course_id    rating
0        1         64  4.532075


In [11]: recommendations.head(10)
Out[11]: 
   user_id  course_id    rating
0        1         24  4.653061
1        1         23  4.800000
2        1         46  4.800000
3        2         46  4.800000
4        2         24  4.653061
5        2         23  4.800000
6        3         46  4.800000
7        3         23  4.800000
8        3         24  4.653061
9        4         70  4.428144
 '''
