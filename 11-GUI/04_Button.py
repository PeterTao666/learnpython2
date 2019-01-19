# Button的案例

import tkinter

def showLabel():
    global baseFrame
    # 在函数中定义了一个Label
    # Label的父组件是baseFrame
    lb = tkinter.Label(baseFrame, text='显示Label')
    lb.pack()

baseFrame = tkinter.Tk()
# 生成一个按钮
# command参数指示，当按钮按下的时候，执行哪个函数
btn = tkinter.Button(baseFrame, text='Show Label', command=showLabel)
btn.pack()

baseFrame.mainloop()