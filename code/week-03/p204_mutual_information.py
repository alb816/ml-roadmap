import numpy as np

def mutual_information(joint_prob: list[list[float]]) -> float:
    """
    Compute the mutual information between two random variables.
    
    Args:
        joint_prob: 2D joint probability distribution P(X,Y)
    
    Returns:
        Mutual information I(X;Y)
    """
    p_xy = np.asarray(joint_prob, dtype=float)

    p_x = np.sum(p_xy, axis=1, keepdims=True)
    p_y = np.sum(p_xy, axis=0, keepdims=True)

    p_x_p_y = p_x * p_y

    mask = p_xy > 0


    info_xy = np.sum(p_xy[mask] * np.log(p_xy[mask] / p_x_p_y[mask]))
    
    return info_xy

