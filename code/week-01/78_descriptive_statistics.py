"""
deep-ml #78 Descriptive Statistics Calculator (Easy, Statistics)
Суть: посчитать основные статистики.
Статус: сдана 22-09-26.
"""


import numpy as np
from collections import Counter

def descriptive_statistics(data: list | np.ndarray) -> dict:
    """
    Calculate various descriptive statistics metrics for a given dataset.
    
    Args:
        data: List or numpy array of numerical values
    
    Returns:
        Dictionary containing mean, median, mode, variance, standard deviation,
        percentiles (25th, 50th, 75th), and interquartile range (IQR)
    """
    data = np.array(data)
    data = np.sort(data)
    n = data.size

    mean = np.sum(data) / n

    mid = n // 2

    median = data[mid] if n % 2 != 0 else (data[mid] + data[mid - 1]) / 2

    counts = Counter(data)
    max_count = max(counts.values())
    mode = [item for item, count in counts.items() if count == max_count][0]

    data_centered = data - mean
    var = np.dot(data_centered, data_centered) / (n)

    std = np.sqrt(var)

    # 25th percentile
    idx = (n - 1) * 0.25
    low = int(idx)
    high = min(low + 1, n - 1)
    d = idx - low

    perc_25 = data[low] + d * (data[high] - data[low])

    # 75th percentile
    idx = (n - 1) * 0.75
    low = int(idx)
    high = min(low + 1, n - 1)
    d = idx - low

    perc_75 = data[low] + d * (data[high] - data[low])

    # IQR
    iqr = perc_75 - perc_25

    stats_dict = {
                'mean': mean, 'median': median, 'mode': mode, 
                'variance': var, 'standard_deviation': std, 
                '25th_percentile': perc_25, '50th_percentile': median, 
                '75th_percentile': perc_75, 'interquartile_range': iqr
    }

    return stats_dict