course_data = extract_course_data(db_engines)

# Print out the number of missing values per column
print(course_data.isnull().sum())

# The transformation should fill in the missing values
def transform_fill_programming_language(course_data):
    imputed = course_data.fillna({"programming_language": "r"})
    return imputed

transformed = transform_fill_programming_language(course_data)

# Print out the number of missing values per column of transformed
print(transformed.isnull().sum())


''' 
<script.py> output:
    course_id               0
    title                   0
    description             0
    programming_language    3
    dtype: int64
    course_id               0
    title                   0
    description             0
    programming_language    0
    dtype: int64
 '''