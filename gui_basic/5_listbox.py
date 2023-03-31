from tkinter import *

root = Tk()
root.title("GUI Python")
root.geometry("720x480") # 가로 * 세로

listbox = Listbox(root, selectmode="extended", height=0) # selectmode="extended" : Multiple choices available, height=3 : show 3 items
listbox.insert(0, "사과")
listbox.insert(1, "딸기")
listbox.insert(2, "바나나")
listbox.insert(END, "수박")
listbox.insert(END, "포도")
listbox.pack()

def btncmd():
	# delete
	# listbox.delete(0) # Delete the first item

	# Check the number
	# print("The number of items selected : ", listbox.size(), "items")

	# Check Item
	# print("Items from 1 to 3 : ", listbox.get(0, 2))

	# Check the selected item (index number returned)
	print("Selected item : ", listbox.curselection())


btn = Button(root, text="click", command=btncmd)
btn.pack()

root.mainloop()
