"""
@author: plantec
"""
try:  # import as appropriate for 2.x vs. 3.x
    import tkinter as tk
except:
    import Tkinter as tk

# Une animation d'un rectangle qui se déplace horizontalement.
# Il faut connaitre les dimension du canvas pour rebrousser chemin arrivé à un bord du canvas.
# Cet exemple montre comment récupérer les dimensions (bbox) du canvas avec la fonction cget()
# Regardez la documentation, cget permet de récupérer d'autre informations utiles.

class Example:
    def __init__(self):
        self.root = tk.Tk()
        self.rect_id = None
        self.square_width = 50
        self.frame = tk.Frame(self.root, width=400, height=400)
        self.frame.pack(side="top", fill="both", expand=True)
        self.canvas = tk.Canvas(self.frame, width=400, height=400, bg="black")
        self.canvas.pack(side="top", fill="both", expand=True)
        self.dx = 50

    def install(self):
        w, h = int(self.canvas.cget("width")) // 2, int(self.canvas.cget("height")) // 2
        sw = self.square_width
        self.rect_id = self.canvas.create_rectangle(w, h, w + sw, h + sw, fill="red")

    def start_animation(self):
        self.canvas.after(0, self.animation)

    def animation(self):
        max_w = int(self.canvas.cget("width"))
        x1, y1, x2, y2 = self.canvas.bbox(self.rect_id)
        print(max_w, self.dx)
        if x2 > max_w:
            self.dx = -self.dx
        elif x1 < 0:
            self.dx = -self.dx
        self.canvas.move(self.rect_id, self.dx, 0)
        self.canvas.after(300, self.animation)

    def start(self):
        self.install()
        self.start_animation()
        self.root.mainloop()


ex = Example()
ex.start()
