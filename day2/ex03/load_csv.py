import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import seaborn as sns

pd.set_option('display.show_dimensions', False)

income = pd.read_csv("day2/income_per_person_gdppercapita_ppp_inflation_adjusted.csv", index_col=0)
life = pd.read_csv("day2/life_expectancy_years.csv", index_col=0)

# we're doing life expectancy by income for each country

plt.show()
