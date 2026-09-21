"""
deep-ml #168 Calculate Conditional Probability from Data (easy, probability)
Суть: подсчет условной вероятности.
Статус: сдана 19-09-26.
"""

def conditional_probability(data, x, y):
    """
    Returns the probability P(Y=y|X=x) from list of (X, Y) pairs.
    Args:
      data: List of (X, Y) tuples
      x: value of X to condition on
      y: value of Y to check
    Returns:
      float: conditional probability, rounded to 4 decimal places
    """
    y_x_count = data.count((x, y))
    x_count = sum(1 for item in data if item[0] == x)
    
    if x_count == 0:
      return 0
    return y_x_count / x_count