import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


mtcars = pd.read_csv('mtcars.csv')

# Boxplot težine po broju cilindara
sns.boxplot(x='cyl', y='wt', data=mtcars, palette='Set3')

# Naslovi i oznake
plt.title('Distribucija težine automobila po broju cilindara')
plt.xlabel('Broj cilindara')
plt.ylabel('Težina (1000 lbs)')

# Prikaz grafa
plt.show()
