from tkinter import *

class Main_frame:
    def __init__(self):
        self.frame_top = Frame(relief='sunken', bd=1)
        self.frame_top.pack(anchor='w', fill='x')

        self.frame_midle = Frame()
        self.frame_midle.pack(anchor='w', fill='x')

        self.frame_textbox = Frame()
        self.frame_textbox.pack(expand=True, fill="both")

        self.frame_bottom = Frame()
        self.frame_bottom.pack(fill='x')