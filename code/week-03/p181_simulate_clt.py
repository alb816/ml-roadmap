import numpy as np

def simulate_clt(num_samples: int, sample_size: int, distribution: str = 'uniform') -> float:
    """
    Compute the mean of sample means to demonstrate the sampling distribution.

    Args:
        num_samples: Number of independent samples to draw
        sample_size: Size of each sample
        distribution: 'uniform' (0,1) or 'exponential' (scale=1)

    Returns:
        Mean of the sample means (float)
    """
    sample_means = []

    for _ in range(num_samples):
        if distribution == 'uniform':
            dist = np.random.uniform(0, 1, sample_size)
        elif distribution == 'exponential':
            dist = np.random.exponential(1, sample_size)
            
        sample_means.append(np.mean(dist))

    return np.mean(sample_means)


if __name__ == '__main__':
    np.random.seed(42)
    print(simulate_clt(1000, 30, 'uniform'))