from tkinter import *

root = Tk()

def myClick():
    myLabel = Label(root, text= f"Nice to meet you {e.get()}!")
    myLabel.pack()

myButton = Button(root, text="Enter Your Name", command=myClick, bg="#146C94")
myButton.pack() 

e = Entry(root, width=50)
e.pack()
e.insert(0, "Enter your name")

root.mainloop()