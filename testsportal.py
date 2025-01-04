#I wasn't sure how to make the buttons actually do something so the ''' chats are saying what the are supposed to do

import tkinter as tk
from window import MainWindow
from difficulty import Difficulty


class Questions(MainWindow,Difficulty):
    def __init__(self, MainWindow,Difficulty):

        '''
        if easy button gets clicked it opens the easy test
        if medium button gets clicked it opens the medium test
        if hard button gets clicked it opens the hard test
        if extreme button gets clicked it opens the extreme test
        if troll button gets clicked it opens the troll test
        '''
        
