#! /usr/bin/python3
# luckySearch.py - Opens a browswer, performs a google search for the command line arguments and then opens the top five results in new tabs
#
# Bryce Frentz
# 9/25/19

import requests, sys, webbrowser, bs4

print('Googling...') 	# display text while downloading the google page
url = 'https://google.com/search?q=' + ' '.join(sys.argv[1:])
print(f'url: {url}')
browser = requests.get(url)
browser.raise_for_status()

# DEBUG
print(browser.content)

# Retrieve top search result links
soup = bs4.BeautifulSoup(browser.text, features="lxml")
#print(soup.getText())


# Open a browswer tab for each result
linkElems = soup.select('div.r a')

# DEBUG
print(len(linkElems))
for item in range(len(linkElems)):
	print(str(item) + "\t" + linkElems[item].getText())

numOpen = min(5, len(linkElems))
for i in range(numOpen):
	print(i)
	print(linkElems[i].get('href'))
	webbrowser.open('http://google.com' + linkElems[i].get('href'))