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
        self.square_width = 20
        self.canvas = tk.Canvas(self.root, width=self.canvas_width, height=self.canvas_height)
        self.canvas.pack()

    def install(self):
        w, h = self.canvas_width // 2, self.canvas_height // 2
        sw = self.square_width
        for n in range(5):
            self.canvas.create_rectangle(w, h, w + sw, h + sw, fill="red", tags="rect")
            w = w + 10
            h = h + 10
        all_rect_ids = self.canvas.find_withtag("rect")
        print(all_rect_ids)
        x1, y1, x2, y2 = self.canvas.bbox("rect")
        print(x1, y1, x2, y2)
        rect_id = self.canvas.create_rectangle(x1, y1, x2, y2, fill="blue")
        self.canvas.tag_lower(rect_id)
        overlapped = self.canvas.find_overlapping(x1, y1, x2, y2)
        print(overlapped)

    def start(self):
        self.root.mainloop()


ex = Example()
ex.install()
ex.start()
