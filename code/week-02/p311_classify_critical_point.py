import numpy as np


def classify_critical_point(hessian: np.ndarray, tol: float = 1e-10):
    eigvals = np.linalg.eigvalsh(hessian)
    if np.any(np.abs(eigvals) <= tol):
        return None
    elif np.all(eigvals > 0):
        return -1
    elif np.all(eigvals < 0):
        return 1
    return 0


if __name__ == '__main__':
    H = np.array([[2, 0], [0, 2]])
    print(classify_critical_point(H))