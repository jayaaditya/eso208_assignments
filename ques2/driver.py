import methods

def printMat(mat):
    for x in mat:
        for a in x:
            print a,
        print ""

def printVec(vec):
    for x in vec:
        print x

with open('./input.txt', 'r') as f:
    n = int(f.readline().strip())
    mat_a = []
    for x in range(n):
        row = map(float, f.readline().strip().split(' '))
        mat_a.append(row)
    maxIter = int(f.readline().strip())
    errLim = float(f.readline().strip())
    epsE = float(f.readline().strip())

display_str = """1 - Power Method
2 - Inverse Power Method
3 - Inverse Power Method with shift 
4 - QR method
Choose option 1~4: """
choice = int(raw_input(display_str).strip())
if choice == 1:
    x_vec, eVal, no = methods.power(mat_a, n, maxIter, errLim)
    print "Eigenvalue"
    print eVal
    print "Eigenvector"
    printVec(x_vec)
    print "No. of Iterations"
    print no
elif choice == 2:
    x_vec, eVal, no = methods.inversePower(mat_a, n, maxIter, errLim)
    print "Eigenvalue"
    print 1/eVal
    print "Eigenvector"
    printVec(x_vec)
    print "No. of Iterations"
    print no
elif choice == 3:
    x_vec, eVal, no = methods.inversePowerShift(mat_a, n, maxIter, errLim, epsE)
    print "Eigenvalue"
    print eVal
    print "Eigenvector"
    printVec(x_vec)
    print "No. of Iterations"
    print no
elif choice == 4:
    eVal, no = methods.qrM(mat_a, n, maxIter, errLim)
    print "Eigenvalues"
    printVec(eVal)
    print "No. of Iterations"
    print no
else:
    NameError("Invalid choice")
