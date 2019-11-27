# Create dict of columns to combine into new datetime column
datetime_cols = {"Part2Start": ['Part2StartDate', 'Part2StartTime']}


# Load file, supplying the dict to parse_dates
survey_data = pd.read_excel("fcc_survey_dts.xlsx",
                            parse_dates = datetime_cols)

# View summary statistics about Part2Start
print(survey_data.Part2Start.describe())

'''
<script.py> output:
    count                    1000
    unique                    985
    top       2016-03-30 01:29:27
    freq                        2
    first     2016-03-29 21:24:57
    last      2016-03-30 09:08:18
    Name: Part2Start, dtype: object
'''

'''
Note that the keys in a dictionary passed to parse_dates cannot be names of columns already in the data frame. 
Also, when combining columns to parse, their order in the list does not matter.
'''

'''
In [2]: pd.read_excel("fcc_survey_dts.xlsx")['Part2StartDate'].head(1)

Out[2]: 
0    2016-03-29
Name: Part2StartDate, dtype: object

'''
'''
In [3]: pd.read_excel("fcc_survey_dts.xlsx")['Part2StartTime'].head(1)

Out[3]: 
0    21:24:57
Name: Part2StartTime, dtype: object
'''