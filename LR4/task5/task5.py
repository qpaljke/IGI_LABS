import numpy as np


class Matrix:
    def __init__(self):
        num_rows = np.random.randint(2, 7)
        num_cols = np.random.randint(2, 7)
        self.matrix = np.random.rand(num_rows, num_cols)

    def lower_triangular_sum(self):
        return np.sum(np.tril(self.matrix, -1))

    def np_std_on_diagonal(self):
        return np.round(np.std(np.diagonal(self.matrix)), 2)

    def std_on_diagonal(self):
        std_sum = 0
        diagonal = np.diagonal(self.matrix)
        for i in range(len(diagonal)):
            std_sum += np.power(diagonal[i] - np.mean(diagonal), 2)
        return np.round(np.sqrt(std_sum/len(diagonal - 1)), 2)

    def print_info(self):
        print('Matrix:\n', self.matrix)
        print('Std on diagonal:', self.std_on_diagonal())
        print('Numpy std on diagonal:', self.np_std_on_diagonal())


def run_task():
    matrix = Matrix()
    matrix.print_info()
