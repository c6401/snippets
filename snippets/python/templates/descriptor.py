class Descriptor:
    def __get__(self, obj, objtype=None):
        value = obj._attr
        return value

    def __set__(self, obj, value):
        obj._attr = value
