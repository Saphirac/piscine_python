import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.show_dimensions', False)

life_expectancy = pd.read_csv("day2/life_expectancy_years.csv", index_col=0)

#print("Loading dataset of dimensions", life_expectancy.shape, '\n', life_expectancy)

graph = life_expectancy.loc["France"]

plt.plot(graph)
plt.xticks(ticks=graph.index[::40])
plt.title('France Life expectancy Projections')
plt.ylabel('Life expectancy')
plt.xlabel('Year')
plt.show()
