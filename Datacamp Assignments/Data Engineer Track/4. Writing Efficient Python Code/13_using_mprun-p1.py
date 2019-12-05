def calc_bmi_lists(sample_indices, hts, wts):

    # Gather sample heights and weights as lists
    s_hts = [hts[i] for i in sample_indices]
    s_wts = [wts[i] for i in sample_indices]

    # Convert heights from cm to m and square with list comprehension
    s_hts_m_sqr = [(ht / 100) ** 2 for ht in s_hts]

    # Calculate BMIs as a list with list comprehension
    bmis = [s_wts[i] / s_hts_m_sqr[i] for i in range(len(sample_indices))]

    return bmis


In [1]: %load_ext memory_profiler

In [2]: from bmi_lists import calc_bmi_lists

In [3]: %mprun -f calc_bmi_lists calc_bmi_lists(sample_indices, hts, wts)

'''
Filename: /tmp/tmpd7vcofqn/bmi_lists.py

Line #    Mem usage    Increment   Line Contents
================================================
     1    116.1 MiB    116.1 MiB   def calc_bmi_lists(sample_indices, hts, wts):
     2                             
     3                                 # Gather sample heights and weights as lists
     4    116.1 MiB      0.0 MiB       s_hts = [hts[i] for i in sample_indices]
     5    116.1 MiB      0.0 MiB       s_wts = [wts[i] for i in sample_indices]
     6                             
     7                                 # Convert heights from cm to m and square with list comprehension
     8    116.1 MiB      0.0 MiB       s_hts_m_sqr = [(ht / 100) ** 2 for ht in s_hts]
     9                             
    10                                 # Calculate BMIs as a list with list comprehension
    11    116.1 MiB      0.0 MiB       bmis = [s_wts[i] / s_hts_m_sqr[i] for i in range(len(sample_indices))]
    12                             
    13    116.1 MiB      0.0 MiB       return bmis


The total sum of the memory allocated for these four lines should be greater than 0.0 MiB. 
If you run %mprun multiple times within your session, you may notice that the Increment column 
reports 0.0 MiB for all lines of code. This is due to a limitation with the magic command (not your fault). 
If you encounter this issue, restart your session and re-run all the 
necessary steps for using %mprun—but this time, only use %mprun once to answer the question.
'''


'''
Using a list comprehension approach allocates anywhere from 0.1 MiB to 2 MiB of memory to calculate your BMIs.

If you run %mprun multiple times within your session, you may notice that the Increment column reports 0.0 MiB for all lines of code. 
This is due to a limitation with the magic command. After running %mprun once, the memory allocation analyzed previously is taken into 
account for all consecutive runs and %mprun will start from the place the first run left off.

Now that we've profiled the calc_bmi_lists() function, let's see if you can do better with a different approach.
'''