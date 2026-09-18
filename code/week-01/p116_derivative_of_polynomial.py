"""
deep-ml #116 Derivative of a Polynomial (easy, Calculus)
Суть: реализовать степенное правило для полинома по коэффициентам.
Статус: сдана 2026-09-18.
"""

def poly_term_derivative(c: float, x: float, n: float) -> float:
    der = c * n * x**(n-1)
    return der