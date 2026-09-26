"""
deep-ml #1130 Generate Normal Samples and Compute Histogram Counts (Easy, Statistics)
Суть: генерация случайных чисел из нормального распределения.
Статус: сдана 25-09-26.
"""


import numpy as np


def fn(seed, mean, std, n, bins): 
    # seed - для воспроизводимости (фиксации) случайных чисел; mean, std, n - параметры нормального распределения
    np.random.seed(seed)
    
    # Генерируем n случайных чисел (сэмплов)
    samples = np.random.normal(mean, std, n)
    
    # Если bins - это массив/список конкретных границ, приводим его элементы к типу float
    if isinstance(bins, (list, tuple, np.ndarray)):
        bins = np.asarray(bins).astype(float)
        
    # counts - сколько значений попало в каждый интервал. edges - массив границ этих интервалов (их всегда на 1 больше, чем интервалов)
    counts, edges = np.histogram(samples, bins=bins) 
    
    return counts.tolist(), edges.tolist()