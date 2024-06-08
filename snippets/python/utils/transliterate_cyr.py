mapping = dict(zip("абвгдезиклмнопрстуфхьыйёжцчшщъюя", (*"abvgdeziklmnoprstufh'y", *"ii yo zh ts ch sh sh' '' yu ya".split())))
def transliterate(text): return ''.join(mapping.get(c, c) for c in text)
