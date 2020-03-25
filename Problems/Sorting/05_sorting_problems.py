'''
Sorting and Intro to Big Data Problems (22pts)

Import the data from NBAStats.py.  The data is all in a single list called 'data'.
I pulled this data from the csv in the same folder and converted it into a list for you already.
For all answers, show your work
Use combinations of sorting, list comprehensions, filtering or other techniques to get the answers.
'''


from NBAStats import *
print(data[0])
from NBAStats import data
header = data.pop(0)
print(header)


#1  Pop off the first item in the list and print it.  It contains the column headers. (1pt)
print(data.pop(0))

#2  Print the names of the top ten highest scoring single seasons in NBA history?
# You should use the PTS (points) column to sort the data. (4pts)
data.sort(key=lambda x: x[-1], reverse = True)
for i in range(10):
    print(data[i][2])


#3  How many career points did Kobe Bryant have? Add up all of his seasons. (4pts)
kobe_bryant = 0
for i in range(len(data)):
    if data[i][2] == "Kobe Bryant":
        kobe_bryant += int(data[i][-1])
print("Kobe Bryant had", kobe_bryant,"career points.")

print(int(sum([x[-1] for x in data if x[2] == "Kobe Bryant"])))


#4  What player has the most 3point field goals in a single season. (3pts)
data.sort(key=lambda x: x[34], reverse=True)
print(data[0][2], "had the most three point field goals in one season.")

#5  One stat featured in this data set is Win Shares(WS).
#  WS attempts to divvy up credit for team success to the individuals on the team.
#  WS/48 is also in this data.  It measures win shares per 48 minutes (WS per game).
#  Who has the highest WS/48 season of all time? (4pts)
ws = header.index("WS")
print(ws)
data.sort(key=lambda x: x[ws])
print(data[-1][2])

data.sort(key=lambda x: x[25], reverse = True)
for i in range(1):
    print(data[i][2], "had the highest ws/48 season of all time.")

#6  Write your own question that you have about the data and provide an answer (4pts)
# Maybe something like: "Who is the oldest player of all time?"  or "Who played the most games?"  or "Who has the most combined blocks and steals?".

#  Who has the most assists in a single season of all time?
data.sort(key=lambda x: x[-6], reverse = True)
for i in range(1):
    print(data[i][2], "has the most assists in a single season of all time.")


#7  Big challenge, few points.  Of the 100 highest scoring single seasons in NBA history, which player has the
# worst free throw percentage?  Which had the best? (2pts)
data.sort(key=lambda x: x[-1], reverse = True)
for i in range(100):
    data[i][2]
data.sort(key=lambda x: x[33])
for i in range(1):
    print(data[i][2], "has the worst free throw percentage of the 100 highest scoring single NBA seasons.")
data.sort(key=lambda x: x[33], reverse=True)
for i in range(1):
    print(data[i][2], "has the best free throw percentage of the 100 highest scoring single NBA seasons.")



