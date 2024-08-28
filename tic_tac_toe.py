import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.title('Tic Tac Toe Game')
win.resizable = False, False
win.geometry("855x765")

class Circle:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Cross:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Frame:
    def __init__(self, number, id):
        self.no = number              # 1 ~ 9
        self.id = id                  # id: 0 = circle / 1 = cross




def click(event, self):
    print(f"clicked at {event.x} - {event.y}")

p1_f = tk.Frame(win, width=90, height=675, background='blue').place(x=0)
p2_f = tk.Frame(win, width=90, height=675, background='red').place(x=765)
board_f = tk.Frame(win, width=675, height=675, background='yellow')
board_f.pack()
box_f = tk.Frame(win, width=855, height=90, background='green')
box_f.pack()

frames = [1, 2, 3, 4, 5, 6, 7, 8, 9]

b_c3 = tk.Canvas(board_f, width=225, height=225)#.grid(row=0, column=0).bind('<Button-1>', click)
b_c4 = tk.Canvas(board_f, width=225, height=225)#.grid(row=0, column=0).bind('<Button-1>', click)
b_c5 = tk.Canvas(board_f, width=225, height=225)#.grid(row=0, column=0).bind('<Button-1>', click)
b_c2 = tk.Canvas(board_f, width=225, height=225)#.grid(row=0, column=0).bind('<Button-1>', click)
b_c6 = tk.Canvas(board_f, width=225, height=225)#.grid(row=0, column=0).bind('<Button-1>', click)
b_c7 = tk.Canvas(board_f, width=225, height=225)#.grid(row=0, column=0).bind('<Button-1>', click)
b_c8 = tk.Canvas(board_f, width=225, height=225)#.grid(row=0, column=0).bind('<Button-1>', click)
b_c9 = tk.Canvas(board_f, width=225, height=225)#.grid(row=0, column=0).bind('<Button-1>', click)
b_c1 = tk.Canvas(board_f, width=225, height=225)#.grid(row=0, column=0).bind('<Button-1>', click)

b_frames = [b_c1, b_c2, b_c3, b_c4, b_c5, b_c6, b_c7, b_c8, b_c9]




lst = ['Cross', 'Circle']
for i in range(6):
    for turn in lst:
        turn_l = tk.Label(box_f, text=f"It's {turn}'s turn.", width=20).pack()
        # wait until you perform action

lst2 = ['Circle', 'Cross']
for i in range(6):
    for turn in lst2:
        turn_l = tk.Label(box_f, text=f"It's {turn}'s turn.", width=20).pack()
        # wait until you perform action

win.mainloop()