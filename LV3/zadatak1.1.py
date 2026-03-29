
import pandas as pd

mtcars = pd.read_csv('mtcars.csv')
#5 automobila s najvećom potrošnjom
top5 = mtcars.sort_values(by='mpg').head(5)
print(top5[['car', 'mpg']])
