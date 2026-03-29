import pandas as pd
import numpy as np


mtcars = pd.read_csv('mtcars.csv')
# automobili s automatskim mjenjačem i snagom preko 100 konjskih snaga
rezultat = mtcars[(mtcars['am'] == 0) & (mtcars['cyl'] == 6) & (mtcars['hp'] > 100)].shape[0] #shape broji koliko ih ima koji zadovoljavaju uvijet
print(rezultat)
