import numpy as np
import matplotlib.pyplot as plt
from numpy import *
from operator import truediv 
import pandas as pd
import seaborn as sns

col_list = ["bugLineNum", "totalNumLinesInFile"]

df = pd.read_csv("1-500.csv", usecols=col_list, sep='\t')

x = df["bugLineNum"]
y = df["totalNumLinesInFile"]


k = list(map(truediv, x, y))
#for j in k[:]:
 #   if (j>=1):
  #      k.remove(j)
   #     print(j)
#plt.hist(k, bins = 200)
k = pd.Series(k)
'''
k.plot.kde(ind= 1200, bw_method= 'silverman')
plt.title("KDE")
plt.xlabel("bugLineNum/totalLines")
plt.xlim([0, 1])
plt.ylabel("Frequency")
plt.show()
'''

'''
k = pd.Series(k)
fig, ax = plt.subplots(figsize = (6,4))
k.plot(kind = "hist", density = True, bins = 600)
k.plot(kind = "kde")
ax.set_xlabel("bugLineNum/totalLines")
ax.set_ylim(0, 1)
ax.set_xlim(0, 1)
ax.set_title("Density Function")
plt.show()
'''
f,ax = plt.subplots()
#sns.distplot(k, hist=True, kde=True, 
 #            bins=int(1200), color = 'darkblue', 
  #           hist_kws={'edgecolor':'black'},
   #          kde_kws={'linewidth': 4})

second_ax = ax.twinx()

#Plotting kde without hist on the second Y axis
plt.xlim([0, 1])
sns.distplot(k, kde=True, hist=False, kde_kws={'linewidth': 4}, color= 'darkblue', norm_hist=True, bins = 100)

#Removing Y ticks from the second axis
second_ax.set_yticks([])

plt.title("KDE: Probability Density Estimate")
plt.xlabel("FJksj")
plt.ylabel("")

plt.show()