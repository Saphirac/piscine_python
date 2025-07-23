from ft_calculator import calculator
import sys

def main():
    a = [5, 10, 2]
    b = [2, 4, 3]
    calculator.dotproduct(a, b)
    calculator.add_vec(a,b)
    calculator.sous_vec(a,b)


if __name__ == "__main__":
    sys.tracebacklimit = 0
    main()
