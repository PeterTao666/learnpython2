# 将一个列表里的每一个参数乘以10，重新生成一个新列表
l1 = [i for i in range(10)]
print(l1)
l2 = []
for i in l1:
    l2.append(i*10)
print(l2)

# 用map函数实现
def mulTen(n):
    return n*10

l3 = map(mulTen,l1)
print(l3)

for i in l3:
    print(i,end=',')

print()
l4 = [i for i in l3]
print(l4)
