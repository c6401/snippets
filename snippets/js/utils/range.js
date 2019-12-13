function* range(start = 0, end = 100, step = 1) {
    for (let i = start; i < end; i += step) {
        yield i;
    }
}
