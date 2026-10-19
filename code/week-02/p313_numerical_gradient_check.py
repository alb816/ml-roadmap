import numpy as np

def numerical_gradient_check(f, x, analytical_grad, epsilon=1e-7):
    """
    Perform numerical gradient checking using centered finite differences.
    
    Args:
        f: A function that takes a numpy array and returns a scalar
        x: numpy array, the point at which to check gradient
        analytical_grad: numpy array, the analytically computed gradient
        epsilon: float, small value for finite difference approximation
    
    Returns:
        tuple: (numerical_grad, relative_error)
    """
    num_grad = np.zeros_like(analytical_grad)
    
    for i in range(len(x)):
        e_vector = np.zeros_like(x, dtype=float)
        e_vector[i] = epsilon
        num_grad[i] = (f(x[i] + e_vector) - f(x[i] - e_vector)) / (2 * epsilon)

    rel_err = np.linalg.norm(num_grad - analytical_grad) / np.sum([np.linalg.norm(num_grad), np.linalg.norm(analytical_grad)])

    return num_grad, rel_err


if __name__ == '__main__':
    def f(x): return np.sum(x**2)
    x = np.array([3.0])
    analytical_grad = np.array([6.0])
    num_grad, rel_err = numerical_gradient_check(f, x, analytical_grad)
    print(([float(g) for g in np.round(num_grad, 4)], bool(rel_err < 1e-5)))
    x = np.array([[3.0], [2]])
    print(x.T)