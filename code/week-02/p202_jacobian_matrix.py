import numpy as np

def jacobian_matrix(f, x: list[float], h: float = 1e-5):
	"""
	Compute the Jacobian matrix using numerical differentiation.
	
	Args:
		f: Function that takes a list and returns a list
		x: Point at which to evaluate the Jacobian
		h: Step size for finite differences
	
	Returns:
		Jacobian matrix
	"""
	f_base = np.array(f(x))

	j = []

	for i in range(len(x)):
		x_incr = list(x)
		x_incr[i] += h
		f_incr = np.array(f(x_incr))
		col_der = (f_incr - f_base) / h
		j.append(col_der)
	j = np.array(j).T
	return j

print(jacobian_matrix(lambda x: [2*x[0] + 3*x[1], x[0] - x[1]], [1, 2]))