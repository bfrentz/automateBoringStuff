#! /usr/bin/python3
# isPhoneNumber.py - Program to determine if input text is a phone number or not
# uses both traditional coding and regular expressions
#
# Bryce Frentz
# 8/12/19



# Lots of individual checks to see if something is a phone number. Slow code. Especially if you wanted to add something to detect the pattern in aside of a larger string.

def isPhoneNumber(text):
	if len(text) != 12:
		return False
	for i in range(0,3):
		if not text[i].isdecimal():
			return False
	if text[3] != text[7] or text[3] != '-':
		return False
	for i in range(4,7):
		if not text[i].isdecimal():
			return False
	for i in range(8,12):
		if not text[i].isdecimal():
			return False
	return True
		
"""
# To look for a number in a larger string:
message = 'Call me at 415-555-0331 tomorrow. 514-555-8484 is the general office number if you\'re unable to reach me.'
for i in range(len(message)):
        chunk = message[i:i+12]
        if isPhoneNumber(chunk):
                print('Phone number found: ' + chunk)
print('Done')

"""

# All of the above can be done more simply and efficiently using regular experessions. These also allow for other formats (XXX) XXX-XXXX
# Regular expressions are descriptions for a pattern of text
# \d\d\d-\d\d\d-\d\d\d\d is the expression to handle the code we previously wrote
# can also use curly braces to repeat pattern:
# \d{3}-\d{3}-\d{4}
# 
# Use re module
#
# Useing the ? character flags a preceeding group as optional in terms of the pattern
# the * character allows for match zero or more (optional or any number of times)
# the + character means to match one or more (requiring at least one match)

import re

# r" " is a raw string and doesn't allow for escape characters
# adding parenthesis will create different groups of searchable text
#
#phoneNumRegex = re.compile(f'(\d{3})-(\d{3}-\d{4})')


def main():
	
	user = 1
	
	phoneNumRegex = re.compile(r'(\d{3}-)?(\d{3}-\d{4})')

	while int(user) != 0:
		number = input("Please enter your text.\n")
		
		mo = phoneNumRegex.search(number)
		print(mo.group(1))
		print(mo.group(2))
		print(mo.group(0))
		print(mo.groups())

		areaCode, mainNumber = mo.groups()
		print(areaCode)
		print(mainNumber)

		#if isPhoneNumber(number):
		#	print(number + " is a valid phone number.")
		#else:
		#	print(number + " is not a valid phone number.")
		
		user = input("Do you want to continue? (Enter 1 to continue or 0 to quit)")

	print("Thank you for using the number checker. Goodbye.")


main()
