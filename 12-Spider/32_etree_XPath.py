from lxml import etree

# 只能读取xml格式内容，html报错
html = etree.parse("./28_xml.xml")

rst = html.xpath('//book')
print(type(rst))
print(rst)

# xpath的意思是，查找带有category属性值为sport的book元素
rst = html.xpath('//book[@category="sport"]')
print(type(rst))
print(rst)

# xpath的意思是，查找带有category属性值为sport的book元素下的year元素
rst = html.xpath('//book[@category="sport"]/year')
print(rst)
print(type(rst))
rst = rst[0]
print(type(rst))
print(rst.tag)
print(rst.text)