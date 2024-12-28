import numpy as np
import multiprocessing
import os


def read_matrix(file_name):
    return np.loadtxt(file_name, delimiter=',')

def write_matrix(file_name, matrix):
    np.savetxt(file_name, matrix, delimiter=',')

def multiply_elements(i, j, A, B, result_file):
    result = A[i, j] * B[i, j]
    with open(result_file, 'a') as f:
        f.write(f'{i},{j},{result}\n')

def parallel_matrix_multiply(A, B, result_file):
    pool = multiprocessing.Pool()
    processes = []

    for i in range(A.shape[0]):
        for j in range(A.shape[1]):
            pool.apply_async(multiply_elements, (i, j, A, B, result_file))
    
    pool.close()
    pool.join()


def main():
    A = read_matrix('matrix_A.txt')
    B = read_matrix('matrix_B.txt')
    
    if A.shape != B.shape:
        print("Матрицы должны быть одного размера для поэлементного умножения.")
        return
    
    if os.path.exists('result.txt'):
        os.remove('result.txt')

    parallel_matrix_multiply(A, B, 'result.txt')

    print("Матрица произведения записана в 'result.txt'.")

if __name__ == "__main__":
    main()
