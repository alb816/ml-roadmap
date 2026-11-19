from math import comb

def hypergeometric_pmf(N: int, K: int, n: int, k: int) -> float:
    """
    Calculate the PMF of the hypergeometric distribution.
    
    Args:
        N: Total population size
        K: Number of success states in population
        n: Number of draws (without replacement)
        k: Number of observed successes
    
    Returns:
        float: P(X = k), rounded to 4 decimal places
    """
    if not(max(0, n - (N - K)) <= k <= min(K, n)):
           return 0.0

    prob = (comb(K, k) * comb(N - K, n - k)) / comb(N, n)

    return round(prob, 4)


if __name__ == '__main__':
    print(hypergeometric_pmf(52, 13, 5, 2))