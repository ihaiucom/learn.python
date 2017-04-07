#!/usr/bin/python
#coding=utf-8
import os
import sys
import getopt
import re
import shutil

def main(argv):

	root = ''
	inputDir = ''
	outputDir = ''
	move = False

	try:
		pts, args = getopt.getopt(argv, "hr:i:o:m:", ['root=', 'idir=', 'odir=', 'move='])
	except getopt.GetoptError:
		print "errorLuaGC.py -r <root> -i <inputDir> -o <outputDir>"
		sys.exit(2)

	for opt, arg in pts:

		if opt == '-h':
			print "errorLuaGC.py -r <root> -i <inputDir> -o <outputDir>"
			sys.exit()
		elif opt in ['-r', '--root'] :
			root = arg
		elif opt in ['-i', '--idir'] :
			inputDir = arg
		elif opt in ['-o', '--odir'] :
			outputDir = arg
		elif opt in ['-m', '--move'] :
			move = bool(arg)


	if root  == '':
		root = root = os.getcwd()

	if inputDir == '':
		inputDir = root + "/allSum/c#"

	if outputDir == '':
		outputDir = root + "/allSum/c#_collect"




	print 'root=' + root
	print 'inputDir=' + inputDir
	print 'outputDir=' + outputDir
	print 'move=' +str(move) 
	print 

	if not os.path.exists(outputDir) :
		os.makedirs(outputDir)

	copyDestDir = outputDir + "/LuaGC"
	if not os.path.exists(copyDestDir) :
		os.makedirs(copyDestDir)



	num = 0
	dirs = os.listdir( inputDir )
	for file in dirs:
		path = os.path.join(inputDir, file)
		if not os.path.isdir(path) and path.endswith(".txt"):
			f = open(path, mode='r')
			content = f.read()

			matchObj = re.search( r'LuaClient\.LuaGC', content, re.M|re.I)
			if matchObj:
				num = num + 1

			f.close()

			if move and matchObj :
				dest = os.path.join(copyDestDir, file)
				shutil.move(path, dest)




	print
	print "num: %d" % (num)

			


main(sys.argv[1:])