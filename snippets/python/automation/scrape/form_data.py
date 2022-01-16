import lxml.html

tree = lxml.html.fromstring(string)
dict(tree.forms[0].fields)
