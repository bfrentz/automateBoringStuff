#! /usr/bin/python3
# backupZip.py - creates a .zip snapshot of the current working folder. Automatically increments the zip filename
#
# Bryce Frentz
# 9/18/19

import zipfile, os

# Backup the entire contents of "folder" into a zip file
def backupToZip(folder):

	folder = os.path.abspath(folder)	# ensure that folder is an absolute path

	# determine the filename that the code should use based on what already exists, for iteration purposes
	number = 1
	while True:
		zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
		if not os.path.exists(zipFilename):
			break
		number += 1
