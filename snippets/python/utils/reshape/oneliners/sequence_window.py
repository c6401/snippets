def window(seq, size=2): return (seq[i: i + size] for i in range(len(seq) - size + 1))
