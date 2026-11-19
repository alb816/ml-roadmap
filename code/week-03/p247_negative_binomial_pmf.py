import math

def negative_binomial_pmf(k: int, r: int, p: float) -> float:
    """
    Calculate the probability of observing exactly k failures
    before achieving r successes in independent Bernoulli trials.
    
    Args:
        k: Number of failures (non-negative integer)
        r: Number of successes required (positive integer)
        p: Probability of success on each trial (0 < p <= 1)
    
    Returns:
        Probability P(X = k) rounded to 5 decimal places
    """
    if k < 0 or r <= 0 or not (0 < p <= 1):
        return 0.0
    
    prob = math.comb(k + r - 1, k) * p ** r * (1 - p)**k

    return round(prob, 5)


if __name__ == '__main__':
    print(negative_binomial_pmf(3, 2, 0.5))