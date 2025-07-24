from load_csv import load


def main():
    life_expectancy = load("day2/life_expectancy_years.csv")

    print(life_expectancy)


if __name__ == "__main__":
    main()
