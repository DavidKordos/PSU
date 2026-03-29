import pandas as pd
import numpy as np

#Prosječna potrošnja za 6 cilindara
mtcars = pd.read_csv('mtcars.csv')
rezultat = mtcars[mtcars['cyl'] == 6]
print(rezultat)
print(rezultat['mpg'].mean())
