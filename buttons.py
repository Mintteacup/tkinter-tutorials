from tkinter import *

root = Tk()

def myClick():
    myLabel = Label(root, text="You Fool!")
    myLabel.pack()

myButton = Button(root, text="Don't Click the Button!", command=myClick, bg="#146C94")
myButton.pack() 

root.mainloop()
