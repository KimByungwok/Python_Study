from tkinter import *

root = Tk()
root.title("GUI Python")
root.geometry("720x480") # 가로 * 세로

txt = Text(root, width=30, height=5) # line
txt.pack()
txt.insert(END, "write here")

e = Entry(root, width=30) # no line
e.pack()
e.insert(0, "write one line here")

def btncmd():
	# content output
	print(txt.get("1.0", END)) # 1: first line, 0: first column from end to END
	print(e.get())
	# content delete
	txt.delete("1.0", END)
	e.delete(0, END)

btn = Button(root, text="click", command= btncmd)
btn.pack()

root.mainloop()
