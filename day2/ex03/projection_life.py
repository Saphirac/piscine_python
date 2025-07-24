import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import seaborn as sns
from load_csv import load


def parse_inc(x):
    """Change k to 1000"""
    if isinstance(x, str):
        if x[-1] == "k":
            return float(x[:-1]) * 10**3
    return float(x)

#TODO : fix this thing

def main():
    income = load("day2/income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    income_1900 = income[["country", "1900"]].rename(columns={"1900": "income_1900"})
    income_1900["income_1900"] = income_1900["income_1900"].map(parse_inc)

    life = load("day2/life_expectancy_years.csv")
    life_1900 = life[["country", "1900"]].rename(columns={"1900": "life_1900"})

    # Merge my data

    lifebyincome = pd.merge(income_1900, life_1900, on="country")

    # Scatterplot :

    plt.figure(figsize=(10, 6))

    ax = sns.scatterplot(data=lifebyincome, x="income_1900", y="life_1900")
    ax.set_xscale("log")

    ax.set_xticks([300, 1000, 10000])
    ax.xaxis.set_major_formatter(
        mticker.FuncFormatter(lambda x, y: f"{int(x / 1000)}k" if x >= 1000 else str(x))
    )

    ax.set_xlabel("Gross domestic product")
    ax.set_ylabel("Life Expectancy")
    ax.set_title("1900")

    plt.show()


if __name__ == "__main__":
    main()
