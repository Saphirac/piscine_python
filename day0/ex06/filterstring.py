import sys
from ft_filter import ft_filter


def main():
    """Filter a string to get word with a len > n"""
    assert len(sys.argv) == 3
    try:
        n = int(sys.argv[2])
    except ValueError:
        n = None
    assert n is not None
    words_list = sys.argv[1].split(" ")

    newlist = ft_filter(lambda a: len(a) > n, words_list)
    print(list(newlist))


if __name__ == "__main__":
    sys.tracebacklimit = 0
    try:
        main()
    except AssertionError as e:
        print(f"{e.__class__.__name__}: the arguments are bad")
