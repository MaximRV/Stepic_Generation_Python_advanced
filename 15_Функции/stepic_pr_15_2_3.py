def mean(*args):
    objects = [arg for arg in args if isinstance(arg, (int, float)) and not isinstance(arg, bool)]
    if objects:
        return sum(objects) / len(objects)
    return 0.0
