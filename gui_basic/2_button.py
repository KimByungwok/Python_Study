from tkinter import *
from tkinter import PhotoImage

root = Tk()
root.title("GUI Python")

# button widget
btn1 = Button(root, text="Button1")
btn1.pack()

btn2 = Button(root, padx=5, pady=10, text="Button2")
btn2.pack()

btn3 = Button(root, padx=10, pady=5, text="Button3")
btn3.pack()

btn4 = Button(root, width=10, height=3, text="Button4")
btn4.pack()

btn5 = Button(root, fg="red", bg="yellow", text="Button5")  # fg: 글자색, bg: 배경색
btn5.pack()

photo = PhotoImage(file="image/check.png")
btn6 = Button(root, image=photo)
btn6.pack()


def btncmd():
	print("Button is clicked")


btn7 = Button(root, text="Operating buttons", command=btncmd)
btn7.pack()

# root.geometry("720x480") # 가로 * 세로
# # root.geometry("720x480+1000+300") # 가로 * 세로 + x좌표 + y좌표 (컴퓨터 화면 기준 가운데)
#
# root.resizable(False, False) # x(가로), y(세로) 값 변경 불가 (창 크기 변경 불가)


root.mainloop()
