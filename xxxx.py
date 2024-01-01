import numpy as np

# The following function sorts the np array `vsim` from highest to lowest and returns the sorted indices
def sort_indices(a):
    return np.argsort(a)[::-1]

vsim=np.array([0.1,0.2,0.3,0.4,0.5])
print(sort_indices(vsim))
print(vsim[sort_indices(vsim)])