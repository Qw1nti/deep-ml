import numpy as np

def compute_norm(arr: np.ndarray, norm_type: str) -> float:
    """
    Compute the specified norm of the input array.
    """

    if norm_type == "frobenius":
        if arr.ndim != 2:
            raise ValueError("Frobenius norm requires a 2D array.")
        return float(np.linalg.norm(arr, "fro"))

    norms = {
        "l1": 1,
        "l2": 2,
        "linf": np.inf
    }

    if norm_type not in norms:
        raise ValueError("Invalid norm type.")

    return float(np.linalg.norm(arr.ravel(), ord=norms[norm_type]))