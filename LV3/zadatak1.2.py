import pandas as pd
import numpy as np


mtcars = pd.read_csv('mtcars.csv')
rezultat = mtcars[mtcars['cyl'] == 8].sort_values(by='mpg').head(3)
print(rezultat['car'])
