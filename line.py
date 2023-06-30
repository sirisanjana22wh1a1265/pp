import tkinter.messagebox
from tkinter import *
win=Tk() #creating the main window and storing the window object in 'win'
win.title('Welcome') #setting title of the window
can=Canvas(win, width=500, height=300) #creating the canvas
l=can.create_line(100, 100, 200, 180,fill='green') #drawing an line 
can.pack()
win.mainloop()
