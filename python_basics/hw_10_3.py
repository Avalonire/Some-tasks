class Cell:
    def __init__(self, cell_numbers):
        self.cells = int(cell_numbers)

    def __add__(self, other):
        return Cell(self.cells + other.cells)

    def __sub__(self, other):
        if self.cells > other.cells:
            return Cell(self.cells - other.cells)
        else:
            raise ValueError('First cell too small!')

    def __mul__(self, other):
        return Cell(self.cells * other.cells)

    def __floordiv__(self, other):
        return Cell(self.cells // other.cells)

    def make_order(self, cells_row):
        result = []
        if self.cells <= int(cells_row):
            return f'{"*" * self.cells}'
        elif self.cells > int(cells_row):
            for i in range(self.cells // cells_row):
                result.append('*' * int(cells_row))
            result.append('*' * (self.cells % cells_row))
            return '\n'.join(result)


cell_1 = Cell(4)
cell_2 = Cell(3)
new_cell = cell_1 + cell_2
print(new_cell.cells)
print(new_cell.make_order(3))
