import matplotlib.pyplot as plt
from load_csv import load
import matplotlib.ticker as mticker
import sys


def parse_pop(x):
    """Change the letters to corresponding numbers"""
    if x[-1] == "k":
        return float(x[:-1]) * 10**3
    if x[-1] == "M":
        return float(x[:-1]) * 10**6
    if x[-1] == "B":
        return float(x[:-1]) * 10**9
    else:
        return float(x)


def main():
    population = load("day2/population_total.csv")
    if population is None:
        sys.exit(1)

    france = population.loc["France"]
    senegal = population.loc["Senegal"]

    france = france.loc[:"2050"].map(parse_pop)
    senegal = senegal.loc[:"2050"].map(parse_pop)

    fig, ax = plt.subplots()

    ax.plot(france, label="France")
    ax.plot(senegal, label="Senegal")

    ax.set_xticks(ticks=senegal.index[::40])
    ax.yaxis.set_major_formatter(
        mticker.FuncFormatter(
            lambda x, y: f"{int(x / 1000000)}M" if x >= 1000000 else str(x)
        )
    )
    ax.set_title("France vs Senegal population comparison")
    ax.legend()
    ax.set_ylabel("Population")
    ax.set_xlabel("Year")
    plt.show()


if __name__ == "__main__":
    main()
