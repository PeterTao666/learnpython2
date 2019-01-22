from lxml import etree

# 只能读取xml格式内容，html报错
html = etree.parse("./28_xml.xml")

rst = etree.tostring(html, pretty_print=True)
print(rst)