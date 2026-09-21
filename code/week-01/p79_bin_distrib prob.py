"""
deep-ml #79 Binomial Distribution Probability (easy, probability)
Суть: функция подсчета вероятности биномиального распределения.
Статус: сдана 19-09-26.
"""

import math

def binomial_probability(n: int, k: int, p: float) -> float:
    """
    Calculate the probability of exactly k successes in n Bernoulli trials.
    
    Args:
        n: Total number of trials
        k: Number of successes
        p: Probability of success on each trial
    
    Returns:
        Probability of k successes
    """
    comb = math.comb(n, k)
    st = p**k
    ft = (1-p)**(n-k)
    res = comb * st * ft
    return res