from abc import abstractmethod, ABC


class Clothes(ABC):
    def __init__(self, size, height):
        self.size = size
        self.height = height

    @abstractmethod
    def consumption(self):
        pass


class Coat(Clothes):
    def __init__(self, size):
        super().__init__(self, size)
        self.size = size

    @property
    def consumption(self):
        return '%.2f' % (self.size / 6.5 + 0.5)


class Costume(Clothes):
    def __init__(self, height):
        super().__init__(self, height)
        self.height = height

    @property
    def consumption(self):
        return '%.2f' % (self.height * 2 + 0.3)


coat = Coat(27)
costume = Costume(32)
print(coat.consumption)
print(costume.consumption)
