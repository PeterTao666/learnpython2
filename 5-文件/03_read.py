# read案列
with open(r'test01.txt', 'r') as f:
    strChar = f.read(1)
    print(len(strChar))
    print(strChar)

# 作业：
# 使用read读取文件，每次读取一个，使用循环读完
# 尽量保持格式
with open(r'test01.txt', 'r') as f:
    strChar = f.read(1)
    while strChar:
        print(strChar)
        strChar = f.read(1)



