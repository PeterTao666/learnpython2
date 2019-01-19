# 事件的简单例子
import tkinter

def baseLabel(event):
    global baseFrame
    lb = tkinter.Label(baseFrame,text='谢谢点击！')
    lb.pack()

baseFrame = tkinter.Tk()

lb = tkinter.Label(baseFrame, text='模拟按钮')
# label绑定相应的消息和处理函数
# 自动获取左键点击，并启动相应的处理函数baseLabel
lb.bind("<Button-1>", baseLabel)
lb.pack()

baseFrame.mainloop()
