import pandas as pd
import numpy as np

# Srednja potrošnja automobila s 4 cilindra mase između 2000 i 2200 lbs
mtcars = pd.read_csv('mtcars.csv')
rezultat = mtcars[(mtcars['cyl'] == 4) & (mtcars['wt'] > 2.0) & (mtcars['wt'] < 2.2)]
print(rezultat)
print(rezultat['mpg'].mean())
