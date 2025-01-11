import sys
from string import punctuation


def main():
    """Count the characters, upper and lower letters, digits, punctuations
    marks and spaces of a given text"""

    assert len(sys.argv) <= 2, "more than one argument"
    if len(sys.argv) == 2:
        args = sys.argv[1]
    else:
        args = input("What is the text to count?\n")

    print("The text contains", len(args), "characters:")
    print(sum(1 for c in args if c.isupper()), "upper letters")
    print(sum(1 for c in args if c.islower()), "lower letters")
    print(sum(1 for c in args if c in punctuation), "punctuation marks")
    print(sum(1 for c in args if c == " "), "spaces")
    print(sum(1 for c in args if c.isdigit()), "digits")


if __name__ == "__main__":
    sys.tracebacklimit = 0
    try:
        main()
    except AssertionError as e:
        print(f"{e.__class__.__name__}: the arguments are bad")
