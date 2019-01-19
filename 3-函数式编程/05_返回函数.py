# 函数作为返回值返回，被返回的函数在函数体内定义

def myF2():
    def myF3():
        return 3
    return myF3()

# 使用上面定义
# 调用myF2，返回一个函数myF3,赋值给f3

f3 = myF2()
print(type(f3))
print(f3)
print('***')
myF2()

# 复杂返回函数的列子
# args:参数列表

def myF4(*args):
    def myF5():
        rst = 0
        for n in args:
            rst += n
        return rst
    return myF5
f5 = myF4(1,2,3,4,5,6,7,8,9,0)
# f5的调用方式
f5()

f6 = myF4(10,20,30,40,50)
f6()




