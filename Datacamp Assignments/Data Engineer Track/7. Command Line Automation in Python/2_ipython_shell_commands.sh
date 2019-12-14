In [10]: list = !ls -h test_dir/*.csv

In [11]: list
# Out[11]: 
# ['test_dir/file_0.csv',
#  'test_dir/file_2.csv',
#  'test_dir/file_4.csv',
#  'test_dir/file_6.csv',
#  'test_dir/file_8.csv']

In [12]: len(list)
# Out[12]: 5