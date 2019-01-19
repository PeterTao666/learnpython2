# 关于读取文件的练习
# 打开文件，三个字符一组读出内容，然后显示在屏幕上
# 每读一次，休息一秒钟
# 让程序暂停，可以使用提么下的sleep函数

import time

with open(r'test01.txt', 'r') as f:
    # read参数的单位是字符，可以理解成一个汉字就是一个字符
    strChar = f.read(3)
    while strChar:
        print(strChar)
        # sleep参数单位是秒
        time.sleep(1)
        strChar = f.read(3)

# 解释一下运行结果，为什么不是每行三个字符
# 作业：
# 使用read读取文件，每次读取一个，使用循环读完
# 尽量保持格式
with open(r'test01.txt', 'r') as f:
    strChar = f.read(1)
    while strChar:
        print(strChar)
        strChar = f.read(1)
