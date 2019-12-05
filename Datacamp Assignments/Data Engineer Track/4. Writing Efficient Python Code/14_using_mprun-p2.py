def calc_bmi_arrays(sample_indices, hts, wts):

    # Gather sample heights and weights as arrays
    s_hts = hts[sample_indices]
    s_wts = wts[sample_indices]

    # Convert heights from cm to m and square with broadcasting
    s_hts_m_sqr = (s_hts / 100) ** 2

    # Calculate BMIs as an array using broadcasting
    bmis = s_wts / s_hts_m_sqr

    return bmis

'''
Let's see if using a different approach to calculate the BMIs can save some memory. 
If you remember, each hero's height and weight is stored in a numpy array. 
That means you can use NumPy's handy array indexing capabilities and broadcasting to perform your calculations. 
'''



In [1]: load_ext memory_profiler

'''
The memory_profiler extension is already loaded. To reload it, use:
  %reload_ext memory_profiler
'''

In [2]: reload_ext memory_profiler

In [3]: from bmi_arrays import calc_bmi_arrays

In [4]: %mprun -f calc_bmi_arrays calc_bmi_arrays(sample_indices, hts, wts)
'''
Filename: /tmp/tmpfg_5zd1g/bmi_arrays.py

Line #    Mem usage    Increment   Line Contents
================================================
     1    118.4 MiB    118.4 MiB   def calc_bmi_arrays(sample_indices, hts, wts):
     2                             
     3                                 # Gather sample heights and weights as arrays
     4    118.4 MiB      0.0 MiB       s_hts = hts[sample_indices]
     5    118.4 MiB      0.0 MiB       s_wts = wts[sample_indices]
     6                             
     7                                 # Convert heights from cm to m and square with broadcasting
     8    118.4 MiB      0.0 MiB       s_hts_m_sqr = (s_hts / 100) ** 2
     9                             
    10                                 # Calculate BMIs as an array using broadcasting
    11    118.4 MiB      0.0 MiB       bmis = s_wts / s_hts_m_sqr
    12                             
    13    118.4 MiB      0.0 MiB       return bmis
'''


'''
By implementing an array approach, you were able to shave off a few MiBs. 
Although this isn't a colossal gain, it still decreases your code's overhead. 
If your input data grows over time, these small improvements could add up to some major efficiency gains.
'''