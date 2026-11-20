import numpy as np

def covariance_from_joint_pmf(x_values: list, y_values: list, joint_pmf: np.ndarray) -> float:
    """
    Compute the covariance of X and Y from their joint PMF.
    
    Args:
        x_values: List of possible values for X
        y_values: List of possible values for Y
        joint_pmf: 2D numpy array where joint_pmf[i][j] = P(X=x_values[i], Y=y_values[j])
    
    Returns:
        Covariance of X and Y as a float
    """
    prob_x = np.sum(joint_pmf, axis=1)
    prob_y = np.sum(joint_pmf, axis=0)


    e_x = np.dot(prob_x, x_values)
    print(e_x)



x_values = [0, 1]
y_values = [0, 1]
joint_pmf = np.array([[0.4, 0.1], [0.1, 0.4]])
print(covariance_from_joint_pmf(x_values, y_values, joint_pmf))