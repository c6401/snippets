from lxml.builder import ElementMaker
from lxml import etree

E = ElementMaker()

root = E.root(
    E.child1("This is child 1"),
    E.child2("This is child 2", attribute="value")
)

xml_string = etree.tostring(root, pretty_print=True).decode()

print(xml_string)