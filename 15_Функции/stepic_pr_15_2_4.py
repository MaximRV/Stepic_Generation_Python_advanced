def greet(name, *args):
    return f"Hello, {' and '.join((name,) + args)}!"
