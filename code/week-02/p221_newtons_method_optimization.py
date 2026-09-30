import numpy as np
from typing import Callable

def newtons_method_optimization(
	gradient_func: Callable[[list[float]], list[float]],
	hessian_func: Callable[[list[float]], list[list[float]]],
	x0: list[float],
	tol: float = 1e-6,
	max_iter: int = 100
) -> list[float]:
	"""
	Find the minimum of a function using Newton's method.
	
	Args:
		gradient_func: Function that returns gradient vector at a point
		hessian_func: Function that returns Hessian matrix at a point
		x0: Initial guess (list of coordinates)
		tol: Convergence tolerance for gradient norm
		max_iter: Maximum number of iterations
		
	Returns:
		The point that minimizes the function
	"""
	x = np.asarray(x0, dtype=float)

	for i in range(max_iter):
		g = np.asarray(gradient_func(x), dtype=float)
		if np.linalg.norm(g) < tol:
			break
		H = np.asarray(hessian_func(x), dtype=float)
		delta = np.linalg.solve(H, -g)
		x += delta
	return x


def grad(x): return [2 * x[0]]
def hess(x): return [[2.0]]
result = newtons_method_optimization(grad, hess, [5.0])
# print([round(v, 4) for v in result])
print(result)