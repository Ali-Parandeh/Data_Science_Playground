# Load file, with Part1StartTime parsed as datetime data
survey_data = pd.read_excel("fcc_survey.xlsx",
                            parse_dates = ['Part1StartTime'])

# Print first few values of Part1StartTime
print(survey_data.Part1StartTime.head())

'''
<script.py> output:
    0   2016-03-29 21:23:13
    1   2016-03-29 21:24:59
    2   2016-03-29 21:25:37
    3   2016-03-29 21:21:37
    4   2016-03-29 21:26:22
    Name: Part1StartTime, dtype: datetime64[ns]
'''

'''
pandas can automatically parse many common date and time formats. 
It can even parse standalone times, without dates, 
but the parsed times will have the date the code was run.
'''