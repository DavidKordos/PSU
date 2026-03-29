import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

mtcars = pd.read_csv('mtcars.csv')

# imaju li automobili s ručnim mjenjačem veću potrošnju od automobila s automatskim mjenjačem
sns.boxplot(x='am', y='mpg', data=mtcars)

plt.title('Potrosnja ovisno o mjenjacu')
plt.xlabel('0=automatski, 1=rucni')
plt.ylabel('potrosnja (mpg)')

plt.show()
