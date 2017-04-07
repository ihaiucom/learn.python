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

	copyDestDir = outputDir + "/No Find Path"
	if not os.path.exists(copyDestDir) :
		os.makedirs(copyDestDir)


	collectDict = {}

	num = 0
	dirs = os.listdir( inputDir )
	for file in dirs:
		path = os.path.join(inputDir, file)
		if not os.path.isdir(path) and path.endswith(".txt"):
			f = open(path, mode='r')
			content = f.read()

			matchObj = re.search( r'\[Error\] from=(.*), to=(.*), key=(.*) not find path', content, re.M|re.I)
			if matchObj:
				num = num + 1
				assetBundlue = matchObj.group(3)
				# collectDict
				if not collectDict.has_key(assetBundlue) :
					collectDict[assetBundlue] = 1
				else:
					collectDict[assetBundlue] = collectDict[assetBundlue] + 1

			f.close()

			if move and matchObj :
				dest = os.path.join(copyDestDir, file)
				shutil.move(path, dest)



	fo = open(outputDir + "/No Find Path.txt", 'w')
	for key in collectDict.keys() :
		print "\n\n%d\n%s" % (collectDict[key], key)
		fo.write( "\n\n%d\n%s\n" % (collectDict[key], key))
	fo.close()


	print
	print "num: %d" % (num)

			


main(sys.argv[1:])