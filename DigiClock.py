import datetime
from tkinter import *
from tkinter import ttk
from tkinter import font


def quit(*args):
    root.destroy()


def clock_time():
    time = datetime.datetime.now()
    time = time.strftime("%d-%m-%Y, %X")  # %D-%m-%Y, %H:%-M:%S")
    txt.set(time)
    root.after(1000, clock_time)


if __name__ == '__main__':
    root = Tk()
    root.attributes("-fullscreen", False)
    root.configure(background='white')
    root.bind("f", quit)
    root.after(1000, clock_time)
    fnt = font.Font(family='Calibri', size=70, weight='bold')
    txt = StringVar()
    lbl = ttk.Label(root, textvariable=txt, font=fnt, foreground='black', background='white')
    lbl.place(relx=0.5, rely=0.5, anchor=CENTER)
    root.mainloop()
