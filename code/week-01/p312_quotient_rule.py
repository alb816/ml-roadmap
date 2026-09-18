"""
deep-ml #312 Quotient Rule for Derivatives (Medium, Calculus)
Суть: поиск производной от частного двух полиномов.
Статус: в процессе.
"""



import numpy as np

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
    # (g(x)/h(x))' = (g'(x)h(x) - g(x)h'(x))/(h(x))^2
    
    g_coeffs = np.array(g_coeffs)
    g_coeffs = g_coeffs[g_coeffs != 0]

    h_coeffs = np.array(h_coeffs)
    h_coeffs = h_coeffs[h_coeffs != 0]


    n_g = len(g_coeffs)
    n_h = len(h_coeffs)
    
    # der_g = n_g * g_coeffs[0] * x**n_g-1 + ...

    g_x = 0
    der_g = 0

    h_x = 0
    der_h = 0

    coeffs = np.concat((g_coeffs, h_coeffs))
    # print(coeffs)

    for i, coef in enumerate(coeffs):
        i += 1
        if i > n_g:
            print('h')
        else:
            der_g += (n_g - i - 1) * coef * x**(n_g-i-2)
            
        
    print(der_g)


quotient_rule_derivative([1, 0, 1], [1, 2], 2)
