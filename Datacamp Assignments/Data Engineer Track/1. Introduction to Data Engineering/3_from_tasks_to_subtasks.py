# Function to apply a function over multiple cores
from multiprocess import Pool
import pandas as pd

@print_timing
def parallel_apply(apply_func, groups, nb_cores):
    with Pool(nb_cores) as p:
        results = p.map(apply_func, groups)
    return pd.concat(results)

# Parallel apply using 1 core
parallel_apply(take_mean_age, athlete_events.groupby('Year'), nb_cores = 1)

# Parallel apply using 2 cores
parallel_apply(take_mean_age, athlete_events.groupby('Year'), nb_cores =2 )

# Parallel apply using 4 cores
parallel_apply(take_mean_age, athlete_events.groupby('Year'), nb_cores =4 )

# <script.py> output:
#     Processing time: 929.0807247161865
#     Processing time: 623.8305568695068
#     Processing time: 323.3604431152344

# For educational purposes, we've used a little trick here to make sure the parallelized version runs faster. In reality, using parallel computing wouldn't make sense here since the computations are simple and the dataset is relatively small. Communication overhead costs the multiprocessing version its edge!

