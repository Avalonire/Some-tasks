class Matrix:
    def __init__(self, list_of_list):
        self.matrix = list_of_list

    def __str__(self):
        return '\n'.join([' '.join([f'{i}' for i in row]) for row in self.matrix])

    def __add__(self, other):
        if len(self.matrix[0]) == len(other.matrix[0]):
            mat_sum = []
            for idx in range(len(self.matrix)):
                item = []
                for _idx in range(len(self.matrix[idx])):
                    item.append(self.matrix[idx][_idx] + other.matrix[idx][_idx])
                mat_sum.append(item)
        else:
            raise ValueError('Addition is impossible! Matrix not indent!')
        return Matrix(mat_sum)


mat_1 = Matrix([[31, 32], [37, 43], [51, 86]])
mat_2 = Matrix([[56, 33], [98, 1], [3, 99]])
print(mat_1, '| Matrix №1')
print('------------------------')
print(mat_2, '| Matrix №2')
print('------------------------\nSummary:')
print(mat_1 + mat_2)
