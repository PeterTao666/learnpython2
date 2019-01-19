from collections import Counter
c = Counter('abcdefabcdeabcdabcaba')
# 为什么下面结果不把以abcd···作为键值，而是以其中每一个字母作为键值
# 需要括号里内容为可迭代
print(c)

s = ['Peter','love','love','love','yuanyuan']
c = Counter(s)
print(c)