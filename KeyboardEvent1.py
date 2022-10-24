"""
@author: plantec
"""
try:  # import as appropriate for 2.x vs. 3.x
    import tkinter as tk
    from tkinter import *
except:
    import Tkinter as tk
    from Tkinter import *

# montre comment lier une fonction (print_key) à n'importe quelle evenement clavier

class Example:
    def __init__(self):
        self.root = tk.Tk()

    def print_key(self, event):
        print(event.keysym, event.keycode, event.char)

    def start(self):
        self.root.bind("<Key>", self.print_key)
        self.root.mainloop()

ex = Example()
ex.start()
