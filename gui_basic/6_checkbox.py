from tkinter import *

root = Tk()
root.title("Python GUI")
root.geometry("640x480") # width x height

checkvar = IntVar() # Check box saves the value as an integer
checkbox = Checkbutton(root, text="Do you like Python?", variable=checkvar)
checkbox.select() # auto select the check box
checkbox.deselect() # auto deselect the check box
checkbox.pack()

checkvar2 = IntVar() # Check box saves the value as an integer
checkbox2 = Checkbutton(root, text="Do you like Java?", variable=checkvar2)
checkbox2.pack()

def btncmd():
    print(checkvar.get()) # 0: not selected, 1: selected
    print(checkvar2.get()) # 0: not selected, 1: selected

btn = Button(root, text="click", command=btncmd)
btn.pack()

root.mainloop()