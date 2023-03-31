from tkinter import *
from tkinter import PhotoImage

root = Tk()
root.title("GUI Python")
root.geometry("640x480")

label1 = Label(root, text="hi nice to meet you")
label1.pack()

photo = PhotoImage(file="image/check.png")
label2 = Label(root, image=photo)
label2.pack()

def change():
	label1.config(text="See you again")

	global photo2 # garbage collection head off
	photo2 = PhotoImage(file="image/close.png")
	label2.config(image=photo2)

btn = Button(root, text="click", command=change)
btn.pack()

root.mainloop()
