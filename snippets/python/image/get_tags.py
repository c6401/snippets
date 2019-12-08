import pyexiv2

def get_tags(file):
    metadata = pyexiv2.ImageMetadata(file)
    metadata.read()
    tag = metadata.get('Iptc.Application2.Keywords')
    return tag.value if tag else []
