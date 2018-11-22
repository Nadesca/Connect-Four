from tkinter import *
import time

WIDTH = 1000
HEIGHT = 800
F = 5
tk = Tk()
canvas = Canvas(tk, width=WIDTH, height=HEIGHT, bg="blue")
canvas.pack()
color = 'red'
# x = 600
# y = 100
r = 25


def draw_grid():
    # x0, x1 = 0, canvas.winfo_width()
    # for r in range(1, 100):
    #     y = r * 100
    for y in range(100, canvas.winfo_height(), 100):
        canvas.create_line(100, y, 800, y, fill="black")

    # for y in range(10, 80, 10):  # draw horizontal borders
    #     canvas.create_line(10*F, y*F, 80*F, y*F, fill="black")
    # for x in range(10, 90, 10):  # draw vertical borders
    #     canvas.create_line(x*F, 1*F, x*F, 70*F, fill="black")

    # canvas.create_line(300, 100, 500, 100, fill="white")
    # canvas.create_line(200, 200, 100, 600, fill="black")
    # canvas.create_line(100, 100, 900, 100, fill="white")


    #
    # y0, y1 = 0, canvas.winfo_height()
    # for c in range(1, 10):
    #     x = c * 100
    #     canvas.create_line(x, y0, x, y1, fill="black")


class Disc:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.shape = canvas.create_oval(self.x-r, self.y-r, self.x+r, self.y+r, fill=color)
        self.speedx = 0
        self.speedy = 3
        self.active = True
        self.move_active()

    def disc_update(self):
        canvas.move(self.shape, self.speedx, self.speedy)
        pos = canvas.coords(self.shape)
        if pos[3] >= (HEIGHT-100) or pos[1] <= 0:
            self.speedy = 0

    def move_active(self):
        if self.active:
            self.disc_update()
            tk.after(2, self.move_active)


draw_grid()

new_disc = Disc(400, 300, "yellow")
new_disc2 = Disc(700, 100, "red")
tk.mainloop()
