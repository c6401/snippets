r = random.Random()
r.seed("...")
items = [i for i in itertools.product(letters, repeat=...)]
r.shuffle(items)
