import decompose
import solve
import sys

def printMat(mat):
    for x in mat:
        for a in x:
            print a,
        print ""

def printVec(vec):
    for x in vec:
        print x

def printLU(l, u, x):
    print "L"
    printMat(l)
    print "U"
    printMat(u)
    print "X"
    printVec(x)

a_mat = []
d_vec = []
with open('./input.txt', 'r') as f:
    n = int(f.readline().strip())
    for line in f.readlines():
        arr = map(float, line.strip().split(' '))
        a_mat.append(arr[0:n])
        d_vec.append(arr[-1])
display_str = """1 - Gauss Elimination w/o pivoting
2 - Gauss Elimination with partial pivoting
3 - Doolittle Decomposition
4 - Crout Decomposition
5 - Cholesky Decomposition
Choose option 1~5: """
choice = int(raw_input(display_str).strip())
l,u = [], []
if choice == 2:
    decompose.pivot(a_mat, d_vec, n)
if choice == 1 or choice == 2:
    gauss_mat, new_d_vec = decompose.gaussElim(a_mat, d_vec, n)
    x_vec = solve.upperMat(gauss_mat, new_d_vec, n)
    print "X"
    printVec(x_vec)
elif choice == 3:
    l,u = decompose.doolittle(a_mat, n)
    x1_vec = solve.lowerMat(l, d_vec, n)
    x_vec = solve.upperMat(u, x1_vec, n)
    printLU(l, u, x_vec)
elif choice == 4:
    l,u = decompose.crout(a_mat, n)
    x1_vec = solve.lowerMat(l, d_vec, n)
    x_vec = solve.upperMat(u, x1_vec, n)
    printLU(l, u, x_vec)
elif choice == 5:
    l, u = decompose.cholesky(a_mat, n)
    x1_vec = solve.lowerMat(l, d_vec, n)
    x_vec = solve.upperMat(l, d_vec, n)
    printLU(l, u, x_vec)
else:
    NameError("Invaild Choice")
