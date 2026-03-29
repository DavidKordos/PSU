import pandas as pd
import numpy as np


mtcars = pd.read_csv('mtcars.csv')
rezultat = mtcars[(mtcars['cyl'] == 4) & (mtcars['wt'] > 2.0) & (mtcars['wt'] < 2.2)]
print(rezultat)
print(rezultat['mpg'].mean())
