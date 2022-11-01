class Road:
    def __init__(self, width, length):
        self._length = length
        self._width = width

    def mass_coating(self, mass_1m, thickness):
        print(f'{int(self._width * self._length * mass_1m * thickness / 1000)} т')


our_road = Road(20, 5000)
our_road.mass_coating(25, 5)
