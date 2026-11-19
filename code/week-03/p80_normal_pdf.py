import math

def normal_pdf(x, mean, std_dev):
    """
    Calculate the probability density function (PDF) of the normal distribution.
    :param x: The value at which the PDF is evaluated.
    :param mean: The mean (μ) of the distribution.
    :param std_dev: The standard deviation (σ) of the distribution.
    """
    var = std_dev ** 2
    val = 1/math.sqrt(2 * math.pi * var) * math.e ** (-1 * (x - mean) ** 2 / (2 * var))
    return round(val,5)

if __name__ == '__main__':
    print(normal_pdf(0, 0, 1))