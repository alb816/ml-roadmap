def taylor_approximation(func_name: str, x: float, n_terms: int) -> float:
    t0, update = {
        'exp': (1.0, lambda t, i: t * x / (i + 1)),
        'sin': (x,   lambda t, i: -t * x * x / ((2 * i + 2) * (2 * i + 3))),
        'cos': (1.0, lambda t, i: -t * x * x / ((2 * i + 1) * (2 * i + 2))),
    }[func_name]

    s, term = 0.0, t0
    for i in range(n_terms):
        s += term
        term = update(term, i)

    return round(s, 6)