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
elems = weather.select('div > span')

# DEBUG
print(len(elems))