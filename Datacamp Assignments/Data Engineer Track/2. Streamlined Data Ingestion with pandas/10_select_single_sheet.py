# Create df from second worksheet by referencing its position
responses_2017 = pd.read_excel("fcc_survey.xlsx",sheet_name = 1)

# or

responses_2017 = pd.read_excel("fcc_survey.xlsx", sheet_name = '2017')
                               
'''
Although it's possible to get multiple spreadsheets in an Excel file with one call to read_excel(), 
it can make more sense to use multiple calls if sheets contain very different data or layouts. 
That way, you can customize other arguments for each sheet
'''

# Graph where people would like to get a developer job
job_prefs = responses_2017.groupby("JobPref").JobPref.count()
job_prefs.plot.barh()
plt.show()