import tkinter as tk
from PIL import Image, ImageTk
import cv2



class Game:
    def __init__(self):
       Home()

        

class Home():

    width=480
    height=853
    window = None
    def __init__(self):

        window = tk.Tk()
        self.window = window
        canvas = tk.Canvas(window,width=self.width,height=self.height)
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
        play_button = tk.Button(window,textvariable =play_text,command = lambda:self.playerSelection(),font ="Raleway",bg="#7385AE",height=2,width=20)
        play_button.grid(column=1,row=2)

        How_to_text = tk.StringVar()
        How_to_text.set("How To Play")
        How_to_button = tk.Button(window,textvariable =How_to_text,command = lambda:self.howToPlay(), font ="Raleway",bg="#7385AE",height=2,width=20)
        How_to_button.grid(column=1,row=3)


        window.mainloop()

    def playerSelection(self):
        self.window.destroy()
        select = PlayerSelection()
        self.window = select.window

    def howToPlay(self):
        self.window.destroy()
        how = HowToPlay()
        self.window=how.window


#Add a button to go back home in instructions !!

class HowToPlay:
    width=480
    height=480
    window = None
    def __init__(self):
        window = tk.Tk()
        self.window=window
        canvas = tk.Canvas(window,width=self.width,height=self.height)
        canvas.grid(columnspan=3,rowspan=4)

        logo = Image.open("SET.png")
        logo = logo.resize((200,100))
        logo = ImageTk.PhotoImage(logo)

        logo_label = tk.Label(image=logo)
        logo_label.image = logo
        logo_label.grid(column=1,row=0)

        instructions = tk.Label(window,text="Instructions en cours d'ajout ...",font="Raleway")
        instructions.grid(columnspan=3,column=0,row=1)


class PlayerSelection:
    width=480
    height=600
    window = None
    player1= None
    player2= None
    def __init__(self):
        
        window = tk.Tk()
        self.window=window
        canvas = tk.Canvas(window,width=self.width,height=self.height)
        canvas.grid(columnspan=3,rowspan=6)

        logo = Image.open("SET.png")
        logo = logo.resize((200,100))
        logo = ImageTk.PhotoImage(logo)

        logo_label = tk.Label(image=logo)
        logo_label.image = logo
        logo_label.grid(column=1,row=0)


        lab1 = tk.Label(window,text="Player 1 :",font="Raleway")
        lab1.grid(columnspan=3,column=0,row=1)

        self.player1 = tk.StringVar()
        self.player1.set("Player Name")
        entree = tk.Entry(window, textvariable=self.player1, width=30)
        entree.grid(columnspan=3,column=0,row=2)

        lab2 = tk.Label(window,text="Player 2 :",font="Raleway")
        lab2.grid(columnspan=3,column=0,row=3)

        self.player2 = tk.StringVar()
        self.player2.set("Player Name")
        entree2 = tk.Entry(window, textvariable=self.player2, width=30)
        entree2.grid(columnspan=3,column=0,row=4)


        How_to_text = tk.StringVar()
        How_to_text.set("Go!")
        How_to_button = tk.Button(window,textvariable =How_to_text,command = lambda:self.startGame(), font ="Raleway",bg="#7385AE",height=2,width=20)
        How_to_button.grid(column=1,row=5)
        
    def startGame(self):
        print("player 1 : {}".format(self.player1.get()))
        print("player 2 : {}".format(self.player2.get()))


#class GameWindow:


g = Game()