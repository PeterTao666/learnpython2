# 排序案列一

a = [234,22312,123,34,45,4,73,9]
al = sorted(a, reverse=True)
print(al)

# 排序案列2

a = [-43,23,45,6,-6,9,-88]
# 按照绝对值进行排序
# abs是求绝对值函数
# 即按照绝对值得倒序排列
al2 = sorted(a, key=abs, reverse=True)
print(al2)

# 排序案列三

astr = ['dana','Danan','Peter','jingjing']
str1 = sorted(astr)
print(str1)
str2 = sorted(astr, key=str.lower)
print(str2)


