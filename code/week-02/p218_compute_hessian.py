import numpy as np
from typing import Callable

def compute_hessian(f: Callable[[list[float]], float], point: list[float], h: float = 1e-5) -> list[list[float]]:
	"""
	Compute the Hessian matrix of function f at the given point using finite differences.
	
	Args:
		f: A scalar function that takes a list of floats and returns a float
		point: The point at which to compute the Hessian (list of coordinates)
		h: Step size for finite differences (default: 1e-5)
		
	Returns:
		The Hessian matrix as a list of lists (n x n where n = len(point))
		
	"""
	n = len(point)
	H = np.zeros((n, n))
	E = np.eye(n)
	f_base = np.asarray(f(point))
	
	for i in range(n):
		H[i, i] = (f(point + h*E[i]) - 2*f_base + f(point - h*E[i])) / h**2
		for j in range(i + 1, n):
			H[i, j] = H[j, i] = (f(point + h*E[i] + h*E[j]) - f(point + h*E[i] - h*E[j]) - 
			                     f(point - h*E[i] + h*E[j]) + f(point - h*E[i] - h*E[j])) / (4 * h**2)
	return H.tolist()

	 

if __name__ == '__main__':
	def f(p): return p[0]**2 + p[1]**2
	result = compute_hessian(f, [0.0, 0.0])
	print(result)