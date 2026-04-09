import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv('mtcars.csv')

# Mapiranje mjenjača za legendu
df['mjenjac'] = df['am'].map({0: 'Automatski', 1: 'Ručni'})

# 4. Odnos ubrzanja (qsec) i snage (hp) prema tipu mjenjača
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='hp', y='qsec', hue='mjenjac', style='mjenjac', s=100)

plt.title('Odnos snage (hp) i ubrzanja (qsec) prema tipu mjenjača')
plt.xlabel('Snaga (hp)')
plt.ylabel('Ubrzanje (qsec)')
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(title='Tip mjenjača')

plt.show()
