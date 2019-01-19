from collections import defaultdict
# lamda表达式，直接返回字符串
func = lambda:"404"
d2 = defaultdict(func)

d2["one"] = 1
d2["two"] = 2
print(d2['one'])
print(d2['four'])
