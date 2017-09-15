import numpy as np
from numpy.linalg import norm, qr
import copy

def power(in_mat, size, maxIter, errLim):
    n = size
    mat_a = np.matrix(in_mat, dtype = float)
    x_vec = np.zeros(shape=(size,1), dtype = float)
    x_vec[0,0] = 1.0
    for no in range(maxIter):
        temp = mat_a*x_vec
        e1 = norm(temp)
        new_x = temp/e1
        e2 = norm(mat_a*new_x)
        err = abs(e2-e1)*100/e2
        x_vec = new_x
        if err < errLim:
            break
    return x_vec.T.tolist()[0], e2, no+1

def inversePower(in_mat, size, maxIter, errLim):
    mat_a = np.matrix(in_mat, dtype = float).I
    return power(mat_a, size, maxIter, errLim)

def inversePowerShift(in_mat, size, maxIter, errLim, epsE):
    mat_a = np.matrix(in_mat, dtype = float)
    mat_a = mat_a - epsE*np.identity(size)
    mat_a = mat_a.I
    x_vec, e, no = power(mat_a, size, maxIter, errLim)
    return x_vec, (1/e)+epsE, no

def qrM(in_mat, size, maxIter, errLim):
    mat_a = np.matrix(in_mat, dtype = float)
    eVals = [mat_a[x,x] for x in range(size)]
    for no in range(maxIter):
        q, r = qr(mat_a)
        new_a = r*q
        new_eVals = [new_a[x,x] for x in range(size)]
        errLis = [(new_eVals[x] - eVals[x])*100/eVals[x] for x in range(size)]
        err = max(errLis)
        eVals = new_eVals
        mat_a = new_a
        if err < errLim:
            break
    return eVals,no+1
