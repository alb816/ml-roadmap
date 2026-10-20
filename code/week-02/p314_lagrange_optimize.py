import numpy as np


def lagrange_optimize(Q: np.ndarray, c: np.ndarray, a: np.ndarray, b: float) -> dict:
    """
    Solve constrained quadratic optimization using Lagrange multipliers.
    
    Minimize: f(x) = (1/2) x^T Q x + c^T x
    Subject to: a^T x = b
    
    Args:
        Q: 2x2 symmetric positive definite matrix
        c: 2-element vector (linear coefficients)
        a: 2-element vector (constraint coefficients)
        b: scalar (constraint value)
    
    Returns:
        Dictionary with 'x', 'lambda', and 'objective' keys
    """
    a = a.reshape(2,1)
    A = np.vstack((np.hstack((Q, -a)), np.hstack((a.T, [[0.0]]))))
    b = np.concatenate((-c, [b]))
    
    x_l = np.linalg.solve(A, b)
    x, l = x_l[0:2], x_l[-1]

    objective = 0.5 * np.dot(x.T, np.dot(Q, x)) + np.dot(c.T, x)
    
    return {'x': np.round(x, 4).tolist(), 'lambda':  round(float(l), 4), 'objective': round(float(objective), 4)}


if __name__ == '__main__':
    result = lagrange_optimize(np.array([[2, 0], [0, 2]]), np.array([0, 0]), np.array([1, 1]), 2)
    print(result)