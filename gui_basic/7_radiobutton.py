from tkinter import *

root = Tk()
root.title("Python GUI")
root.geometry("640x480") # width x height

Label(root, text="Select the menu").pack()

burger_var = IntVar() # this variable saves the value of int type
button_burger1 = Radiobutton(root, text="Hamburger", value=1, variable=burger_var)
button_burger1.select() # auto select the check box
button_burger2 = Radiobutton(root, text="Cheeseburger", value=2, variable=burger_var)
button_burger3 = Radiobutton(root, text="Chickenburger", value=3, variable=burger_var)

button_burger1.pack()
button_burger2.pack()
button_burger3.pack()

Label(root, text="Select the drink").pack()

drink_var = StringVar() # this variable saves the value of string type
button_drink1 = Radiobutton(root, text="Coke", value=1,variable=drink_var)
button_drink1.select() # auto select the check box
button_drink2 = Radiobutton(root, text="Sprite", value=2,variable=drink_var)

button_drink1.pack()
button_drink2.pack()


def btncmd():
    print(burger_var.get()) # hamburger is selected print value
    print(drink_var.get()) # drink is selected print value
btn = Button(root, text="order", command=btncmd)
btn.pack()

root.mainloop()