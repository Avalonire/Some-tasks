class Complexity:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return Complexity(self.a + other.a, self.b + other.b)

    def __sub__(self, other):
        return Complexity(self.a - other.a, self.b - other.b)

    def __mul__(self, other):
        return Complexity(self.a * other.a - self.b * other.b, self.b * other.a + self.a * other.b)

    def __str__(self):
        return f'{self.a} + {self.b}i'


num_1 = Complexity(3, 5)
num_2 = Complexity(-1, 2)
print(num_1)
print(num_2)
print(num_1 + num_2)
print(num_1 - num_2)
print(num_1 * num_2)
