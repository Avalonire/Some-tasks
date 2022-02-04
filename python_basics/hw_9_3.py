class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def get_full_name(self):
        print(f'Worker full name: {self.name} {self.surname}')

    def get_total_income(self):
        print(f'Worker total income: {self._income["wage"] + self._income["bonus"]}')


ivan = Position('Ivan', 'Ivanov', 'manager', 67000, 13400)
print(ivan.__dict__)
ivan.get_full_name()
ivan.get_total_income()
