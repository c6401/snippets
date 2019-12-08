import pyexiv2

def set_tags(file, tags):
    metadata = pyexiv2.ImageMetadata(file)
    metadata.read()
    key = 'Iptc.Application2.Keywords'
    metadata[key] = pyexiv2.IptcTag(key, tags)
    metadata.write()
