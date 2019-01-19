# 设置Label的例子
import tkinter

base = tkinter.Tk()
base.wm_title("Label Test")
# 支持属性很多background，front，underLine等
# 第一个参数，指定所属
lb1 = tkinter.Label(base, text="Python AI")
lb1.pack()

lb2 = tkinter.Label(base, text="绿色背景", background='green')
lb2.pack()

lb3 = tkinter.Label(base, text="蓝色背景", background='blue')
lb3.pack()

base.mainloop()



