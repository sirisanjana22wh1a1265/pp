import tkinter.messagebox
from tkinter import *
win=Tk() #creating the main window and storing the window object in 'win'
win.title('Welcome') #setting title of the window
can=Canvas(win, width=500, height=300) #creating the canvas
can.create_oval(100, 100, 200, 200) #drawing an oval 
can.pack()
win.mainloop() 
