from time import sleep
from tqdm import tqdm
from typing import Iterator


def ft_enumerate(lst):
    """My own enumerate"""
    i = 0
    for x in lst:
        yield i, x
        i += 1


def ft_tqdm(lst: range) -> Iterator[int]:
    """Generate a progress bar for the given function"""

    def my_print(i, n):
        print(f"{int(100 * i / n)}% [{'=' * int(50 * i / n)}>] {i}/{n}", end="\r")

    n = len(lst)
    for i, x in ft_enumerate(lst):
        my_print(i, n)
        yield x
    my_print(n, n)


def main():
    """tester for tqdm function"""
    for elem in ft_tqdm(range(333)):
        sleep(0.005)
    print()
    for elem in tqdm(range(333)):
        sleep(0.005)
    print()
    # for elem in ft_tqdm():
    #     sleep(0.005)
    # print()
    # for elem in tqdm():
    #     sleep(0.005)
    # print()


if __name__ == "__main__":
    # sys.tracebacklimit = 0
    try:
        main()
    except TypeError as e:
        print(f"{e.__class__.__name__}: invalid given argument")
