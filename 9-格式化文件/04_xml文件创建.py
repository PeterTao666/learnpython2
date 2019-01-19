import xml.etree.ElementTree as et

stu = et.Element("Studnet1")

name = et.SubElement(stu, 'Name')
name.attrib = {'lang', 'en'}
name.text = 18

et.dump(stu)