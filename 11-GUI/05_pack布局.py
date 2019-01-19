# pack布局案例
import tkinter

baseFrame = tkinter.Tk()

btn1 = tkinter.Button(baseFrame, text='A')
btn1.pack(side=tkinter.LEFT, expand=tkinter.YES, fill=tkinter.Y)

btn2 = tkinter.Button(baseFrame, text='B')
btn2.pack(side=tkinter.TOP, expand=tkinter.YES, fill=tkinter.BOTH)

btn3 = tkinter.Button(baseFrame, text='C')
btn3.pack(side=tkinter.RIGHT, expand=tkinter.YES, fill=tkinter.NONE, anchor=tkinter.NE)

btn4 = tkinter.Button(baseFrame, text='D')
btn4.pack(side=tkinter.LEFT, expand=tkinter.NO, fill=tkinter.Y)

btn5 = tkinter.Button(baseFrame, text='E')
btn5.pack(side=tkinter.TOP, expand=tkinter.NO,fill=tkinter.BOTH)

btn6 = tkinter.Button(baseFrame, text='F')
btn6.pack(side=tkinter.BOTTOM, expand=tkinter.YES)

btn7 = tkinter.Button(baseFrame, text='G')
btn7.pack(anchor=tkinter.SE)

baseFrame.mainloop()