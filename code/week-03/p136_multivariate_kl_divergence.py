import numpy as np

def multivariate_kl_divergence(mu_p: np.ndarray, Cov_p: np.ndarray, mu_q: np.ndarray, Cov_q: np.ndarray) -> float:
    """
    Computes the KL divergence between two multivariate Gaussian distributions.
    
    Parameters:
    mu_p: mean vector of the first distribution
    Cov_p: covariance matrix of the first distribution
    mu_q: mean vector of the second distribution
    Cov_q: covariance matrix of the second distribution

    Returns:
    KL divergence as a float
    """
    k = mu_p.size
    diff = mu_p - mu_q
    inv_cov_q = np.linalg.inv(Cov_q)

    term1 = np.log(np.linalg.det(Cov_q) / np.linalg.det(Cov_p))
    term2 = diff.T @ inv_cov_q @ diff
    term3 = np.trace(inv_cov_q @ Cov_p)

    kl = 0.5 * (term1 - k + term2 + term3)
    return kl


if __name__ == '__main__':
    np.random.seed(42)
    Px = np.random.randn(4, 10)
    Qx = np.random.randn(4, 10)
    mu1, cov1, mu2, cov2 = np.mean(Px, axis=1), np.cov(Px), np.mean(Qx, axis=1), np.cov(Qx)
    print(multivariate_kl_divergence(mu1, cov1, mu2, cov2))