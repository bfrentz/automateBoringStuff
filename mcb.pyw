#! /usr/bin/python3
# mcb.py (MultiClipBoardi) - Saves and loads pieces of text to the clipboard
# .pyw extension supresses the terminal
#
# Bryce Frentz
# 8/12/19
#
"""
Program plan:
The program will save each piece of clipboard text under a keyword. 
* The command line argument for the keyword is checked
* If the argument is save, then the clipboard contents are saved to the keyword
* If the argument is list, then all the keywords are copied to the clipboard
* Otherwise, the text for the keyword will be copied to the clipboard

Usage:
py mcb.pyw save <keyword> - Saves the clipboard to keyword.
py mcb.pyw <keyword> - Loads keyword to the clipboard
py mcb.pyw list - loads all keywords to the clipboard
"""

import sys
import shelve
import pyperclip

# Open shelf
mcbShelf = shelve.open('mcb')


# Save the clipboard content
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
	mcbShelf[sys.argv[2]] = pyperclip.paste()

# List the keywords and load a specific keyword's content
elif len(sys.argv) == 2:
	if sys.argv[1].lower() == 'list':
		pyperclip.copy(str(list(mcbShelf.keys())))
	elif sys.argv[1] in mcbShelf:
		pyperclip.copy(mcbShelf[sys.argv[1]])

# close shelf
mcbShelf.close()