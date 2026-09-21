"""
deep-ml #81 Poisson Distribution Probability Calculator (easy, probability)
Суть: Функция подсчета вероятности распределения Пауссона
Статус: сдана 19-09-26.
"""

import math

def poisson_probability(k, lam):
	"""
	Calculate the probability of observing exactly k events in a fixed interval,
	given the mean rate of events lam, using the Poisson distribution formula.
	:param k: Number of events (non-negative integer)
	:param lam: The average rate (mean) of occurrences in a fixed interval
	"""
	val = (lam**k * math.exp(-lam))/math.factorial(k)
	return round(val,5)