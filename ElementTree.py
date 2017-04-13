import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom

root = ET.Element('inventory')
cheese = ET.Element('cheese')
third = ET.Element('third')
name = ET.SubElement(cheese, 'name')
name.text = 'Caerphilly'
root.append(cheese)
root.append(third)

temp = ET.SubElement(root, 'temp')
root.remove(temp)   #'temp'로하면 오류
ET.dump(root)


def xml_pprint(element):
    s = ET.tostring(element)
    print(minidom.parseString(s).toprettyxml())
    # element를 스트링 형태로 #보통 xml형태로 출력해라
cheese.attrib['id'] = 'c01'


xml_pprint(cheese)
text = ET.tostring(cheese)
print(text)     #us-ascii로 되어있어서 b'이 븥는다.
text = ET.tostring(cheese, encoding = 'utf-8')
