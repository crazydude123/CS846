import numpy as np
import matplotlib.pyplot as plt
from numpy import *
from operator import truediv 
import pandas as pd
import seaborn as sns
from sklearn.datasets import load_digits
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from collections import Counter

col_list = ["Forks", "TimeDiffInMins"]

df = pd.read_csv("output.csv", usecols=col_list, sep='\t')
#print(df)
x = df["TimeDiffInMins"]
y = df["Forks"]

xx = list(x)
yy = list(y)

for j in xx[:]:
   if j>=5000 or j<0:
      del yy[xx.index(j)]
      xx.remove(j)

for j in yy[:]:
   if j>=4000 or j<0:
      del xx[yy.index(j)]
      yy.remove(j)




df = list(zip(xx, yy))
df = pd.DataFrame(df, columns = ["TimeDiffInMins", "Forks"])

categories = np.unique(df["Forks"])

colors = np.linspace(0, 1, len(categories))
colors = np.around(colors, 2)
colordict = dict(zip(categories, colors))
labeldict = dict(zip(colors, categories))
df["Color"] = df["Forks"].apply(lambda x: colordict[x])
countt = Counter(df["Color"])

groups = df.groupby("Color")
print(groups)

plt.title("Bug fix times vs. Projects")
for name, group in groups:
   plt.plot(group.TimeDiffInMins , group.Forks , marker = 'o', linestyle='', markersize=6, label = countt[name])

plt.xlabel("Time in minutes")
plt.ylabel("Number of forks")
#plt.scatter(df["TimeDiffInMins"], df["Forks"], c=df.Color, label=0)

plt.legend()
plt.show()

t = set(yy)
c = len(t)

for i in set(yy):
   plt.axhline(y=i)
plt.title(c)
plt.plot(xx, yy, 'o', color='black')
#plt.ylim([0, 500])
#plt.xlim([0, 2000])
plt.show()