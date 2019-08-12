#! /usr/bin/python3
# bulletPointAdder.py - 
#
# Takes text from the clipboard
# Edits the text
# Copies the modified text back to the clipboard
#
# Bryce Frentz
# 8/11/19

import sys
import pyperclip

# Takes text from clipboard
text = pyperclip.paste()


# Separate lines and add a star to the beginning of the line
lines = text.split('\n')
for i in range(len(lines)):
	lines[i] = '* ' + lines[i]

# Join strings back together in one since copy epects a single string
text = '\n'.join(lines)

# Copies text to clipboard
pyperclip.copy(text)
