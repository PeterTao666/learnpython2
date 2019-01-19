# 任务：对hello函数进行功能扩展，每次执行hello之前打印当前时间
import time

# 高阶函数，把函数作为参数
def printTime(f):
    def wrapper(*args,**kwargs):
        print   ("Time:",time.ctime())
        return f(*args,**kwargs)
    return wrapper

# 上面定义了装饰器，使用的时候需要用到@，此符号是python的语法糖

@printTime
def hello():
    print("Hello world!")

hello()
'''
hello = printTime(hello)
hello()
'''