from tkinter import *  # pip install tkinter
from PIL import Image, ImageTk, ImageSequence  # pip install Pillow
import time
import pygame  # pip install pygame
from pygame import mixer

mixer.init()

root = Tk()
root.geometry("800x600")
root.attributes('-topmost', 1)

mixer.music.load("intro_music.mp3")
mixer.music.play()

def play_gif():
    global img
    img = Image.open("AI_visualization.gif")

    lbl = Label(root)
    lbl.place(x=0, y=0)

    def update_frame(ind):
        img.seek(ind)
        frame = img.copy()
        frame = frame.resize((800, 600))
        tk_img = ImageTk.PhotoImage(frame)

        lbl.config(image=tk_img)
        lbl.image = tk_img
        ind += 1
        if ind == img.n_frames:
            ind = 0
        root.after(50, update_frame, ind)
    root.after(0, update_frame, 0)

root.after(4000, root.destroy)

play_gif()
root.mainloop()
