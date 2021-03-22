from github import Github
from pydriller import RepositoryMining
import requests
import json 
import csv
import pandas as pd
# First create a Github instance:
df = pd.read_csv('topJavaMavenProjects.csv')
k = df.set_index('repository_url').T.to_dict('list')

# using an access token
g = Github("\\access token")
# Opening JSON file 
f = open('sstubs.json') 
  
# returns JSON object as  
# a dictionary 
data = json.load(f)
x = []
z = [] 
forks = []
watch = []
pro = []
for i in range(2500, 3000):
    sha = data[i]['fixCommitSHA1']
    shaparent = data[i]['fixCommitParentSHA1']
    projex = data[i]['projectName']
    projex = projex.replace(".", "/")
    repo = g.get_repo(projex)
    commit = repo.get_commit(sha= sha)
    commit1 = repo.get_commit(sha= shaparent)
    q = "https://github.com" + "/" + projex
    datediff = commit.commit.committer.date - commit1.commit.committer.date
    try:
        temp = commit.committer.followers
        if not (temp == None):
            x.append(temp)
        else:
            x.append(0)
    except:
        x.append(0)
    z.append((datediff.days * 60 * 24) + datediff.seconds//60)
    print(i)
    forks.append(k[q][0])
    watch.append(k[q][1])
    pro.append(q)


t = zip(x, z, forks, watch, pro)
with open('output.csv', 'a') as f:
    writer = csv.writer(f, delimiter='\t')
    #writer.writerows(zip(["Followers"], ["TimeDiffInMins"], ["Forks"], ["Watchers"], "ProjectURL"))
    writer.writerows(t)

# 0- 1500
# 4500 - 5000
# 3000 -3500
# 2500 - 3000
