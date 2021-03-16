from github import Github
from pydriller import RepositoryMining
import requests
import json 
import csv
# First create a Github instance:

# using an access token
g = Github("/access token")

# Opening JSON file 
f = open('sstubs.json') 
  
# returns JSON object as  
# a dictionary 
data = json.load(f)
x = []
y = [] 
for i in range(0, 1000):
    sha = data[i]['fixCommitSHA1']
    xtemp = data[i]['bugLineNum']
    projex = data[i]['projectName']
    projex = projex.replace(".", "/")
    repo = g.get_repo(projex)
    commit = repo.get_commit(sha= sha)
    url = commit.files[0].raw_url
    r = requests.get(url)
    CoList = r.text.split("\n") 
    Counter = 0
    for i in CoList:  
        Counter += 1
    x.append(xtemp)
    y.append(Counter)

t = zip(x, y)
with open('1-500.csv', 'w') as f:
    writer = csv.writer(f, delimiter='\t')
    writer.writerows(zip(["bugLineNum"], ["totalNumLinesInFile"]))
    writer.writerows(t)