from typing import List, Any
import numpy as np

class Matrix:
    def __init__(self, matrix: List[List[Any]]) -> None:
        self.matrix = matrix
        self.rows = len(matrix)
        self.cols = len(matrix[0]) if self.rows > 0 else 0

    def __str__(self) -> str:
        return '\n'.join([' '.join(map(str, row)) for row in self.matrix])

    def __add__(self, other: 'Matrix') -> 'Matrix':
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError('Invalid matrix dimensions')
        return Matrix([[self.matrix[i][j] + other.matrix[i][j] for j in range(self.cols)] for i in range(self.rows)])

    def __mul__(self, other: 'Matrix') -> 'Matrix':
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError('Invalid matrix dimensions')
        return Matrix([[self.matrix[i][j] * other.matrix[i][j] for j in range(self.cols)] for i in range(self.rows)])

    def __matmul__(self, other: 'Matrix') -> 'Matrix':
        if self.cols != other.rows:
            raise ValueError('Invalid matrix dimensions')
        return Matrix([[sum(self.matrix[i][k] * other.matrix[k][j] for k in range(self.cols)) for j in range(other.cols)] for i in range(self.rows)])

def main():
    np.random.seed(0)

    np_matrix1 = np.random.randint(0, 10, (10, 10))
    np_matrix2 = np.random.randint(0, 10, (10, 10))

    matrix1 = Matrix(np_matrix1.tolist())
    matrix2 = Matrix(np_matrix2.tolist())

    with open('artifacts/3.1/matrix+.txt', 'w') as file:
        file.write(str(matrix1))
        file.write('\n\n')
        file.write(str(matrix2))
        file.write('\n\n')
        file.write(str(matrix1 + matrix2))

    with open('artifacts/3.1/matrix*.txt', 'w') as file:
        file.write(str(matrix1))
        file.write('\n\n')
        file.write(str(matrix2))
        file.write('\n\n')
        file.write(str(matrix1 * matrix2))

    with open('artifacts/3.1/matrix@.txt', 'w') as file:
        file.write(str(matrix1))
        file.write('\n\n')
        file.write(str(matrix2))
        file.write('\n\n')
        file.write(str(matrix1 @ matrix2))

if __name__ == '__main__':
    main()

