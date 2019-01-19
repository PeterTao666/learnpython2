import xml.etree.ElementTree as et

# 在内存中创建一个空的文档

etree = et.ElementTree()

e = et.ElementTree('Student')

etree.__setroot(e)

e_name = et.SubElement(e, 'Name')
e_name.text = "hahaha"

stree.write('v06.xml')