import numpy as np

mat1 = np.matrix([[1, 2, 5], [3, 4, 8], [4, 2, 6]])
mat2 = np.matrix([[2, 3, 1], [4, 7, 9], [2, 2, 1]])

print("Matrix1:\n", mat1)
print("Matrix2:\n", mat2)
print()

print("Matrix Addition:\n", np.add(mat1, mat2))
print("Matrix Subtraction:\n", np.subtract(mat1, mat2))
print("Matrix Multiplication:\n", np.matmul(mat1, mat2))
print("Scalar Multiplication of Matrix1 by 2:\n", 2 * mat1)
print("Transpose of Matrix1:\n", np.transpose(mat1))
