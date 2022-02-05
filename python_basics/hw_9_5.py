class Stationery:
    title = 'Bic'

    @staticmethod
    def draw():
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print(f'{self.title} {Pen.__name__} пишет чернилами')


class Pencil(Stationery):
    def draw(self):
        print(f'{self.title} {Pencil.__name__} рисует линии графитом')


class Handle(Stationery):
    def draw(self):
        print(f'{self.title} {Handle.__name__}, отрисовка не смывается')


pen = Pen()
pen.draw()
pencil = Pencil()
pencil.draw()
handle = Handle()
handle.draw()
