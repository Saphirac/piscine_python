def ft_filter(f, iterable):
    if f:
        return (x for x in iterable if f(x))
    else:
        return (x for x in iterable if x)
