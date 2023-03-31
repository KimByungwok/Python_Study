from tkinter import *

root = Tk()
root.title("GUI Python")
root.geometry("720x480") # 가로 * 세로
# root.geometry("720x480+1000+300") # 가로 * 세로 + x좌표 + y좌표 (컴퓨터 화면 기준 가운데)

root.resizable(False, False) # x(가로), y(세로) 값 변경 불가 (창 크기 변경 불가)


root.mainloop()
