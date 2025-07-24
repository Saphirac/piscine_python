import matplotlib.pyplot as plt
from load_csv import load

def parse_pop(x) :
    if (x[-1] == 'k') :
        return float(x[:-1]) * 10**3
    if (x[-1] == 'M') :
        return float(x[:-1]) * 10**6
    if (x[-1] == 'B') :
        return float(x[:-1]) * 10**9
    else :
        return float(x)

def main():
    population = load("day2/population_total.csv")

    france = population.loc["France"]
    senegal = population.loc["Senegal"]

    france = france.loc[:'2050'].map(parse_pop)
    senegal = senegal.loc[:'2050'].map(parse_pop)

    plt.plot(france, label='France')
    plt.plot(senegal, label='Senegal')

    plt.xticks(ticks=senegal.index[::40])

    plt.title('France vs Senegal population comparison')
    plt.legend()
    plt.ylabel('Population')
    plt.xlabel('Year')
    plt.show()


if __name__ == "__main__":
    main()
