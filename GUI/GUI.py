import tkinter as tk
from PIL import Image, ImageTk
import cv2
from utils import *

window = tk.Tk()

canvas = tk.Canvas(window,width=480,height=853)
canvas.grid(columnspan=3,rowspan=4)

logo = Image.open("SET.png")
logo = logo.resize((300,150))
logo = ImageTk.PhotoImage(logo)

logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=1,row=0)

instructions = tk.Label(window,text="The Family Game Of Visual Perception",font="Raleway")
instructions.grid(columnspan=3,column=0,row=1)

play_text = tk.StringVar()
play_text.set("Play")
play_button = tk.Button(window,textvariable =play_text,command = lambda:playWindow(), font ="Raleway",bg="#7385AE",height=2,width=20)
play_button.grid(column=1,row=2)

How_to_text = tk.StringVar()
How_to_text.set("How To Play")
How_to_button = tk.Button(window,textvariable =How_to_text,command = lambda:howToPlay(), font ="Raleway",bg="#7385AE",height=2,width=20)
How_to_button.grid(column=1,row=3)


window.mainloop()