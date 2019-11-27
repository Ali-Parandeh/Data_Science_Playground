'''
In [3]: survey_data['Part2EndTime'].head(1)
Out[3]: 
0    03292016 21:27:25
Name: Part2EndTime, dtype: object
'''

pd.to_datetime(survey_data['Part2EndTime'], format='%m%d%Y %H:%M:%S').head(1)

'''
0   2016-03-29 21:27:25
Name: Part2EndTime, dtype: datetime64[ns]
'''


'''
In [10]: survey_data['Part2EndTime'].head(1)
Out[10]: 
0    03292016 21:27:25
Name: Part2EndTime, dtype: object
'''


# Parse datetimes and assign result back to Part2EndTime
survey_data["Part2EndTime"] = pd.to_datetime(survey_data["Part2EndTime"], 
                                             format="%m%d%Y %H:%M:%S")

# Print first few values of Part2EndTime
print(survey_data["Part2EndTime"].head())

'''
<script.py> output:
    0   2016-03-29 21:27:25
    1   2016-03-29 21:29:10
    2   2016-03-29 21:28:21
    3   2016-03-29 21:30:51
    4   2016-03-29 21:31:54
    Name: Part2EndTime, dtype: datetime64[ns]
'''