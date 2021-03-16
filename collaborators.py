from github import Github
from pydriller import RepositoryMining
import requests
import json 
import csv
# First create a Github instance:

# using an access token
g = Github("\\access token")
# Opening JSON file 
f = open('sstubs.json') 
  
# returns JSON object as  
# a dictionary 
data = json.load(f)
x = []
y = [] 
z = []
for i in range(200, 600):
    sha = data[i]['fixCommitSHA1']
    shaparent = data[i]['fixCommitParentSHA1']
    projex = data[i]['projectName']
    projex = projex.replace(".", "/")
    repo = g.get_repo(projex)
    commit = repo.get_commit(sha= sha)
    commit1 = repo.get_commit(sha= shaparent)
    datediff = commit.commit.committer.date - commit1.commit.committer.date
    try:
        temp = commit.committer.followers
        if not (temp == None):
            x.append(temp)
        else:
            x.append(0)
    except:
        x.append(0)
    try:
        temp1 = commit.committer.collaborators
        if not (temp1 == None):
            y.append(temp1)
        else:
            y.append(0)
    except:
        y.append(0)
    z.append(datediff.seconds//60)
    print(i)

t = zip(x, y, z)
with open('collaborators.csv', 'a') as f:
    writer = csv.writer(f, delimiter='\t')
    #writer.writerows(zip(["Followers"], ["Collaborators"], ["TimeDiffInMins"]))
    writer.writerows(t)

# 0-200
# 1000 - 1400
# 200 - 600
