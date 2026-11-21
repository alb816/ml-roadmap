import numpy as np

def entropy_and_cross_entropy(P: list[float], Q: list[float]) -> tuple[float, float]:
    """
    Compute entropy of P and cross-entropy between P and Q.
    
    Args:
        P: True probability distribution
        Q: Predicted probability distribution
    
    Returns:
        Tuple of (entropy H(P), cross-entropy H(P,Q))
    """
    P = np.asarray(P)
    Q = np.asarray(Q)

    mask = P > 0

    entropy = np.dot(P[mask], -np.log(P[mask]))
    cross_entropy = np.dot(P[mask], -np.log(Q[mask])) if not np.any(Q[mask] == 0) else float('inf')
    return (round(entropy, 6), round(cross_entropy, 6))


print(entropy_and_cross_entropy([0.25, 0.25, 0.25, 0.25], [0.25, 0.25, 0.25, 0.25]))