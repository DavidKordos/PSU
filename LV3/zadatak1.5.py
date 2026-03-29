import pandas as pd
import numpy as np

mtcars = pd.read_csv('mtcars.csv')

#gear ili am
rucni = mtcars[mtcars['am'] == 1]
automatski = mtcars[mtcars['am'] == 0]

print("Rucni:", len(rucni))
print("Automatski:", len(automatski))
