# Label 的例子
import tkinter
base = tkinter.Tk()
# 负责标题
base.wm_title("Label Test")

lb = tkinter.Label(base, text='Python Label')
# 给组件指定布局
lb.pack()

base.mainloop()