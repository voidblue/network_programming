import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom

root = ET.Element('inventory')
cheese = ET.Element('cheese')
third = ET.Element('third')
name = ET.SubElement(cheese, 'name') #name태그를 생성하면서 cheese의 하위 엘리먼트에 넣는다.
name.text = 'Caerphilly'                #name변수 가장 안에 있는 name태그 안에 입력
root.append(cheese)                 #inventory(root)태그 안에 cheese태그를 넣는다.
root.append(third)

temp = ET.SubElement(root, 'temp')
root.remove(temp)                 #temp엘리먼트를 지운다.
ET.dump(root)


def xml_pprint(element):
    s = ET.tostring(element)
    print(minidom.parseString(s).toprettyxml())
    # element를 스트링 형태로 #보통 xml형태로 출력해라
cheese.attrib['id'] = 'c01'


xml_pprint(root)
# text = ET.tostring(cheese)
# print(text)     #us-ascii로 되어있어서 b'이 븥는다.
# text = ET.tostring(cheese, encoding = 'utf-8')
