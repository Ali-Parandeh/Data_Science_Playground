$ paste seasonal/autumn.csv seasonal/winter.csv
# Date,Tooth      Date,Tooth
# 2017-01-05,canine       2017-01-03,bicuspid
# 2017-01-17,wisdom       2017-01-05,incisor
# 2017-01-18,canine       2017-01-21,wisdom
# 2017-02-01,molar        2017-02-05,molar
# 2017-02-22,bicuspid     2017-02-17,incisor
# 2017-03-10,canine       2017-02-25,bicuspid
# 2017-03-13,canine       2017-03-12,incisor
# 2017-04-30,incisor      2017-03-25,molar
# 2017-05-02,canine       2017-03-26,incisor
# 2017-05-10,canine       2017-04-04,canine
# 2017-05-19,bicuspid     2017-04-18,canine
# 2017-05-25,molar        2017-04-26,canine
# 2017-06-22,wisdom       2017-04-26,molar
# 2017-06-25,canine       2017-04-26,wisdom
# 2017-07-10,incisor      2017-04-27,canine
# 2017-07-10,wisdom       2017-05-08,molar
# 2017-07-20,incisor      2017-05-13,bicuspid
# 2017-07-21,bicuspid     2017-05-14,wisdom
# 2017-08-09,canine       2017-06-17,canine
# 2017-08-16,canine       2017-07-01,incisor
#         2017-07-17,canine
#         2017-08-10,incisor
#         2017-08-11,bicuspid
#         2017-08-11,wisdom
#         2017-08-13,canine

# What's wrong with the output from a data analysis point of view?

# Answer 
# The last few rows have the wrong number of columns.
# joining the lines with columns creates only one empty column at the start, not two.