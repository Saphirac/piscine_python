from time import sleep
from tqdm import tqdm


def ft_tqdm(lst):
    def my_print(i, n):
        print(f"{int(100 * i / n)}% [{'=' * int(50 * i / n)}] {i}/{n}", end="\r")

    n = len(lst)
    for i, x in ft_enumerate(lst):
        my_print(i, n)
        yield x
    my_print(n, n)


def ft_enumerate(lst):
    i = 0
    for x in lst:
        yield i, x
        i += 1


def main():
    """tester"""
    # for elem in tqdm(range(333)):
    #     sleep(1)
    for elem in ft_tqdm(range(333)):
        sleep(0.005)
    print()


if __name__ == "__main__":
    # sys.tracebacklimit = 0
    # try:
    main()
    # except AssertionError as e:
    #     print(f'{e.__class__.__name__}: the arguments are bad')
