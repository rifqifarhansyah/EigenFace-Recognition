import numpy as np
import time
import cv2
import os
import math
from QRDecomposition import *


def getEignValues(A):
    """ 
    Simultaneous power iteration method for computing the top k eigenvalues
    and eigenvectors of a matrix A.
    """
    rowNum = A.shape[0] 

    # Initialize the eigenvectors
    # *** QR decomposition ***
    Q = np.random.rand(rowNum, rowNum) 
    Q, _ = getQR(Q)
    Q_prev = np.zeros((rowNum, rowNum)) # Initialize previous Q

    # Initialize the eigenvalues
    eVal = np.zeros(rowNum) 

    # Iterate until convergence
    while np.linalg.norm(Q - Q_prev) > 1e-10: # Convergence criterion
        # *** Update previous Q ***
        Q_prev = Q 

        # Compute the matrix-by-vector product AZ
        Z = A.dot(Q) 

        # Compute the QR factorization of Z
        Q, _ = getQR(Z) 

        # Update the eigenvalues
        eVal = np.diag(Q.T.dot(A.dot(Q)))

    return eVal

def getEignVectors(A):
    """ 
    Simultaneous power iteration method for computing the top k eigenvalues
    and eigenvectors of a matrix A.
    """
    rowNum = A.shape[0] 

    # Initialize the eigenvectors
    # *** QR decomposition ***
    Q = np.random.rand(rowNum, rowNum) 
    Q, _ = getQR(Q)
    Q_prev = np.zeros((rowNum, rowNum)) # Initialize previous Q

    # Initialize the eigenvalues
    eVal = np.zeros(rowNum) 

    # Iterate until convergence
    while np.linalg.norm(Q - Q_prev) > 1e-10: # Convergence criterion
        # *** Update previous Q ***
        Q_prev = Q 

        # Compute the matrix-by-vector product AZ
        Z = A.dot(Q) 

        # Compute the QR factorization of Z
        Q, _ = getQR(Z) 

        # Update the eigenvalues
        eVal = np.diag(Q.T.dot(A.dot(Q)))

    return Q
    