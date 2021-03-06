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

	LoadAssetBundleFromFileRoot = outputDir + "/LoadAssetBundleFromFile"
	if not os.path.exists(LoadAssetBundleFromFileRoot) :
		os.makedirs(LoadAssetBundleFromFileRoot)


	LoadAssetBundleFromFileDict = {}

	dirs = os.listdir( inputDir )
	for file in dirs:
		path = os.path.join(inputDir, file)
		if not os.path.isdir(path) and path.endswith(".txt"):
			f = open(path, mode='r')
			content = f.read()

			# LoadAssetBundleFromFile
			matchObj = re.match( r'\[Error\] LoadAssetBundleFromFile assetBundle=null,  assetBundleName=(.*),', content, re.M|re.I)
			if matchObj:
				assetBundlue = matchObj.group(1)
				if not LoadAssetBundleFromFileDict.has_key(assetBundlue) :
					LoadAssetBundleFromFileDict[assetBundlue] = 1
				else:
					LoadAssetBundleFromFileDict[assetBundlue] = LoadAssetBundleFromFileDict[assetBundlue] + 1


			f.close()

			if move and matchObj :
				dest = os.path.join(LoadAssetBundleFromFileRoot, file)
				shutil.move(path, dest)

	totalAll = 0
	totalLine = 0
	fo = open(outputDir + "/LoadAssetBundleFromFileDict.txt", 'w')
	for assetBundle in LoadAssetBundleFromFileDict.keys() :
		print "%d 	%s" % (LoadAssetBundleFromFileDict[assetBundle], assetBundle)
		fo.write( assetBundle + "\n")
		totalAll = totalAll + LoadAssetBundleFromFileDict[assetBundle]
		totalLine = totalLine + 1


	print
	print "LoadAssetBundleFromFileDict: totalAll=%d, 	totalLine=%d" % (totalAll, totalLine)

	fo.close()
			


main(sys.argv[1:])