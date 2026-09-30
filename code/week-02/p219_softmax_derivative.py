import numpy as np

def softmax_derivative(x: list[float]) -> list[list[float]]:
    z = np.asarray(x, dtype=float)
    s = np.exp(z - np.max(z))
    s /= s.sum()
    return (np.diag(s) - np.outer(s, s)).tolist()