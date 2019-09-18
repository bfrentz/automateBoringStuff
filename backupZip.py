#! /usr/bin/python3
# backupZip.py - creates a .zip snapshot of the current working folder. Automatically increments the zip filename
#
# Bryce Frentz
# 9/18/19

import zipfile, os, sys

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

	# Create the zipfile
	print('Creating %s...' % (zipFilename))
	backupZip = zipfile.ZipFile(zipFilename, 'w')

	# Walk through folder and compress the files
	for folderName, subFolders, fileNames in os.walk(folder):
		print('Adding files in %s...' % (folderName))
		backupZip.write(folderName)		# Add current folder to the Zip

		# Add files in this foder to the zip
		for filename in fileNames:
			newBase = os.path.basename(folder) + '_'
			if filename.startswith(newBase) and filename.endswith('.zip'):
				continue	# don't backup the other backups
			backupZip.write(os.path.join(folderName, filename))

	backupZip.close()
	print('Done.')



backupTarget = ''

if len(sys.argv) > 2:
	print("ERROR: Too many arguments.")
	sys.exit()
elif len(sys.argv) == 2:
	backupTarget = sys.argv[1]
	#print(backupTarget)

if not os.path.exists(backupTarget):
	backupTarget = os.getcwd()
	
#print(backupTarget)
backupToZip(backupTarget)
