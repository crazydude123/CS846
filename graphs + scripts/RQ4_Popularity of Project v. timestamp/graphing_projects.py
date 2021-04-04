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
import statistics

col_list = ["Forks", "TimeDiffInMins"]

df = pd.read_csv("output.csv", usecols=col_list, sep='\t')
#print(df)
x = df["TimeDiffInMins"]
y = df["Forks"]

xx = list(x)
yy = list(y)

for j in xx[:]:
   if j>=1000 or j<0:
      del yy[xx.index(j)]
      xx.remove(j)

for j in yy[:]:
   if j>=1600 or j<0:
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

#Logic to calculate Forks avg. Time
j = {}
bb = {}
length = len(df["Color"])
for i in set(df["Color"]):
   gg = []
   vou = 0.0
   cut = 0
   summ = 0
   for k in range(0, length):
      if (df["Color"][k]==i):
         gg.append(df["TimeDiffInMins"][k])
   j[i]= statistics.mean(gg)
   try:
      bb[i]= round(statistics.stdev(gg), 2)
   except:
      bb[i] = 0
print(j)


groups = df.groupby("Color")
print(groups)

plt.title("Bug fix times vs. Projects; Label: Count : Mean : StdDev")
for name, group in groups:
   hh = [countt[name],j[name], bb[name]]
   plt.plot(group.TimeDiffInMins , group.Forks , marker = 'o', linestyle='', markersize=6, label = hh)

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