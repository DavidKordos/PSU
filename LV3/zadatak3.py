import urllib.request as ur
import pandas as pd
import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt

# URL koji sadrži XML datoteku s mjerenjima za Osijek (postaja=160) i PM10 (polutant=5)
url = '[iszz.azo.hr](http://iszz.azo.hr/iskzl/rs/podatak/export/xml?postaja=160&polutant=5&tipPodatka=0&vrijemeOd=01.01.2017&vrijemeDo=31.12.2017)'


airQualityHR = ur.urlopen(url).read()
root = ET.fromstring(airQualityHR)


df = pd.DataFrame(columns=('mjerenje', 'vrijeme'))


for i, obj in enumerate(root):
    try:
        mjerenje = float(obj[0].text)
        vrijeme = obj[2].text
        df.loc[i] = [mjerenje, vrijeme]
    except Exception:
        continue


df['vrijeme'] = pd.to_datetime(df['vrijeme'], utc=True)

df = df.sort_values('vrijeme')


df['month'] = df['vrijeme'].dt.month
df['dayOfweek'] = df['vrijeme'].dt.dayofweek


df.plot(y='mjerenje', x='vrijeme', title='Dnevne koncentracije PM10 - Osijek 2017', ylabel='PM10 (µg/m³)')
plt.tight_layout()
plt.show()

# Ispis tri datuma s najvećim koncentracijama PM10
top3 = df.sort_values('mjerenje', ascending=False).head(3)
print("Tri datuma s najvećom koncentracijom PM10 u Osijeku 2017. godine:")
for index, row in top3.iterrows():
    print(f"- {row['vrijeme'].date()} : {row['mjerenje']} µg/m³")
