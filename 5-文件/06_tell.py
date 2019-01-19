# tell函数举例：
with open(r'test01.txt', 'r') as f:
    strChar = f.read(3)
    pos = f.tell()

    while strChar:
        print(pos)
        print(strChar)

        strChar = f.read(3)
        pos = f.tell()

# 以下结果说明：
# tell的fanhu返回数字的单位是byte
# read是以字符为单位