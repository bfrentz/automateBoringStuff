#! /usr/bin/python3
# luckySearch.py - Opens a browswer, performs a google search for the command line arguments and then opens the top five results in new tabs
#
# Bryce Frentz
# 9/25/19

import requests, sys, webbrowser, bs4

print('Googling...') 	# display text while downloading the google page
res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

# Retrieve top search result links


# Open a browswer tab for each result