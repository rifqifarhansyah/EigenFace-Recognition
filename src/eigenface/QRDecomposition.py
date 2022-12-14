import numpy as np
import math

def householder(y):
    rowNum = y.shape[0]
    k = np.sign(y[0])*math.sqrt(np.dot(y,y))
    e = np.zeros((1,rowNum))
    e[0][0] = 1
    u = y - (k*e)
    ut = np.transpose(u)
    H = np.identity(rowNum)-2*(np.dot(ut,u)/np.dot(u,ut))
    return H

def getQR(a):
    numRow = a.shape[0]
    q = np.identity(numRow)
    for i in range(numRow-1):
        y = a[i:numRow,i]
        h_prime = householder(y)
        h = np.block([
            [np.identity(i),np.zeros((i,numRow-i))],
            [np.zeros((numRow-i,i)),h_prime]
        ])
        ht = np.transpose(h)
        q = np.dot(q,ht)
        a = np.dot(h,a)
    return q,a