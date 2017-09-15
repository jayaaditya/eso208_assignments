import numpy as np
import math

def doolittle(a_mat, n):
    l_mat = [[0 for x in range(n)] for a in range(n)]
    u_mat = [[0 for x in range(n)] for a in range(n)]
    for x in range(n):
        l_mat[x][x] = 1
    for i in range(n):
        for j in range(i,n):
            u_mat[i][j] = a_mat[i][j]
            for k in range(0, i):
                u_mat[i][j] -= l_mat[i][k]*u_mat[k][j]
        for j in range(i+1,n):
            l_mat[j][i] = a_mat[j][i]
            for k in range(0, i):
                l_mat[j][i] -= l_mat[j][k]*u_mat[k][i]
            l_mat[j][i] = float(l_mat[j][i])/u_mat[i][i]
    return l_mat, u_mat

def crout(a_mat, n):
    l_mat = [[0 for x in range(n)] for a in range(n)]
    u_mat = [[0 for x in range(n)] for a in range(n)]
    for x in range(n):
        u_mat[x][x] = 1
    for i in range(n):
        for j in range(i,n):
            l_mat[j][i] = a_mat[j][i]
            for k in range(0, i):
                l_mat[j][i] -= l_mat[j][k]*u_mat[k][i]
        for j in range(i+1, n):
            u_mat[i][j] = a_mat[i][j]
            for k in range(0,i):
                u_mat[i][j] -= l_mat[i][k]*u_mat[k][j]
            u_mat[i][j] = float(u_mat[i][j])/l_mat[i][i]
    return l_mat, u_mat

def gaussElim(a_mat, d_vec, n):
    a = np.matrix(a_mat)
    d = d_vec
    for x in range(n-1):
        for x1 in range(x+1, n):
            d[x1] = d[x1] - a[x1,x]*d[x]/a[x,x]
            a[x1] = a[x1] - a[x1,x]*a[x]/a[x,x]
    return a.tolist(), d

def pivot(a_mat, d_vec, n):
    for i in range(n):
        max_no = abs(a_mat[i][i])
        index = i
        for j in range(i+1, n):
            if abs(a_mat[j][i]) > max_no:
                max_no = abs(a_mat[j][i])
                index = j
        temp = a_mat[i][:]
        a_mat[i] = a_mat[index]
        a_mat[index] = temp
        temp = float(d_vec[i])
        d_vec[i] = d_vec[index]
        d_vec[index] = temp

def cholesky(a_mat, n):
    l_mat = [[0 for x in range(n)] for a in range(n)]
    for i in range(n):
        temp = a_mat[i][i]
        for k in range(0,i):
            temp -= l_mat[i][k]*l_mat[i][k]
        l_mat[i][i] = math.sqrt(temp)
        for j in range(i+1, n):
            l_mat[j][i] = a_mat[j][i]
            for k in range(0,i):
                l_mat[j][i] -= l_mat[j][k]*l_mat[k][i]
            l_mat[j][i] = l_mat[j][i]/l_mat[i][i]
    u_mat = np.matrix(l_mat).getT().tolist()
    return l_mat, u_mat
                
