def hello():
    print("hello worid!")
f = hello
f()
hello()
print(id(f))
print(id(hello))
print(f.__name__)
print(hello.__name__)

# 现在由新的需求：
# 对hello功能进行拓展，每次打印hello之前打印当前系统时间
# 而实现这个功能又不能改动现有代码
# ==>使用装饰器