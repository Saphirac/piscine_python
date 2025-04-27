import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import seaborn as sns


def parse_inc(x):
    if isinstance(x, str):
        if x[-1] == "k":
            return float(x[:-1]) * 10**3
    return float(x)


pd.set_option("display.show_dimensions", False)

income = pd.read_csv("day2/income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
income = income.map(parse_inc)

life = pd.read_csv("day2/life_expectancy_years.csv")
# here we have to index both by "country"


# we're doing life expectancy by income for each country ONLY for the year 1900 !!

# what we have to do : merge the data, and keep income and life expectancy as suffixes, then we have to merge the data for the year 1900 only, and then we scatter life by income


lifebyincome = pd.merge(income, life, how="left", left_index=True, right_index=True)
lifebyincome.to_csv("day2/test.csv")

print("Income shape :", income.shape)
print("Life shape :", life.shape)
print("Life by income shape :", lifebyincome.shape)


# sns.relplot(lifebyincome, x="income", y="life_expectancy")
# plt.show()
