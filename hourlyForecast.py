#! /usr/bin/python3
# hourlyForecast.py - Pulls the hourly forecast data from wunderground.com
#
# Bryce Frentz
# 9/24/19

import requests, bs4

# Get the remainder of the day's hourly forecast
res = requests.get('https://www.wunderground.com/hourly/us/in/notre-dame/46556')
res.raise_for_status()
weather = bs4.BeautifulSoup(res.text, features="lxml")

# Get div span
elems = weather.select('tr div > span')

# DEBUG
#print(len(elems))
#for item in range(len(elems)):
#	print(str(item) + "\t" + elems[item].getText())

time = []
attribute = []
temp = []
precip = []
wind = []

# Get the items from the website's text
for item in range(len(elems)):
	if item % 10 == 0:
		#print(str(item) + "\t" + elems[item].getText())
		time.append(elems[item].getText())
	elif item % 10 == 1:
		#print(str(item) + "\t" + elems[item].getText())
		attribute.append(elems[item].getText())
	elif item % 10 == 2:
		#print(str(item) + "\t" + elems[item].getText())
		temp.append(elems[item].getText())
	elif item % 10 == 4:
		#print(str(item) + "\t" + elems[item].getText())
		precip.append(elems[item].getText())
	elif item % 10 == 9:
		#print(str(item) + "\t" + elems[item].getText())
		wind.append(elems[item].getText())

# Print out the data in nice tabular format
print('Time\tConditions\tTemperature\tPrecipitation\tWind')
for item in range(len(time)):
	print(time[item] + "\t" + attribute[item] + "\t" + temp[item] + "\t" + precip[item] + "\t" + wind[item])