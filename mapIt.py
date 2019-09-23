#! /usr/bin/python3
# mapIt.py - Opens a google maps link to any address entered or address copied to the clipboard
#
# Bryce Frentz
# 9/19/19

import webbrowser, sys, pyperclip

if len(sys.argv) > 1:
	# Get address from command line.
	address = ' '.join(sys.argv[1:])

else:
	# Get the address from the clipboard
	address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)