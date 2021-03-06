def dt_intersect(start1, end1, start2, end2):
    start = max(start1, start2)
    end = min(end1, end2)
    if start < end:
        return start - end
    return datetime.timedelta()
