import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#graphique montrant une tendance PIB --> générosité

df = pd.read_excel("données.xls",index_col='Country name')
df2 = df.sort_values(by = 'Logged GDP per capita', ascending = False)

#print(df)

#graphique montrant une tendance PIB --> moins de générosité

p = np.polyfit((0,0.4),(11,0),deg=1)
X = np.linspace(0,11,1000)
Y = p[1]*X + p[0]
plt.figure()
df.plot.scatter(x='Logged GDP per capita', y='Generosity')
plt.show()

#La tendance générale est PIB élevé --> haut taux de bonheur

plt.figure()
df.plot.scatter(x='Logged GDP per capita', y='Ladder score')
plt.show()


# On voit que comme pour la plupart des indicateurs, on peut relier le PIB à de nombreux indicateurs de bien-être, avec cependant de nombreuses exception
# On en déduit que le PIB est un bon indicateur du niveau de bien-être mais qu'il n'est pas idéal
# IL pourrait être intéressant de consiérer de nouveau indicateur pour mieux mesurer le bien-être d'une population 


plt.figure()
plt.scatter(df2['Logged GDP per capita'], df2['Healthy life expectancy']/100)
plt.scatter(df2['Logged GDP per capita'], df2['Social support'])
plt.scatter(df2['Logged GDP per capita'], df2['Freedom to make life choices'])
plt.show()


plt.figure()
plt.scatter(df2['Logged GDP per capita'], df2['Perceptions of corruption'])
plt.show()