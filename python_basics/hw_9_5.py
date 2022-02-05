class Stationery:
    title = 'Bic'

    @staticmethod
    def draw():
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print(f'{Pen.__name__} пишет чернилами')


class Pencil(Stationery):
    def draw(self):
        print(f'{Pencil.__name__} рисует линии графитом')


class Handle(Stationery):
    def draw(self):
        print(f'{Handle.__name__}, отрисовка не смывается')


pen = Pen()
pen.draw()
print(pen.title)
pencil = Pencil()
pencil.draw()
print(pencil.title)
handle = Handle()
handle.draw()
print(handle.title)
