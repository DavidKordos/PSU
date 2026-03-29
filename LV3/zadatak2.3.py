import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


mtcars = pd.read_csv('mtcars.csv')

sns.barplot(x='am', y='mpg', data=mtcars, ci=None, palette='Set2') #ci uklanja prikaz intervala pouzdanovsti

# Naslovi i oznake
plt.title('Prosječna potrošnja automobila po broju cilindara')
plt.xlabel('Vrsta mjenjaca')
plt.ylabel('Potrošnja (mpg)')

plt.show()
