import numpy as np

def getEignValuesVectors(Matrix):
    """ 
    return all eign value and vectors of A by 
    Simultaneous power iteration method 
    """
    rowNum = Matrix.shape[0] 

    # Initialize the eigenvectors
    # *** QR decomposition ***
    Q = np.random.rand(rowNum, rowNum) 
    Q, _ = np.linalg.qr(Q)
    Q_prev = np.zeros((rowNum, rowNum)) # Initialize previous Q

    # Initialize the eigenvalues
    eVal = np.zeros(rowNum) 
    
    # Iterate until convergence
    while np.linalg.norm(Q - Q_prev) > 1e-10: # Convergence criterion
        # *** Update previous Q ***
        Q_prev = Q 

        # Compute the matrix-by-vector product AZ
        Z = Matrix.dot(Q) 
        # Compute the QR factorization of Z
        Q, _ = np.linalg.qr(Z) 

        # Update the eigenvalues
        eVal = np.diag(Q.T.dot(Matrix.dot(Q)))
    return eVal, Q

