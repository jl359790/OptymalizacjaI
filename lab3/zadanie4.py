def GenerateSubsets(A, size_max):
    B = list()
    if size_max == 1:
        for i in range(0, len(A)):
            b = list()
            b.append(A[i])
            B.append(b)
    else:
        maxi = len(A) - size_max + 1
        for i in range (0, maxi):
            c = GenerateSubsets(A[i+1:], size_max - 1)
            for j in range (0, len(c)):
                c[j].insert(0, A[i])
                B.append(c[j])
    return B
def ChooseColumns(A, b):
    m = len(A)
    n = len(b)
    
    C = list()
    for i in range (0, m):
        c = list()
        for j in range (0, n):
            c.append(A[i][b[j]])
        C.append(c)
    return C
def FillWithZeros(x, b, n):
	y = [0 for i in range(0, n)]
	for i in range(0, len(b)):
		y[b[i]] = x[i]
	return y
def ScalarProduct(x, y):
	sum = 0
	for i in range(0, len(x)):
		sum = sum + x[i] * y[i]
	return sum
def isPositive(x):
	for i in range(0, len(x)):
		if x[i] < 0:
			return False
	return True
	
import numpy

A = (
[-1.0, 1.0, 1.0, 0.0, 0.0],
[1.0, 0.0, 0.0, 1.0, 0.0],
[0.0, 1.0, 0.0, 0.0, 1.0]
)

b = (1.0, 3.0, 2.0)

c = (1.0, 1.0, 0.0, 0.0, 0.0)

m = len(A)
n = len(A[0])

Bases = GenerateSubsets(list(range(n)), m)

X = list()

for B in Bases:
	A_B = ChooseColumns(A, B)
	if (numpy.linalg.det(A_B) != 0):
		x_B = numpy.linalg.solve(A_B, b)
		if isPositive(x_B):
			x = FillWithZeros(x_B, B, n)
			X.append(x)

if (len(X) == 0):
	print "INFEASIBLE"
else:
	j = 0
	max = ScalarProduct(c,X[0])
	for i in range(1, len(X)):
		current = ScalarProduct(c, X[i])
		if current > max:
			max = current
			j = i
	print max
	print X[j]
