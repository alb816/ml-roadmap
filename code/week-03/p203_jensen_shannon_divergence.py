import numpy as np

def jensen_shannon_divergence(P: list[float], Q: list[float]) -> float:
    """
    Compute the Jensen-Shannon Divergence between two probability distributions.
    
    Args:
        P: First probability distribution
        Q: Second probability distribution
    
    Returns:
        Jensen-Shannon Divergence value
    """
    P = np.asarray(P)
    Q = np.asarray(Q)

    M = 1/2 * (P + Q)

    jsd = 0.5 * (
        np.sum(P * np.log(P / M, out=np.zeros_like(P), where=(P > 0))) +
        np.sum(Q * np.log(Q / M, out=np.zeros_like(Q), where=(Q > 0)))
    )

    return np.clip(jsd, 0.0, np.log(2))


print(jensen_shannon_divergence([0.5, 0.5], [0.5, 0.5]))