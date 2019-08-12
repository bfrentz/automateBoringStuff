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


# List keywords and load content


# close shelf
mcbShelf.close()