from typing import Any


# This is a decorator with 2 wrapped function
# the first function lets you get what will be the limit and only serves to return the real decorator
# the second function, callLimiter is there to return the wrapper function
# the wrapper function, limit function is what actually does the work (it reimplaces what the real function would have done)
def callLimit(limit: int):
    """A decorator that adds a call limit to a function"""
    count = 0

    def callLimiter(function):
        def limit_function(*args: Any, **kwds: Any):
            nonlocal count
            if count < limit:
                count += 1
                return function(*args, **kwds)
            else:
                print("Error:", function, "call to many times")
                return None

        return limit_function

    return callLimiter


@callLimit(3)
def f(a, b):
    return a + b


@callLimit(1)
def g():
    print("g()")


def main():
    for i in range(3):
        print(f(1, 2))
        g()


if __name__ == "__main__":
    main()
