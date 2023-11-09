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
        self.rect_id = None
        self.canvas_width = 600
        self.canvas_height = 400
        self.square_width = 50
        self.canvas = tk.Canvas(self.root, width=self.canvas_width, height=self.canvas_height)
        self.canvas.pack()

    def install(self):
        w, h = self.canvas_width // 2, self.canvas_height // 2
        sw = self.square_width
        self.rect_id = self.canvas.create_rectangle(w, h, w + sw, h + sw, fill="red")
        print(self.canvas.coords(self.rect_id))

    def start(self):
        self.root.mainloop()


ex = Example()
ex.install()
ex.start()
