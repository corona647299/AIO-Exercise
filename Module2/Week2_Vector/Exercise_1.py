import numpy as np

#a
def compute_vector_length(vector):
    len_of_vector = np.linalg.norm(vector)
    return len_of_vector

#b
def compute_dot_product(vector1, vector2):
    result = np.dot(vector1, vector2)
    return result

#c
def matrix_multi_vector(matrix, vector):
    result = np.dot(matrix, vector)
    return result

#d
def matrix_multi_matrix(matrix1, matrix2):
    len_of_vector = np.dot(matrix1, matrix2)
    return len_of_vector

#e
def inverse_matrix(matrix):
    result = np.linalg.inv(matrix)
    return result

m1 = np.array([[-2, 6], [8, -4]])
result = inverse_matrix(m1)
print(result)



