# Matrix Algebra
import numpy as np
A = np.array([[1,2,3],[2,7,4]])
B = np.array([[1,-1],[0,1]])
C = np.array([[5,-1],[9,1],[6,0]])
D = np.array([[3,-2,-1],[1,2,3]])
u = np.array([6,2,-3,5])
v = np.array([3,5,-1,4])
w = np.array([1,8,0,5])

# 1. Matrix Dimensions
print ('1. Matrix Dimensions')
print ('1.1) Dimension of matrix A is ' + str(A.shape))
print ('1.2) Dimension of matrix B is ' + str(B.shape))
print ('1.3) Dimension of matrix C is ' + str(C.shape))
print ('1.4) Dimension of matrix D is ' + str(D.shape))
print ('1.5) Dimension of matrix u is ' + str(u.shape))
print ('1.6) Dimension of matrix w is ' + str(w.shape))
#Result
#1. Matrix Dimensions
#1.1) Dimension of matrix A is (2, 3)
#1.2) Dimension of matrix B is (2, 2)
#1.3) Dimension of matrix C is (3, 2)
#1.4) Dimension of matrix D is (2, 3)
#1.5) Dimension of matrix u is (4,)
#1.6) Dimension of matrix w is (4,)

# 2. Vector Operations
a = 6
print('2. Vector Operations')
print ('2.1) u + v = ' + str(u + v))
print ('2.2) u - v = ' + str(u - v))
print ('2.3) a * u = ' + str(a * u))
print ('2.4) u * v = ' + str(np.dot(u,v)))
print ('2.5) ||u|| = ' + str(np.linalg.norm(u)))
#Result
#2. Vector Operations
#1.1) u + v = [ 9  7 -4  9]
#1.2) u - v = [ 3 -3 -2  1]
#1.3) a * u = [ 36  12 -18  30]
#1.4) u * v = 51
#1.5) ||u|| = 8.60232526704

# 3. Matrix Operations
print('3. Matrix Operations')
print ('3.1) not defined')
print ('3.2) \n A - C(T) = ' + str(A - C.transpose()))
print ('3.3) \n C(T) + 3D = ' + str(C.transpose() + 3 * D))
print ('3.4) \n BA = ' + str(np.dot(B,A)))
print ('3.5) not defined')
print('\n' + 'Optional')
print ('3.6) not defined')
print ('3.7) \n CB = ' + str(np.dot(C,B)))
print ('3.8) \n B^4 = ' + str(B ** 4))
print ('3.9) \n AA(T) = ' + str(np.dot(A,A.transpose())))
print ('3.10) \n D(T)D = ' + str(np.dot(D.transpose(),D)))
#Result
#3. Matrix Operations
#3.1) not defined
#3.2) 
# A - C(T) = [[-4 -7 -3]
# [ 3  6  4]]
#3.3) 
# C(T) + 3D = [[14  3  3]
# [ 2  7  9]]
#3.4) 
# BA = [[-1 -5 -1]
# [ 2  7  4]]
#3.5) not defined

#Optional
#3.6) not defined
#3.7) 
# CB = [[ 5 -6]
# [ 9 -8]
# [ 6 -6]]
#3.8) 
# B^4 = [[1 1]
# [0 1]]
#3.9) 
# AA(T) = [[14 28]
# [28 69]]
#3.10) 
# D(T)D = [[10 -4  0]
# [-4  8  8]
# [ 0  8 10]]
