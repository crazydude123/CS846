import numpy as np
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
from numpy import *
from operator import truediv 
import pandas as pd
import seaborn as sns
from sklearn.datasets import load_digits
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from collections import Counter

col_list = ["Forks", "TimeDiffInMins", "Followers"]

df = pd.read_csv("output.csv", usecols=col_list, sep='\t')
#print(df)
x = df["TimeDiffInMins"]
y = df["Forks"]
z = df["Followers"]

xx = list(x)
yy = list(y)
zz = list(z)

for j in xx[:]:
   if j>=200 or j<0:
      del yy[xx.index(j)]
      del zz[xx.index(j)]
      xx.remove(j)

for j in yy[:]:
   if j>=1200 or j<0:
      del xx[yy.index(j)]
      del zz[yy.index(j)]
      yy.remove(j)

for j in zz[:]:
   if j>=3000 or j<0:
      del xx[zz.index(j)]
      del yy[zz.index(j)]
      zz.remove(j)


df = list(zip(xx, yy, zz))
df = pd.DataFrame(df, columns = ["TimeDiffInMins", "Forks", "Followers"])

fig = plt.figure(figsize = (10, 7))
ax = plt.axes(projection ="3d")

plt.xlabel("Time in minutes")
plt.ylabel("Number of forks")
ax.set_zlabel("Number of Followers")

ax.scatter3D(xx, yy, zz, color = "green")
#plt.show()

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