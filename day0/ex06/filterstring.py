import sys
from ft_filter import ft_filter

x = lambda a : a * 5

def  is_upper(str):
    if str.isupper() == True:
        return True
    return False

def main():
    assert len(sys.argv) == 3
    test_len = lambda a, b: len(a) > b
    try:
        n = int(sys.argv[2])
    except ValueError:
        n = None
    assert n is not None
    words_list = sys.argv[1].split(" ")

    newlist = [x for x in words_list if test_len(x, n)]
    print(newlist)

if __name__ == "__main__":
    sys.tracebacklimit = 0
    try:
        main()
    except AssertionError as e:
        print(f'{e.__class__.__name__}: the arguments are bad')
