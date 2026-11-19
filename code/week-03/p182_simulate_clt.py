import numpy as np

def simulate_clt(distribution: str, n: int, runs: int = 10000, seed: int = 42) -> dict:
    """
    Simulate the Central Limit Theorem.

    Args:
        distribution (str): The distribution to sample from ('uniform', 'exponential', 'bernoulli').
        n (int): Sample size.
        runs (int): Number of repeated experiments.
        seed (int): Random seed for reproducibility.

    Returns:
        dict: {'mean': float, 'std': float} of the standardized sample means.
    """
    np.random.seed(seed)

    if distribution == 'uniform':
        mu = 0.5
        sigma = np.sqrt(1/12)
        dist = np.random.uniform(0, 1, size=(runs, n))
        
    elif distribution == 'exponential':
        mu = 1.0
        sigma = 1.0
        dist = np.random.exponential(1.0, size=(runs, n))
    elif distribution == 'bernoulli':
        mu = 0.3
        sigma = np.sqrt(0.3*0.7)
        dist = (np.random.rand(runs, n) < 0.3).astype(float)
    else:
        raise ValueError(f"Unsupported distribution: {distribution}")

    sample_means = dist.mean(axis=1)

    z_scores = (sample_means - mu) / (sigma / np.sqrt(n))

    return {'mean': z_scores.mean(),
            'std': z_scores.std()
    }


if __name__ == '__main__':
    res = simulate_clt('uniform', n=5, runs=5000, seed=0)
    print({'mean': round(res['mean'],3), 'std': round(res['std'],3)})