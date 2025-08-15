import matplotlib.pyplot as plt
from load_csv import load
import sys


def main():
    life_expectancy = load("day2/life_expectancy_years.csv")
    if life_expectancy is None:
        sys.exit(1)

    graph = life_expectancy.loc["France"]

    plt.plot(graph)
    plt.xticks(ticks=graph.index[::40])
    plt.title("France Life expectancy Projections")
    plt.ylabel("Life expectancy")
    plt.xlabel("Year")
    plt.show()


if __name__ == "__main__":
    main()
