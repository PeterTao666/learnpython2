import re

p = re.compile(r'\d+')

m = p.search("one12two34three567four")

print(m.group())

rst = p.findall("one12two34three567four")
print(type(rst))

print(rst)
