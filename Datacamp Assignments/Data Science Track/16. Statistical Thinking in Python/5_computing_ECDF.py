# Computing ECDFs

# ECDFs are among the most important plots in statistical analysis.

import numpy as np

def ecdf(data):
    """Compute ECDF for a one-dimensional array of measurements."""
    # Number of data points: n
    n = len(data.data)

    # x-data for the ECDF: x
    x = np.sort(data.data)

    # y-data for the ECDF: y
    y = np.arange(1, n+1) / n

    return x, y
