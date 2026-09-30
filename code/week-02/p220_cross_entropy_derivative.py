import numpy as np

def cross_entropy_derivative(logits: list[float], target: int) -> list[float]:
    z = np.asarray(logits, dtype=float)
    p = np.exp(z - np.max(z))
    p /= p.sum()
    y = np.zeros_like(p)
    y[target] = 1.0
    return (p - y).tolist()