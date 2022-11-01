class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.name} start going!')

    def stop(self):
        print(f'{self.name} stop!')

    def turn(self, direction=None):
        if direction == 'right':
            print(f'{self.name} turn {direction}')
        elif direction == 'left':
            print(f'{self.name} turn {direction}')
        else:
            print(f'{self.name} need direction to turn!')

    def show_speed(self):
        print(f'{self.name} speed {self.speed}')


class TownCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)
        self.name = f'Town car {name}'

    def show_speed(self):
        if self.speed >= 60:
            print(f'{self.name} speed {self.speed}')
            print(f'{self.name} speed violation! Slow down!')
        else:
            print(f'{self.name} speed {self.speed}')


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)
        self.name = f'Work car {name}'

    def show_speed(self):
        if self.speed >= 40:
            print(f'{self.name} speed {self.speed}')
            print(f'{self.name} speed violation! Slow down!')
        else:
            print(f'{self.name} speed {self.speed}')


class SportCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)
        self.name = f'Sport car {name}'


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        self.name = f'Police car {name}'
        self.is_police = True


chuck_car = PoliceCar(80, 'red', 'Mazda')
josh_car = TownCar(70, 'black', 'Kia')
bill_car = WorkCar(40, 'green', 'Jeep')
kevin_car = SportCar(90, 'red', 'Lamborghini')

josh_car.show_speed()
josh_car.turn('right')
josh_car.turn()
bill_car.show_speed()
chuck_car.stop()
print(chuck_car.is_police)
print(kevin_car.__dict__)
kevin_car.go()
