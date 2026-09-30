"""
deep-ml #309 Product Rule for Derivatives (Medium, Machine Learning)
Суть: найти коэффициенты производной произведения полиномов.
Статус: сдана 27-09-26.
"""


import numpy as np


def _poly_der(c):
    """Коэффициенты производной: d_j = (j+1) * c[j+1]"""
    c = np.asarray(c, float)
    return c[1:] * np.arange(1, len(c))     # cрезается 1-й коэффициент, производная которого равна 0, затем np.arange 
                                            # формирует степени от 1 до len(c) не включительно. Константа -> пустой массив
def _mul(a, b):
    """Произведение многочленов (пустой массив = нулевой многочлен)"""
    if a.size == 0 or b.size == 0:
        return np.zeros(max(a.size + b.size - 1, 1))    # возращается массив из нулей
    return np.convolve(a, b,)   # свёрточное произведение коэффициентов, где a.size, b.size = N, M.
                                # Для n-й позиции итогового массива формула такая:
                                # sum(a[m] * b[n-m]); m = max(0, n-M+1), ..., min(N-1, n); n = 0, ..., N+M-2

def product_rule_derivative(f_coeffs: list, g_coeffs: list):
    f = np.asarray(f_coeffs, float)
    g = np.asarray(g_coeffs, float)
    res = _mul(_poly_der(f), g) + _mul(f, _poly_der(g))
    return np.round(res, 4)


print(product_rule_derivative([1, 2], [3, 4]))