"""
@author: plantec
"""
try:  # import as appropriate for 2.x vs. 3.x
    import tkinter as tk
    from tkinter import *
except:
    import Tkinter as tk
    from Tkinter import *



class Example:
    def __init__(self):
        self.root = tk.Tk()
        self.canvas_width = 600
        self.canvas_height = 400
        self.pim = tk.PhotoImage(file='alien.gif')
        self.canvas = tk.Canvas(self.root, width=self.canvas_width, height=self.canvas_height)
        self.canvas.pack()

    def install(self):
        self.canvas.create_image(100, 100, image=self.pim, tags="image")

    def start(self):
        self.install()
        self.root.mainloop()


ex = Example()
ex.start()
