"""
deep-ml #184 Empirical Probability Mass Function (PMF) (Easy, Probability & Statistics)
Суть: посчитать мат ожидание и дисперсию .
Статус: сдано 21-09-26.
"""


import numpy as np


def empirical_pmf(samples):
    """
    Given an iterable of integer samples, return a list of (value, probability)
    pairs sorted by value ascending.
    """
    sample_set = set(samples)
    samples = np.array(samples)
    n = len(samples)
    probs = [(val, np.sum(samples == val) / n) for val in sample_set]
    return probs