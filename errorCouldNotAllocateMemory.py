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
		print "errorLoad.py -r <root> -i <inputDir> -o <outputDir>"
		sys.exit(2)

	for opt, arg in pts:

		if opt == '-h':
			print "errorLoad.py -r <root> -i <inputDir> -o <outputDir>"
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

	copyDestDirTempOverflow = outputDir + "/CouldNotAllocateMemory TempOverflow"
	if not os.path.exists(copyDestDirTempOverflow) :
		os.makedirs(copyDestDirTempOverflow)


	copyDestDirTempJobAlloc = outputDir + "/CouldNotAllocateMemory TempJobAlloc"
	if not os.path.exists(copyDestDirTempJobAlloc) :
		os.makedirs(copyDestDirTempJobAlloc)


	collectDict = {}
	collectDictSize = {}
	collectTempOverflowDict = {}
	collectTempJobAllocDict = {}

	collectTempOverflowCountDict = {}
	collectTempJobAllocCountDict = {}

	dirs = os.listdir( inputDir )
	for file in dirs:
		path = os.path.join(inputDir, file)
		if not os.path.isdir(path) and path.endswith(".txt"):
			f = open(path, mode='r')
			content = f.read()

			matchObj = re.search( r'\[Error\] Could not allocate memory: System out of memory!\nTrying to allocate: (.*)B with 16 alignment. MemoryLabel: (.*)\n', content, re.M|re.I)
			if matchObj:
				size = (float(matchObj.group(1)) / 1024 / 1024) 
				label = matchObj.group(2)

				if not collectDict.has_key(label) :
					collectDict[label] = 1
					collectDictSize[label] = []
				else:
					collectDict[label] = collectDict[label] + 1


				collectDictSize[label].append( size )


				if move:
					copyDestDir = copyDestDirTempOverflow
					if label == "TempJobAlloc" :
						copyDestDir = copyDestDirTempJobAlloc
					dest = os.path.join(copyDestDir, file)
					shutil.move(path, dest)



			f.close()


	totalAll = 0
	totalLine = 0


	fo = open(outputDir + "/CouldNotAllocateMemory.txt", 'w')

	for key in collectDict.keys() :
		print "%d 	%s" % (collectDict[key], key)
		fo.write(str(collectDict[key]) + "   " + key + "\n")

		
	fo.write("\n")
	for key in collectDict.keys() :

		sizeList = collectDictSize[key]
		sizeList.sort();
		fo.write( "\n" + key + "  " + str(len(sizeList) )+ "\n")
		print "\n" + key + "  " + str(len(sizeList))
		for size in sizeList :
			print size
			fo.write( str(size) + " MB\n")


		
	fo.close()
	print


	

			


main(sys.argv[1:])