import functools
# 实现上面int16的功能
int16 = functools.partial(int,base=16)
a = int16("12345")
print(a)