

import os
from tkinter import *
os.system('clear') 
root=Tk()
root.title("wow tkinter")
root.geometry('400x600')
def do():
	dolabel = Label(root,text="hello "+ myText. get())
	dolabel.pack()
mylabel = Label(root , text="ur name please")
mylabel.pack()
myText = Entry(root, width="30")
myText.pack()
myButton = Button(root, text="commit",command=do)
myButton.pack()
root.mainloop()
