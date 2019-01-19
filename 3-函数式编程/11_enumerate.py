# enumerate 案例一
l1 = [11,22,33,44,55]
em = enumerate(l1)
l2 = [i for i in em]
print(l2)

# enumerate 案例二
em = enumerate(l1, start=100)
l2 = [i for i in em]
print(l2)
