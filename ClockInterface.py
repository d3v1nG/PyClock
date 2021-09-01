from tkinter import * 
from tkinter.ttk import *
import tkinter.font as tkFont
# from GameManager import GameManager
from ChessTimer import ChessTimer
import threading
import os


root = Tk()
p1_timer = ChessTimer(5)
# p1_timer.start()
# p1_timer.pause()
p2_timer = ChessTimer(5)
# p2_timer.start()
# p2_timer.pause()


def p1_press(event):
    if p1_timer.running:
        p1_timer.pause()
        p2_timer.resume()
    else:
        print("Not your turn")
    # get_times()

def p2_press(event):
    if p2_timer.running:
        p2_timer.pause()
        p1_timer.resume()
    else:
        print("Not your turn")
    # get_times()

def get_times():
    # os.system("cls")
    print("p1",p1_timer.get_clock())
    print("p2", p2_timer.get_clock())


def update_clock():
        if p1_timer.running:
            p1_clock_label.config(text=p1_timer.get_time_live())
        if p2_timer.running:
            p2_clock_label.config(text=p2_timer.get_time_live())
        root.after(1, update_clock)

def start_game(event):
    p1_timer.start()
    update_clock()

root.title("Python Chess Clock")
# root.geometry("1000x500")
fontStyle = tkFont.Font(family="Lucida Grande", size=100)
root.bind("<Shift_L>", p1_press)
root.bind("<Shift_R>", p2_press)
root.bind("<space>", start_game)

# p1_clock = StringVar()
# p1_clock.set(p1_timer.get_clock())
p1_clock_label = Label(root, text=p1_timer.get_clock(), font=fontStyle)
p1_clock_label.grid(row=0, column=0, pady=10, padx=100)
# fontStyle.configure(size=100)

# p2_clock = StringVar()
# p2_clock.set(p2_timer.get_clock())
p2_clock_label = Label(root, text=p2_timer.get_clock(), font=fontStyle)
p2_clock_label.grid(row=0, column=1, pady=10, padx=100)



root.mainloop()