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

    # Делаем правильные срезы для поиска 25-го и 75-го процентилей
    if n % 2 != 0:
        left_data = data[0:mid+1]   # Включаем медиану в левую часть
        right_data = data[mid:n]    # Включаем медиану в правую часть
    else:
        left_data = data[0:mid]     # Делим ровно пополам
        right_data = data[mid:n]

    # 25th percentile
    left_mid = left_data.size // 2
    perc_25 = left_data[left_mid] if n % 2 != 0 else (left_data[left_mid] + left_data[left_mid - 1]) / 2

    # 75th percentile
    right_mid = right_data.size // 2
    perc_75 = right_data[right_mid] if n % 2 != 0 else (right_data[right_mid] + right_data[right_mid - 1]) / 2

    # IQR
    iqr = perc_75 - perc_25

    stats_dict = {
                'mean': mean, 'median': median, 'mode': mode, 
                'variance': var, 'standard_deviation': std, 
                '25th_percentile': perc_25, '50th_percentile': median, 
                '75th_percentile': perc_75, 'interquartile_range': iqr
    }

    return stats_dict


print(descriptive_statistics([1, 2, 4, 4, 4, 4, 5, 6]))