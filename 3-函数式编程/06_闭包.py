# 闭包常见坑
def count():
    # 定义列表，列表里存放的是定义的函数
    fs = []
    for i in range(1,4):
        # 定义了一个函数f
        # f是一个闭包结构
        def f():
            return i*i
        fs.append(f)
    return fs

f1,f2,f3 = count()
print(f1())
print(f2())
print(f3())

# 修改上述函数
def count2():
    def f(j):
        def g():
            return j*j
        return g
    fs1 = []
    for i in range(1,4):
        fs1.append(f(i))
    return fs1
f1,f2,f3 = count2()
print(f1())
print(f2())
print(f3())



