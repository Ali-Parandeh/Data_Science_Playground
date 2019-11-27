# Load file with Yes as a True value and No as a False value
survey_subset = pd.read_excel("fcc_survey_yn_data.xlsx",
                              dtype={"HasDebt": bool,
                              "AttendedBootCampYesNo": bool},
                              true_values = ['Yes'],
                              false_values = ['No'])

# View the data
print(survey_subset.head())

'''
<script.py> output:
                                   ID.x  AttendedBootCampYesNo  HasDebt  HasFinancialDependents  HasHomeMortgage  HasStudentDebt
    0  cef35615d61b202f1dc794ef2746df14                  False     True                     1.0              0.0             1.0
    1  323e5a113644d18185c743c241407754                  False    False                     0.0              NaN             NaN
    2  b29a1027e5cd062e654a63764157461d                  False    False                     0.0              NaN             NaN
    3  04a11e4bcb573a1261eb0d9948d32637                  False     True                     0.0              0.0             1.0
    4  9368291c93d5d5f5c8cdb1a575e18bec                  False     True                     0.0              0.0             0.0
'''

'''
Building a data pipeline that sets Boolean dtypes and uses custom true 
and false values requires being very familiar with the data. It's a good idea to import the data as-is and explore it before doing so.
'''