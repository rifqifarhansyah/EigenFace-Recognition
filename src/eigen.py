import numpy as np
import time
import cv2
import os

def simultaneous_power_iteration(A, k):
    """ 
    Simultaneous power iteration method for computing the top k eigenvalues
    and eigenvectors of a matrix A.
    """
    # Initialize the eigenvectors
    n = A.shape[0] # number of rows
    Q = np.random.rand(n, k) # Random initial guess
    Q, _ = np.linalg.qr(Q) # QR decomposition
    Q_prev = np.zeros((n, k)) # Initialize previous Q

    # Initialize the eigenvalues
    lambda_ = np.zeros(k) # Initialize eigenvalues

    # Iterate until convergence
    while np.linalg.norm(Q - Q_prev) > 1e-10: # Convergence criterion
        Q_prev = Q # Update previous Q
        Z = A.dot(Q) # Compute the matrix-by-vector product AZ
        Q, _ = np.linalg.qr(Z) # Compute the QR factorization of Z
        lambda_ = np.diag(Q.T.dot(A.dot(Q))) # Update the eigenvalues

    return lambda_, Q

def getEigenVectors(A, k):
    """ 
    Compute the top k eigenvectors of a matrix A.
    """
    lambda_, Q = simultaneous_power_iteration(A, k) # Compute the eigenvalues and eigenvectors
    return Q

def getEigenValues(A, k):
    """ 
    Compute the top k eigenvalues of a matrix A.
    """
    lambda_, Q = simultaneous_power_iteration(A, k) # Compute the eigenvalues and eigenvectors
    return lambda_

    