#! /usr/bin/python3
# weatherCheck.py - Opens a wunderground site for Notre Dame weather
#
# Bryce Frentz
# 9/19/19

import webbrowser, sys, pyperclip

webbrowser.open('https://www.wunderground.com/weather/us/in/notre-dame')

# I'd also like to update this to take a command line argument for different places about which I care (ND, Louisville, Sioux Falls, Bozeman, MSP)
# I want to update using beautifulsoup4 to get hourly weather for the day or the 10 day forecast