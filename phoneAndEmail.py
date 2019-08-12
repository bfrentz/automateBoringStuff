#! /usr/bin/python3
# phoneAndEmail.py
# Finds phone numbers and email addresses from all text currently on clipboard

# Bryce Frentz
# 8/12/19
#
# Road Map:
#
# Get text from clipboard
# Find all phone numbers and email addresses in the text
# Paste the to the clipboard
#

import sys
import re
import pyperclip


# regular expression for phone numbers
# includes options for extensions and many different types of listing the number (w/ or w/o area code, parenthesis, spaces, dashes, etc)
phoneRegex = re.compile(r'''(
	(\d{3}|\(\d{3}\))?		# area code, with or without parentheses, optional
	(\s|-|\.)?			# separator, either a space, dash, or dot, optional
	(\d{3})				# first three digits
	(\s|-|\.)			# separator, either a space, dash, or dot
	(\d{4})				# last four digits
	(\s*(ext|x|ext.)\s*(\d{2,5}))?	# extension, listed as ext, x, or ext., followed by number of length 2-5 digits
	)''', re.VERBOSE)


# My regular expression for emails, I think it'll accept anything
emailRegex = re.compile(r'''(
	(.*)			# username, takes anything between the space and @ symbol for the identifier
	@			# @ symbol
	(.*)			# domain name
	\.			# dot
	(.*)			# top-level domain
	)''', re.VERBOSE)

# From book, which will accept almost every email address possible
emailRegexAl = re.compile(r'''(
	[a-zA-Z0-9._%+-]+	# username, taking all alphanumeric and special characters allowable, requires at least one but can be as long as necessary
	@			# @ symbol
	[a-zA-Z0-9.-]+		# domain name, accepts all alphanumeric and allowable special characters, requiring one character but can be as long as necessary
	(\.[a-zA-Z]{2,4})	# dot-something, includes dot, can accept all alphanumeric characters and restricts length between 2-4 characters long
	)''', re.VERBOSE)


# FIND IN CLIPBOARD TEXT


# COPY RESULTS TO CLIPBOARD
