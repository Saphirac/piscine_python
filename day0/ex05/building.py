import sys
from string import punctuation


def tracebacklimit():
    """Set tracebacklimit to 0 as to not have exceptions showing"""
    sys.tracebacklimit = 0


def main():
    """Count the characters, upper and lower letters, digits, punctuations
    marks and spaces of a given text"""
    tracebacklimit()

    if len(sys.argv) == 2:
        args = sys.argv[1]
    elif len(sys.argv) < 2:
        args = input("What is the text to count?\n")
    else:
        assert len(sys.argv) <= 2, "more than one argument"
        return 1

    print("The text contains", len(args), "characters:")
    print(sum(1 for c in args if c.isupper()), "upper letters")
    print(sum(1 for c in args if c.islower()), "lower letters")
    print(sum(1 for c in args if c in punctuation), "punctuation marks")
    print(sum(1 for c in args if c == " "), "spaces")
    print(sum(1 for c in args if c.isdigit()), "digits")


if __name__ == "__main__":
    main()
