from functools import reduce
# 定义一个操作函数
# 加入操作函数只是相加
def myAdd(x,y):
    return x + y

# 对于列表[1,2,3,4,5]执行myAdd函数的reduce
rst = reduce(myAdd,[1,2,3,4,5])
print(rst)
