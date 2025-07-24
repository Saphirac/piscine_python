from typing import Any
import numbers


def mean(args):
    return sum(args) / len(args)


def median(args):
    s_args = sorted(args)
    n = len(args)
    return s_args[n // 2] if n % 2 else (s_args[n // 2] + s_args[n // 2 - 1]) / 2


def quartile(args):
    s_args = sorted(args)
    n = len(args)
    return [float(median(s_args[: (n + 1) // 2])), float(median(s_args[n // 2 :]))]


def variance(args):
    m = mean(args)
    n = len(args)
    #if you want the same result as 42 (but the formula is wrong) :
    #return 0.0 if n == 1 else sum((x - m) ** 2 for x in args) / n
    return 0.0 if n == 1 else sum((x - m) ** 2 for x in args) / (n - 1)


def std(args):
    return variance(args) ** 0.5


FUNCTIONS: Any = {
    "mean": mean,
    "median": median,
    "quartile": quartile,
    "std": std,
    "var": variance,
}


def ft_statistics(*args: Any, **kwargs: Any) -> None:
    """Apply the choosen function specified in the dict to the given tuple"""
    check_args = all(isinstance(arg, numbers.Number) for arg in args)
    for func in kwargs.values():
        if func in FUNCTIONS:
            if args and check_args:
                print(func, ":", FUNCTIONS[func](args))
            else:
                print("ERROR")
    return
