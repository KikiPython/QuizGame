#I wasn't sure how to make the buttons actually do something so the "#" chats are saying what the are supposed to do

import tkinter as tk
from window import MainWindow
from difficulty import Difficulty

#window opens by the easy button

class Easy(self):
    def __init__(self):

        self.root = root
        self.root.geometry("500x500")
        self.root.title("Easy Quiz")

    def Question_one(self):

        self.label = tk.Label(self.root,text="What is 35 + 47?")
        self.label.pack()

        self.incorrectbutton_one = tk.Button(self.root,text="72")
        self.incorrectbutton_one.pack(pady=10)
        self.correctbutton_two = tk.Button(self.root,text="82")
        self.correctbutton_two.pack(pady=30)
        self.incorrectbutton_three = tk.Button(self.root,text="103")
        self.incorrectbutton_three.pack(pady=50)
        self.incorrectbutton_four = tk.Button(self.root,text="73")
        self.incorrectbutton_four.pack(pady=70)

        #if answer is correct it moves on, if answer is incorrect, nothing will happen

    def Question_two(self):

        self.label = tk.Label(self.root,text="What is 7 * 3?")
        self.label.pack()


        self.incorrectbutton_five = tk.Button(self.root,text="10")
        self.incorrectbutton_five.pack(pady=10)
        self.incorrectbutton_six = tk.Button(self.root,text="17")
        self.incorrectbutton_six.pack(pady=30)
        self.correctbutton_seven = tk.Button(self.root,text="21")
        self.correctbutton_seven.pack(pady=50)
        self.incorrectbutton_eight = tk.Button(self.root,text="73")
        self.incorrectbutton_eight.pack(pady=70)

        #if question is correct it moves on, if question is incorrect, the test will reset, and so will happen to the rest of the questions

    def Question_three(self):

        self.label = tk.Labelself.root,text=("What is the first step of the water cycle?")
        self.label.pack()


        self.incorrectbutton_five = tk.Button(self.root,text="Evacuation")
        self.incorrectbutton_five.pack(pady=10)
        self.incorrectbutton_six = tk.Button(self.root,text="Precipitation")
        self.incorrectbutton_six.pack(pady=30)
        self.incorrectbutton_seven = tk.Button(self.root,text="Condensation")
        self.incorrectbutton_seven.pack(pady=50)
        self.correctbutton_eight = tk.Button(self.root,text="Evaporation")
        self.correctbutton_eight.pack(pady=70)

        #if the question is incorrect, the quiz will now end and show the ending screen

    def Ending_Screen(self):

        self.label = tk.Labelself.root,text=("You Win!")
        self.label.pack()

if __name__ == "__main__":
    main()
