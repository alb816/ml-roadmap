import numpy as np

def fn(seed, mean, std, n, bins):
    # return (counts, edges) as plain Python lists
    np.random.seed(seed)



print(fn(0, 0, 1, 5, [-3, -1, 1, 3]))