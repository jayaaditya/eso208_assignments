def lowerMat(a_mat, d_vec, n):
    x_vec = [0.0 for x in range(n)]
    for i in range(n):
        x_vec[i] = d_vec[i]
        for j in range(0,i):
            x_vec[i] -= x_vec[j]*a_mat[i][j]
        x_vec[i] = float(x_vec[i])/a_mat[i][i]
    return x_vec

def upperMat(a_mat, d_vec, n):
    x_vec = [0.0 for x in range(n)]
    for x in range(n):
        i = n - 1 - x
        x_vec[i] = d_vec[i]
        for j in range(i+1, n):
            x_vec[i] -= x_vec[j]*a_mat[i][j]
        x_vec[i] = float(x_vec[i])/a_mat[i][i]
    return x_vec
