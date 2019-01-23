from urllib import request
from bs4 import BeautifulSoup

url = 'http://www.baidu.com'

rsp = request.urlopen(url)
content = rsp.read()

soup = BeautifulSoup(content, 'lxml')

# bs自动转码
content = soup.prettify()
#print(content)
print("###" * 10)
print(soup.head)
print("###" * 10)
print(soup.meta)
print("###" * 10)
print(soup.link)
print(soup.link.name)
print(soup.link.attrs)
print("###" * 10)
print(soup.title)
print(soup.title.name)
print(soup.title.attrs)
print(soup.title.string)
print("###" * 10)
print(soup.name)
print(soup.attrs)
print(soup.sring)

print("###" * 20)
for node in soup.head.contents:
    if node.name == "meta":
        print(node)
    if node.name == "title":
        print(node.string)
print("###" * 20)
tags = soup.find_all(name='meta')
print(tags)
print("###" * 20)
import re
tags = soup.find_all(re.compile('^me'), content="always")
for tag in tags:
    print(tag)

