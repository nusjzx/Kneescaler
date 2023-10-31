import numpy as np

def matmul(size):
    
    matrix_A = np.random.rand(size, size)
    matrix_B = np.random.rand(size, size)

    result_matrix = np.dot(matrix_A, matrix_B)

    return result_matrix

# Example usage:
# result = matmul(100)  # Perform matrix multiplication with 100x100 matrices
