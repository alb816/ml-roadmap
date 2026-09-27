"""
deep-ml #215 Partial Derivatives of Multivariable Functions (Medium, Calculus)
Суть: найти частные производные.
Статус: сдана 27-09-26.
"""


import numpy as np


def compute_partial_derivatives(
    func_name: str, point: tuple[float, ...]
) -> tuple[float, ...]:
    """
    Compute partial derivatives of multivariable functions.

    Args:
            func_name: Function identifier
                    'poly2d': f(x,y) = x²y + xy²
                    'exp_sum': f(x,y) = e^(x+y)
                    'product_sin': f(x,y) = x·sin(y)
                    'poly3d': f(x,y,z) = x²y + yz²
                    'squared_error': f(x,y) = (x-y)²
            point: Point (x, y) or (x, y, z) at which to evaluate

    Returns:
            Tuple of partial derivatives (∂f/∂x, ∂f/∂y, ...) at point
    """
    x, y = point[0], point[1]
    gradient = np.zeros(2)

    if func_name == "poly2d":
        gradient[0] = 2 * x * y + y**2
        gradient[1] = x**2 + 2 * x * y
    elif func_name == "exp_sum":
        gradient[0] = np.e ** (x + y)
        gradient[1] = np.e ** (x + y)
    elif func_name == "product_sin":
        gradient[0] = np.sin(y)
        gradient[1] = x * np.cos(y)
    elif func_name == "poly3d":
        gradient = np.append(gradient, 0.0)
        z = point[2]
        gradient[0] = 2 * x * y
        gradient[1] = x**2 + z**2
        gradient[2] = 2 * y * z
    elif func_name == "squared_error":
        gradient[0] = 2 * (x - y) # * 1
        gradient[1] = 2 * (x - y) * -1
    return gradient
