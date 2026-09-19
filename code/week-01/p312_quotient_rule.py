"""
deep-ml #312 Quotient Rule for Derivatives (Medium, Calculus)
Суть: поиск производной от частного двух полиномов.
Статус: сдана 18-09-26.
"""


import numpy as np


def _poly_val(c, x):
    n = len(c)
    val = 0

    for i in range(n):
        val += c[i] * x**(n-1-i)
    return val

def _poly_der(c, x):
    n = len(c)
    der = 0

    for i in range(n-1):
        der += (n-1-i) * c[i] * x**(n-2-i)
    return der
 
def quotient_rule_derivative(g_coeffs: list, h_coeffs: list, x: float) -> float:
    """
    Compute the derivative of f(x) = g(x)/h(x) at point x using the quotient rule.
    
    Args:
        g_coeffs: Coefficients of numerator polynomial in descending order
        h_coeffs: Coefficients of denominator polynomial in descending order
        x: Point at which to evaluate the derivative
        
    Returns:
        The derivative value f'(x)
    """
    g, h = np.array(g_coeffs, float), np.array(h_coeffs, float)
    return ( _poly_der(g, x) * _poly_val(h, x)
           - _poly_val(g, x) * _poly_der(h, x) ) / _poly_val(h, x)**2


print(quotient_rule_derivative([1, 0, 1], [1, 2], 2))
