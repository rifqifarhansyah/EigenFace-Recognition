import numpy as np
import cv2
from eigen import simultaneous_power_iteration ,eigenVectors, eigenValues
from PIL import Image

def SVD(A, k):
    """ 
    Decompose a matrix into U, Sigma, and VTranspose

    Parameters
    ----------
    A : numpy.ndarray
        The matrix to be decomposed
    k : int
        The number of singular values to be computed
    """
    # Compute the eigenvalues and eigenvectors of A*A^T
    lambda_, Q = simultaneous_power_iteration(A.dot(A.T), k)

    # Compute the singular values
    sigma = np.sqrt(lambda_)

    # Compute the eigenvectors of A^T*A
    lambda_, P = simultaneous_power_iteration(A.T.dot(A), k)

    # Compute the singular vectors
    U = A.dot(P)
    for i in range(k):
        U[:,i] = U[:,i]/sigma[i]

    # Return the singular values and vectors
    return sigma, U, P.T