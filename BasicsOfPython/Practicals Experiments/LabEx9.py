#python program to perform matrix multiplication using numpy
import numpy as np
A = np.array([[1, 2, 3], [4, 5, 6]])
B = np.array([[7, 8], [9, 10], [11, 12]])
result = np.dot(A, B)
print("Matrix A:")
print(A)
print("\nMatrix B:")
print(B)
print('\nProduct of A and B:')
print(result)