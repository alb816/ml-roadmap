import numpy as np

def kl_divergence_normal(mu_p, sigma_p, mu_q, sigma_q):
    term1 = np.log(sigma_q / sigma_p)
    term2 = (sigma_p ** 2 + (mu_p - mu_q) ** 2) / (2 * sigma_q ** 2)
    
    kl = term1 + term2 - 0.5
    return kl


if __name__ == '__main__':
    mu_p = 0.0
    sigma_p = 1.0
    mu_q = 0.0
    sigma_q = 1.0
    print(kl_divergence_normal(mu_p, sigma_p, mu_q, sigma_q))