def ft_filter(f, iterable):
    f"""Reproduce filter function"""
    if f:
        return (x for x in iterable if f(x))
    else:
        return (x for x in iterable if x)


print(ft_filter.__doc__)
