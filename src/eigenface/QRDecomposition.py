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
    n = a.shape[0]
    q = np.identity(n)
    for i in range(n-1):
        y = a[i:n,i]
        h_prime = householder(y)
        h = np.block([
            [np.identity(i),np.zeros((i,n-i))],
            [np.zeros((n-i,i)),h_prime]
        ])
        ht = np.transpose(h)
        q = np.dot(q,ht)
        a = np.dot(h,a)
    return q,a