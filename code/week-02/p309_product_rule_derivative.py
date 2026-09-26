import numpy as np


def _poly_der(c):
    n = len(c)
    c_der = 0

    for i in range(-1, 0):
        c_der += ((n-2-i) * c[i]) # * x**(n-2-i)
    return c_der
 

def product_rule_derivative(f_coeffs: list, g_coeffs: list) -> list:
    """
    Compute the derivative of the product of two polynomials.
    
    Args:
        f_coeffs: Coefficients of polynomial f, where f_coeffs[i] is the coefficient of x^i
        g_coeffs: Coefficients of polynomial g, where g_coeffs[i] is the coefficient of x^i
    
    Returns:
        Coefficients of (f*g)' as a list of floats rounded to 4 decimal places
    """
    f, g = np.array(f_coeffs, float), np.array(g_coeffs, float)
    print(_poly_der(f))
    print(_poly_der(g))
    print(_poly_der(f) * np.asarray(g_coeffs))
    print(np.asarray(f_coeffs) * _poly_der(g))
    return ( _poly_der(f) * np.asarray(g_coeffs)
           + np.asarray(f_coeffs) * _poly_der(g))



print(product_rule_derivative(f_coeffs=[1, 2], g_coeffs=[3, 4, 1])) # 1 + 2x -> 2
                                                                # 3 + 4x -> 4
                                                                 # der_f * val_g = 