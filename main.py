from tkinter import *
from main_ui.main_element import Main_element
from aset.aset_img import Aset_img

class Main_window:
    def __init__(self):
        self.root = Tk()
        self.aset_img = Aset_img()
        icon = PhotoImage(file='aset/image/dnote_icon.png')
        self.root.iconphoto(True, icon)
        self.main_element = Main_element(self.root)     
                                                        
        self.widow_setup()
        self.main_element.menu_display()

    def widow_setup(self):
        self.root.geometry("600x650")
        self.root.title("D-Note")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = Main_window()
    app.run()