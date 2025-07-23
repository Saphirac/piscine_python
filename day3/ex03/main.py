from ft_calculator import calculator
import sys

def main():
    v1 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
    v1 + 5
    print("---")
    print(calculator.__add__.__doc__)
    v2 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
    v2 * 5
    print(calculator.__mul__.__doc__)
    print("---")
    v3 = calculator([10.0, 15.0, 20.0])
    v3 - 5
    v3 / 5
    v3 / 0

if __name__ == "__main__":
    sys.tracebacklimit = 0
    try:
        main()
    except ZeroDivisionError as e:
        print(f"An error occurred: {e}")
