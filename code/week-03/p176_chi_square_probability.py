import math

def chi_square_probability(x, k):
    """
    Calculate the probability density of x in a Chi-square distribution
    with k degrees of freedom.
    """
    if x < 0 or k <= 0:
        return 0.0

    if x == 0:
        if k > 2:
            return 0.0
        if k == 2:
            return 0.5
        if k < 2:
            return float('inf')

    probability = (1 / (2 ** (k / 2) * math.gamma(k / 2))) * x ** (k / 2 - 1) * math.e ** (-x / 2)
    
    return round(probability, 3)

if __name__ == '__main__':
    print(chi_square_probability(2, 2))