# 新建一个函数，此函数是默认输入的字符串是16进制数字
# 把此字符串返回十进制的数字
def int16(x,base=16):
    return int(x,base)
int16("12345")