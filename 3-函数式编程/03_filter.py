# filter 案列
# 对一个列表，对其进行过滤，偶数组成的一个新数列
# 需要义过滤函数
# 过滤函数要求有输入，返回布尔值

def isEven(a):
    return a % 2 == 0
l = [3,4,56,3,2,3,4556,67,4,4,3,23455,43]

rst = filter(isEven,l)
# 返回的filter内容是一个可迭代对象
print(type(rst))
print(rst)

print([i for i in rst])

a = list(rst)
print(a)
