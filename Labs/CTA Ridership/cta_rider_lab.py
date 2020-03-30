'''
CTA Ridership (25pts)

Get the csv from the following data set.
https://data.cityofchicago.org/api/views/w8km-9pzd/rows.csv?accessType=DOWNLOAD
This shows CTA ridership by year going back to the 80s
It has been updated with 2018 data, but not yet with 2019 unfortunately


1  Make a line plot of rail usage for the last 10 years of data.  (year on x axis, and ridership on y) (5pts)
2  Plot bus usage for the same years as a second line on your graph. (5pts)
3  Plot total usage on a third line on your graph. (5pts)
4  Add a title and label your axes. (4pts)
5  Add a legend to show data represented by each of the three lines. (4pts)
6  What trend or trends do you see in the data?  Offer a hypotheses which might explain the trend(s). Just add a comment here to explain. (2pts)
'''

import csv
<<<<<<< HEAD
import matplotlib.pyplot as plt


with open("CTA_-_Ridership_-_Annual_Boarding_Totals (2).csv") as f:
    reader = csv.reader(f)
    data = list(reader)

plt.figure(1)

headers = data.pop(0)
print(headers)
print(data)

years = [int(x[0]) for x in data[20:]]
rail_usage = [int(x[3]) for x in data[20:]]
print(rail_usage)
bus_usage = [int(x[1]) for x in data[20:]]
print(bus_usage)
total_ridership = [int(bus_usage[x]) + int(rail_usage[x]) for x in range(len(bus_usage))]
print(total_ridership)

graph = plt.figure(1, tight_layout=True)

plt.plot(years, rail_usage, label = "Rail")
plt.plot(years, bus_usage, label = "Bus")
plt.plot(years, total_ridership, label = "Total")

plt.xlabel('Year')
plt.ylabel('Number of riders (hundred millions)')
plt.title('CTA Ridership 2008-2017: Bus, Rail, Total')
plt.legend()
plt.axis([2008, 2017, 0, 600000000])

plt.show()

'''
# 6
Overall increase in rail, overall decrease in bus, and overall decrease in total usage. Increase in rail could 
be a result of an increasing climate aware population. People are more likely to take the train in an effort to reduce
their carbon footprint. A decrease in bus usage could have something to do with increased traffic from rideshare services
that make bus travel times worse. 

'''
=======

with open("CTA_-_Ridership_-_Annual_Boarding_Totals (1).csv") as f:
    cr = csv.reader(f)
    data = list(cr)

print(data)


# pop header
# get last 10 years (years)
# get last 10 years bus
# get last 10 years rail
# get last 10 years total

# plot bus
# plot rail
# plot total

# axis
# labels
# title
# legend (label plots)

# show plot
>>>>>>> 729df7b42a237934c57ac059eb2373f61b5423c2
