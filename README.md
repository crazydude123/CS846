# CS846

1. linNumDataExtraction.py: Has code to extra data from the sstubs.json file on the MSR site
2. 1-500.csv: has 1200 rows of data extracted
3. nuggetplot.py reads data from 1-500.csv and plots the normalized frequency distribution
4. collaborators.py
5. graph + scripts/followers/followers_various.py does cluster analysis for collaborators.csv


USAGE:

1. python3 linNumDataExtraction.py should fetch the data
2. python3 nuggetplot.py to plot a nice histogram
3. graph + scripts/ nugget/ has all the graphs and data: beautiful x'D
4. "python3 collaborators.py" fetches the collaborator/follower/timestamp diff in minutes in that order
5. collaborators.csv is the o/p of step 4
6. "python3 followers_various.py" give cluster analyses of followers v. time taken to fix bug
7. NOTE THAT collaborators.csv actually has the followers. (collaborators aren't a thing dweeb, grow up)
