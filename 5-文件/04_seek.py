# seek案例
# 打开文件后，从第五个字节处开始读取

# 打开读写指针在0出，即文件的开头
with open(r'test01.txt', 'r') as f:
    # seek移动单位
    f.seek(4, 0)
    strChar = f.read()
    print(strChar)