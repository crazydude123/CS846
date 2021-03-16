
import numpy as np
import matplotlib.pyplot as plt
from numpy import *
from operator import truediv 
import pandas as pd
col_list = ["bugLineNum", "totalNumLinesInFile"]

df = pd.read_csv("1-500.csv", usecols=col_list, sep='\t')

x = df["bugLineNum"]
y = df["totalNumLinesInFile"]
print(x)


k = list(map(truediv, x, y))

plt.hist(k, bins = 1200)
plt.title("Gaussian Histogram")
plt.xlabel("bugLineNum/totalLines")
plt.xlim([0, 1])
plt.ylabel("Frequency")
plt.show()