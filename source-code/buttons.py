try:  # import as appropriate for 2.x vs. 3.x
    import tkinter as tk
    from tkinter import *
except:
    import Tkinter as tk
    from Tkinter import *

root =  tk.Tk()
frame = Frame(root)
frame.pack()
    
def commandClbWithArg(something):
    print('plop :', something)

bottomframe = Frame(root)
bottomframe.pack( side = BOTTOM)

redbutton = Button(frame, text="Red", fg="red", command=lambda: commandClbWithArg('red') )
redbutton.pack( side = LEFT)

greenbutton = Button(frame, text="Brown", fg="brown", command=lambda: commandClbWithArg('brown') )
greenbutton.pack( side = LEFT )

bluebutton = Button(frame, text="Blue", fg="blue", command=lambda: commandClbWithArg('blue'))
bluebutton.pack( side = LEFT )

blackbutton = Button(bottomframe, text="Black", fg="black", command=lambda: commandClbWithArg('black') )
blackbutton.pack( side = BOTTOM)

root.mainloop()
