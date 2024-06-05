import lxml.html

tree = lxml.html.fromstring(____)
dict(tree.forms[0].fields)
