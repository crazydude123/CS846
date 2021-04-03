from github import Github
from pydriller import RepositoryMining
import requests
import json 
import csv
# First create a Github instance:

# using an access token
g = Github("038ea8869e81cae047d36be79a208d8f1d52b098")

# Opening JSON file 
f = open('sstubs.json') 
zz =0
# returns JSON object as  
# a dictionary
c = 0 
data = json.load(f)
for i in data:
    c +=1

x = []
y = [] 
for i in range(0, c):
    sha = data[i]['fixCommitSHA1']
    xtemp = data[i]['bugLineNum']
    repo = g.get_repo('signalapp/Signal-Android')
    commit = repo.get_commit(sha= sha)
    url = commit.files[0].raw_url
    r = requests.get(url)
    CoList = r.text.split("\n") 
    Counter = 0
    for i in CoList:  
        Counter += 1
    x.append(xtemp)
    y.append(Counter)
    print(zz)
    zz+=1

t = zip(x, y)
with open('1-500.csv', 'w') as f:
    writer = csv.writer(f, delimiter='\t')
    writer.writerows(zip(["bugLineNum"], ["totalNumLinesInFile"]))
    writer.writerows(t)