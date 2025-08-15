from load_csv import load
import sys

def main():
    life_expectancy = load("day2/life_expectancy_years.csv")
    if life_expectancy is None:
        sys.exit(1)
    print("Loading dataset of dimensions", life_expectancy.shape, life_expectancy)


if __name__ == "__main__":
    main()
