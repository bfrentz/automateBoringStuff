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
"""

import sys
import shelve
import pyperclip


