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
income_1900 = income[['country', '1900']].rename(columns={'1900': 'income_1900'})
income_1900['income_1900'] = income_1900['income_1900'].map(parse_inc)

life = pd.read_csv("day2/life_expectancy_years.csv")
life_1900 = life[['country', '1900']].rename(columns={'1900': 'life_1900'})

lifebyincome = pd.merge(income_1900, life_1900, on='country')
# here we have to index both by "country"

lifebyincome.to_csv("day2/test.csv")

# we're doing life expectancy by income for each country ONLY for the year 1900 !!

# what we have to do : merge the data, and keep income and life expectancy as suffixes, then we have to merge the data for the year 1900 only, and then we scatter life by income

plt.figure(figsize=(10,6))

ax = sns.scatterplot(data=lifebyincome, x='income_1900', y='life_1900')
ax.set_xscale('log')

ax.set_xticks([300, 1000, 10000])
ax.xaxis.set_major_formatter(mticker.FuncFormatter(lambda x,y: f'{int(x/1000)}k' if x>=1000 else str(x)))

ax.set_xlabel("Gross domestic product")
ax.set_ylabel("Life Expectancy")
ax.set_title("1900")

plt.show()

#lifebyincome = pd.merge(income, life, how="left", left_index=True, right_index=True)


# plt.show()
