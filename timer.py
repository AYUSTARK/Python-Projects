import datetime
from tkinter import *
from tkinter import ttk
from tkinter import font

global endTime


def quit(*args):
    root.destroy()


def cant_wait():
    timeLeft = endTime - datetime.datetime.now()
    timeLeft = timeLeft - datetime.timedelta(microseconds=timeLeft.microseconds)
    txt.set(timeLeft)
    root.after(1000, cant_wait)


if __name__ == '__main__':
    root = Tk()
    root.attributes("-fullscreen", False)
    root.configure(background='black')
    root.bind("f", quit)
    endTime = datetime.datetime.now() + datetime.timedelta(days=2)
    root.after(1000, cant_wait)
    fnt = font.Font(family='Calibri', size=70, weight='bold')
    txt = StringVar()
    lbl = ttk.Label(root, textvariable=txt, font=fnt, foreground='white', background='black')
    lbl.place(relx=0.5, rely=0.5, anchor=CENTER)
    root.mainloop()
