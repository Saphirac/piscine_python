import pandas as pd

pd.set_option('display.show_dimensions', False)

life_expectancy = pd.read_csv("day2/life_expectancy_years.csv")

print("Loading dataset of dimensions", life_expectancy.shape, life_expectancy)
