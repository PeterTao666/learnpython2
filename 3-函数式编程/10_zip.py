# zip 案列
l1 = [1,2,3,4,5]
l2 = [11,22,33,44,55]
z = zip(l1,l2)
print(type(z))
print(z)
for i in z:
    print(i)

# zip 案列二
l1 = ["wangwang","mingyue","yyt"]
l2 = [89,23,78]
z = zip(l1,l2)
for i in z:
    print(i)
## 考虑下面结果，为什么会为空
l3 = [i for i in z]
print(l3)

