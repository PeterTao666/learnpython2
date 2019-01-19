# 导入相关包
import re

# 查找数字
# r表示字符串不转义
p = re.compile(r'\d+')

# 在字符串中进行查找，按照规则p指定的正则进行查找
# 返回结果是None表示没有找到，否则返回Match对象
m = p.match("one12twothree33456four78nine", 3, 26)

print(m)

# 上述代码说明问题
# 1.match可以输入参数表示起始位置
# 2.查找到结果只包含一个，表示第一次进行匹配成功的内容

print(m[0])
print(m.start(0))
print(m.end(0))

# 案列二
import re
# I表示忽略大小写
p = re.compile(r'([a-z]+) ([a-z])', re.I)

n = p.match("I am really love yuanyuan")
print(n)

print(n.groups())

print(n.group(1))
print(n.start(1))
print(n.end(1))
