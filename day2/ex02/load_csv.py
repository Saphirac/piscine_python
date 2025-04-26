import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

pd.set_option('display.show_dimensions', False)

population = pd.read_csv("day2/population_total.csv", index_col=0)

#print("Loading dataset of dimensions", life_expectancy.shape, '\n', life_expectancy)

def parse_pop(x) :
    if (x[-1] == 'k') :
        return float(x[:-1]) * 10**3
    if (x[-1] == 'M') :
        return float(x[:-1]) * 10**6
    if (x[-1] == 'B') :
        return float(x[:-1]) * 10**9
    else :
        return float(x)

france = population.loc["France"]
senegal = population.loc["Senegal"]

france = france.map(parse_pop)
senegal = senegal.map(parse_pop)

plt.plot(france, label='France')
plt.plot(senegal, label='Senegal')

plt.xticks(ticks=senegal.index[::40])

plt.title('France vs Senegal population comparison')
plt.legend()
plt.ylabel('Population')
plt.xlabel('Year')
plt.show()
