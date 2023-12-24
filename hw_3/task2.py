import numpy as np
from numpy.lib.mixins import NDArrayOperatorsMixin

class FileMixin:
    def write_to_file(self, file_path):
        with open(file_path, 'w') as file:
            file.write(str(self))

class StringMixin:
    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.__array__()])
    
class PropertyAccessMixin:
    @property
    def matrix(self):
        return self

    @matrix.setter
    def matrix(self, value):
        self[...] = value
    
class Matrix(NDArrayOperatorsMixin, FileMixin, StringMixin, PropertyAccessMixin):
    def __init__(self, matrix):
        self._matrix = np.array(matrix)

    def __array__(self):
        return self._matrix

    # from NDArrayOperatorsMixin doc: ``__array_ufunc__`` method, which subclasses must implement.
    def __array_ufunc__(self, ufunc, method, *inputs, **kwargs):
        inputs = tuple(x._matrix if isinstance(x, Matrix) else x for x in inputs)
        result = getattr(ufunc, method)(*inputs, **kwargs)
        if method == '__call__' and isinstance(result, np.ndarray):
            return type(self)(result)
        return result

def main():
    np.random.seed(0)

    np_matrix1 = np.random.randint(0, 10, (10, 10))
    np_matrix2 = np.random.randint(0, 10, (10, 10))

    matrix1 = Matrix(np_matrix1.tolist())
    matrix2 = Matrix(np_matrix2.tolist())

    with open('artifacts/3.2/matrix+.txt', 'w') as file:
        file.write(str(matrix1))
        file.write('\n\n')
        file.write(str(matrix2))
        file.write('\n\n')
        file.write(str(matrix1 + matrix2))
    
    with open('artifacts/3.2/matrix-.txt', 'w') as file:
        file.write(str(matrix1))
        file.write('\n\n')
        file.write(str(matrix2))
        file.write('\n\n')
        file.write(str(matrix1 - matrix2))

    with open('artifacts/3.2/matrix*.txt', 'w') as file:
        file.write(str(matrix1))
        file.write('\n\n')
        file.write(str(matrix2))
        file.write('\n\n')
        file.write(str(matrix1 * matrix2))

    with open('artifacts/3.2/matrix@.txt', 'w') as file:
        file.write(str(matrix1))
        file.write('\n\n')
        file.write(str(matrix2))
        file.write('\n\n')
        file.write(str(matrix1 @ matrix2))

if __name__ == '__main__':
    main()

