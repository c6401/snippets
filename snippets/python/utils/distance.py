def distance(a, b):
    return sum((an - bn) ** 2 for an, bn in zip(a, b)) ** 0.5
