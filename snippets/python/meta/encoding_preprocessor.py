import codecs

def codec(encoding):
    if encoding == 'preprocessor':
        return codecs.CodecInfo(
            name='preprocessor',
            encode=lambda input, errors='strict': (input, len(input)),
            decode=lambda input, errors='strict': (input, len(input)),
        )
