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

col_list = ["Followers", "TimeDiffInMins"]

df = pd.read_csv("collaborators.csv", usecols=col_list, sep='\t')

x = df["TimeDiffInMins"]
y = df["Followers"]

xx = list(x)
yy = list(y)

for j in xx[:]:
   if j>=2000 or j<0:
      del yy[xx.index(j)]
      xx.remove(j)

for j in yy[:]:
   if j>=500 or j<0:
      del xx[yy.index(j)]
      yy.remove(j)

df = list(zip(xx, yy))
for i in df:
   if i[0]<0 or i[1]<0:
      print(i)


pca = PCA(2)
df = pca.fit_transform(df)

from sklearn.metrics import silhouette_score

sil = []
kmax = 10

# dissimilarity would not be defined for a single cluster, thus, minimum number of clusters should be 2
for k in range(2, kmax+1):
   kmeans = KMeans(n_clusters = k).fit(df)
   labels = kmeans.labels_
   sil.append(silhouette_score(df, labels, metric = 'euclidean'))
print(sil)
print(df.shape)

kmeans = KMeans(n_clusters= 3)
label = kmeans.fit_predict(df)
a = dict(Counter(label))
print(a)
#filter rows of original data
u_labels = np.unique(label)
centroids = kmeans.cluster_centers_
#plt.ylim([0, 500])
#plt.xlim([0, 2000])
#plotting the results:
plt.title(a)
 
for i in u_labels:
    plt.scatter(df[label == i , 0] , df[label == i , 1] , label = i)
plt.scatter(centroids[:,0] , centroids[:,1] , s = 80, color = "black")
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