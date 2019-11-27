# Load the data
survey_data = pd.read_excel("fcc_survey_subset.xlsx")

# Count NA values in each column
print(survey_data.isna().sum())


'''
<script.py> output:
    ID.x                        0
    HasDebt                     0
    HasFinancialDependents      7
    HasHomeMortgage           499
    HasStudentDebt            502
    dtype: int64
'''


# Set dtype to load appropriate column(s) as Boolean data
survey_data = pd.read_excel("fcc_survey_subset.xlsx",
                            dtype = {'HasDebt': bool})

# View financial burdens by Boolean group
print(survey_data.groupby('HasDebt').sum())


'''
<script.py> output:
             HasFinancialDependents  HasHomeMortgage  HasStudentDebt
    HasDebt                                                         
    False                     112.0              0.0             0.0
    True                      205.0            151.0           281.0

'''


'''
Modeling True/False data as Booleans can streamline some data manipulation functions and 
keep spurious summary statistics, like quartile values, from being calculated. 
If you want to make a column with NA values Boolean, you can load the data, impute missing values, then re-cast the column as Boolean.
'''