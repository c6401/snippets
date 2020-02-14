def slices(seq, number):
    size, num_of_large = divmod(len(seq), number)
    for offset in range(0, num_of_large*(size+1), size+1):
        yield seq[offset:offset+size+1]
    for offset in range(num_of_large*(size+1), len(seq), size):
        yield seq[offset:offset+size]
