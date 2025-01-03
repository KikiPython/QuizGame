import tkinter as tk
from window import MainWindow

#easy = ages 5-10, medium = ages 10-15, hard = ages 15-20, impossible = ages 20-30, troll = ages any

class Difficulty(MainWindow):

    def __init__(MainWindow,self,root):
        self.label = tk.Label(self.root, text="Hello! Please pick a difficulty:")
        self.label.pack()

        self.easy_button = tk.Button(self.root, text="Easy", command=self.MainWindow)
        self.easy_button.pack(pady=30)

        self.medium_button = tk.Button(self.root, text="Medium", command=self.MainWindow)
        self.medium_button.pack(pady=50)

        self.hard_button = tk.Button(self.root, text="Hard", command=self.MainWindow)
        self.hard_button.pack(pady=70)

        self.extreme_button = tk.Button(self.root, text="Extreme", command=self.MainWindow)
        self.extreme_button.pack(pady=90)

        self.troll_button = tk.Button(self.root, text="Troll", command=self.MainWindow)
        self.troll_button.pack(pady=110)