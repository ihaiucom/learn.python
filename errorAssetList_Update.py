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

	copyDestDir = outputDir + "/更新资源读取资源列表失败"
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

			matchObj = re.search( r'\[Error\] 更新资源读取资源列表失败 updateAssetListUrl=(.*),', content, re.M|re.I)
			if matchObj:
				num = num + 1


				msg = matchObj.group(1)
				# collectDict
				if not collectDict.has_key(msg) :
					collectDict[msg] = 1
				else:
					collectDict[msg] = collectDict[msg] + 1

			f.close()

			if move and matchObj :
				dest = os.path.join(copyDestDir, file)
				shutil.move(path, dest)




	totalAll = 0
	totalLine = 0

	fo = open(outputDir + "/更新资源读取资源列表失败.txt", 'w')
	for key in collectDict.keys() :
		print "%d 	%s" % (collectDict[key], key)
		fo.write( "%d 	%s\n" % (collectDict[key], key))
		totalAll = totalAll + collectDict[key]
		totalLine = totalLine + 1
	fo.close()
	print


	print
	print "num: %d" % (num)
	print
	print "collectDict: totalAll=%d, 	totalLine=%d" % (totalAll, totalLine)

			


main(sys.argv[1:])