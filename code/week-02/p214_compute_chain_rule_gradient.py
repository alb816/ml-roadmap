import numpy as np


def forward(functions: list[str], x: float):
	functions.reverse()
	values = []
	prev = x
	for f_i in range(len(functions)):
		if functions[f_i] == 'square':
			values.append((functions[f_i], prev**2))
		elif functions[f_i] == 'sin':
			values.append((functions[f_i], np.sin(prev)))
		elif functions[f_i] == 'exp':
			values.append((functions[f_i], np.exp(prev)))
		elif functions[f_i] == 'log':
			values.append((functions[f_i], np.log(prev)))
		prev = values[f_i][1]
	return values


def der_simple(f: str, x: float):
	if f == 'square':
		der = 2 * x
	elif f == 'sin':
		der = np.cos(x)
	elif f == 'exp':
		der = np.exp(x)
	elif f == 'log':
		der = 1 / x
	return der


def compute_chain_rule_gradient(functions: list[str], x: float) -> float:
	"""
	Compute derivative of composite functions using chain rule.
	
	Args:
		functions: List of function names (applied right to left)
				  Available: 'square', 'sin', 'exp', 'log'
		x: Point at which to evaluate derivative
	
	Returns:
		Derivative value at x
	
	Example:
		['sin', 'square'] represents sin(x²)
		['exp', 'sin', 'square'] represents exp(sin(x²))
	"""
	vals = forward(functions, x)
	der = der_simple(functions.pop(0), x)
	
	for f_i in range(1, len(functions)+1):
		x = vals[f_i-1][1]
		f = vals[f_i][0]
		der *= der_simple(f, x)
	return der


result = compute_chain_rule_gradient(['exp', 'sin', 'square'], 0.5)
print(result)