#! /usr/bin/python3
# dateChanger.py - Changes filenames in directories from American date (MM-DD-YYYY) to European (DD-MM-YYYY)
#
# Bryce Frentz
# 9/18/19

"""
Searches all filenames in the curent workin gdirectory for american style dates
Renames files (when found) with the month and day swapped)
"""

import shutil, os, re

# Create a regex pattern for finding american dates
datePattern = re.compile(r"""^(.*?)	# All text before date appears
	((0|1)?\d)-						# one or two digits for the month
	((0|1|2|3)?\d)-					# One or two digits, 0-3, for day
	((19|20)\d\d)					# four digits for the year starting in 19 or 20
	(.*?)$							# all text after the date
	""", re.VERBOSE)
	

# Loop over files and scan for american names
for americanFilename in os.listdir('.'):
	mo = datePattern.search(americanFilename)

	# Skip files w/o dates
	if mo == None:
		continue

	# get the different parts of filename
	beforePart = mo.group(1)
	monthPart = mo.group(2)
	dayPart = mo.group(4)
	yearPart = mo.group(6)
	afterPart = mo.group(8)

	# create strings for european file names
	euroFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart

	absWorkingDirectory = os.path.abspath('.')
	americanFilename = os.path.join(absWorkingDirectory, americanFilename)
	euroFilename = os.path.join(absWorkingDirectory, euroFilename)

	# rename the files
	print('Renaming "%s" to "%s"...' % (americanFilename, euroFilename))
	shutil.move(americanFilename, euroFilename)
