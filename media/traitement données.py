import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#graphique montrant une tendance PIB --> générosité

df = pd.read_excel("données.xls",index_col='Country name')

#print(df)

#graphique montrant une tendance PIB --> générosité

p = np.polyfit((0,0.4),(11,0),deg=1)
X = np.linspace(0,11,1000)
Y = p[1]*X + p[0]
#plt.figure()
#df.plot.scatter(x='Logged GDP per capita', y='Generosity')
#plt.show()

#la tendance générale est PIB élevé --> haut taux de bonheur

#plt.figure()
#df.plot.scatter(x='Logged GDP per capita', y='Ladder score')
#plt.show()


df2 = df.sort_values(by = 'Logged GDP per capita', ascending = False)
plt.figure()
plt.plot(df2['Logged GDP per capita'], df2['Healthy life expectancy']/100)
plt.plot(df2['Logged GDP per capita'], df2['Social support'])
plt.plot(df2['Logged GDP per capita'], df2['Freedom to make life choices'])
plt.show()
