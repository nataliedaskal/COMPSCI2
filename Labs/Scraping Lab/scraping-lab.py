# SCRAPING PROBLEMS
# Twitter Scraping (15pts)
# Go to your favorite follow on Twitter.  (not someone who posts explicit materials please)
# Inspect the twitter feed in Chrome.
# You'll notice that the tweets are stored in a ordered list <ol></ol>, and individual tweets are contained as list items <li></li>.
# Use BeautifulSoup and requests to grab the text contents of last 5 tweets located on the twitter page you chose.
# Print the tweets in a nicely formatted way.
# Have fun.  Again, nothing explicit.

print("@GCTigerTracker's five most recent tweets")
print("")

from bs4 import BeautifulSoup
import requests

url = "https://twitter.com/gctigertracker"  # uniform resource locator

page = requests.get(url)

soup = BeautifulSoup(page.text, "html.parser")

tweet = soup.findAll(class_="tweet-text")
tweets = []
for i in tweet:
    tweets.append(i.text)

for i in range(5):
    print("Tweet number", i + 1, ":")
    print(tweets[i])


#  print("{} {}!".format("Hello", "World"))

# Weather Scraping (15pts)
# Below is a link to a 10-day weather forecast at weather.com
# Pick the weather for a city that has the first letter as your name.
# Use requests and BeautifulSoup to scrape data from the weather table.
# Print a synopsis of the weather for the next 10 days.
# Include the day and date, description, high and low temp, chance of rain, and wind. (2pts each)
# Print the weather for each of the next 10 days to the user in a readable sentences.
# You can customize the text as you like, but it should be readable as a sentence without errors. (5pts)
# You will need to target specific classes or other attributes to pull some parts of the data.
# Sample sentence:
# Wednesday, April 4 will be Partly Cloudy/Windy with a High of 37 degrees and a low of 25, humidity at 52%.  There is 0% chance of rain with winds out of the WNW at 22 mph.
# if the sentence is a little different than shown, that will work; do what you can.  Don't forget about our friend string.format()

print("")
print("Nantucket, MA 10-Day Weather Report")
print("")

from bs4 import BeautifulSoup
import requests

url = "https://weather.com/weather/tenday/l/8cf50ada9067513e696ed4c448e8d583a20f080987d1b27f3979b6d0c22caf1d"

page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")

days = []
day = soup.findAll(class_="date-time")
for day in day:
    days.append(day.text)

dates = []
date = soup.findAll(class_="day-detail clearfix")
for date in date:
    dates.append(date.text)

descriptions = []
titles = []
description = soup.findAll(class_="description")
for description in description[1:]:
    descriptions.append(description)
for i in range(len(descriptions)):
    title = descriptions[i].get("title")
    titles.append(title)

temperatures = []
temperature = soup.findAll(class_="temp")
for temperature in temperature[1:]:
    temperatures.append(temperature.text)

precipitation = []
precip = soup.findAll(class_="precip")
for precip in precip[1:]:
    precipitation.append(precip.text)

winds = []
wind = soup.findAll(class_="wind")
for wind in wind[1:]:
    winds.append(wind.text)

humidities = []
humidity = soup.findAll(class_="humidity")
for humidity in humidity[1:]:
    humidities.append(humidity.text)

for i in range(10):
    print(days[i] + ",", dates[i] + ":", titles[i], "High temperature of", temperatures[i][0:3] + "F.", "Low temperature of", temperatures[i][3:] + "F.", precipitation[i], "chance of rain. Winds to the",  winds[i][0:3], "at" + winds[i][3:-1] + ". " + humidities[i], "humidity.")
