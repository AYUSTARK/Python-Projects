import pygame
import tkinter as tkr
from tkinter.filedialog import askdirectory
import os


def play():
    pygame.mixer.music.load(playList.get(tkr.ACTIVE))
    var.set(playList.get(tkr.ACTIVE))
    print("Playing")
    pygame.mixer.music.play()


def stop():
    pygame.mixer.music.stop()
    print("Stopped")


def pause():
    pygame.mixer.music.pause()
    print("paused")


def resume():
    pygame.mixer.music.unpause()
    print("resumed")


if __name__ == '__main__':
    musicPlayer = tkr.Tk()
    musicPlayer.title("MP3 Player")
    musicPlayer.geometry("450x350")
    directory = askdirectory()
    os.chdir(directory)
    songList = os.listdir()
    playList = tkr.Listbox(musicPlayer, font="Helvetica 12 bold", bg="yellow", selectmode=tkr.SINGLE)
    for item in songList:
        pos = 0
        playList.insert(pos, item)
        pos = pos + 1
    pygame.init()
    pygame.mixer.init()

    var = tkr.StringVar()

    button2 = tkr.Button(musicPlayer, width=5, height=3, font="Helvetica 12 bold", text="STOP", command=lambda: stop(),
                         bg="red", fg="white")
    button1 = tkr.Button(musicPlayer, width=5, height=3, font="Helvetica 12 bold", text="PLAY", command=lambda: play(),
                         bg="red", fg="white")
    button3 = tkr.Button(musicPlayer, width=5, height=3, font="Helvetica 12 bold", text="PAUSE", command=lambda: pause(),
                         bg="red", fg="white")
    button4 = tkr.Button(musicPlayer, width=5, height=3, font="Helvetica 12 bold", text="RESUME", command=lambda: resume(),
                         bg="red", fg="white")

    songtitle = tkr.Label(musicPlayer, font="Helvetica 12 bold", textvariable=var)

    songtitle.pack()
    button1.pack(fill="x")
    button2.pack(fill="x")
    button3.pack(fill="x")
    button4.pack(fill="x")
    playList.pack(fill="both", expand="yes")
    musicPlayer.mainloop()
