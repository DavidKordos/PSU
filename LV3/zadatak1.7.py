import pandas as pd
import numpy as np


mtcars = pd.read_csv('mtcars.csv')

# Masa svakog automobila u kg
mtcars['masa_kg'] = mtcars['wt'] * 1000 * 0.453592

print(mtcars[['car', 'masa_kg']])
