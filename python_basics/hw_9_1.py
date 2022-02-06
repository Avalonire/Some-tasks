import tkinter as tk


class TrafficLight(tk.Tk):
    def __init__(self):
        self.__color = ['white', 'red', 'yellow', 'green']
        super().__init__()
        self.geometry('250x365')
        self.title('Светофор')
        self.canvas = tk.Canvas(self, width=125, height=365)
        self.canvas.pack()
        self.canvas.create_oval(4, 4, 120, 120, fill=self.__color[1], tags='c_1')
        self.canvas.create_oval(4, 124, 120, 240, fill=self.__color[0], tags='c_2')
        self.canvas.create_oval(4, 248, 120, 360, fill=self.__color[0], tags='c_3')
        self.canvas.create_text(60, 60, text='', font='Arial', tags='count')

    def countdown(self, seconds):
        if seconds > 0:
            self.canvas.itemconfigure('count', text=f'{seconds}')
            self.after(1000, self.countdown, seconds - 1)
        else:
            self.canvas.itemconfigure('count', text='')

    def yellow_upd(self):
        self.canvas.itemconfigure('c_1', fill=self.__color[0])
        self.canvas.itemconfigure('c_2', fill=self.__color[2])

    def green_upd(self):
        self.canvas.move('count', 0, 240)
        self.canvas.itemconfigure('count', text='9')
        self.countdown(9)
        self.canvas.itemconfigure('c_2', fill=self.__color[0])
        self.canvas.itemconfigure('c_3', fill=self.__color[3])

    def colors_off(self):
        self.canvas.itemconfigure(tk.ALL, fill=self.__color[0])

    def running(self):
        self.countdown(7)
        self.after(7000, self.yellow_upd)
        self.after(9000, self.green_upd)
        self.after(18000, self.colors_off)


if __name__ == '__main__':
    traffic = TrafficLight()
    traffic.running()
    traffic.mainloop()
