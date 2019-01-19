# sub替换的案例
import re

p = re.compile(r'(\w+) (\w+)')

s = "hello 123 wang 456 xiaojing, i love you"

rst = p.sub(r'Hello word', s)
print(rst)

