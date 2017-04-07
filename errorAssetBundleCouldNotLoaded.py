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

	copyDestDir = outputDir + "/AssetBundleCouldNotLoaded"
	if not os.path.exists(copyDestDir) :
		os.makedirs(copyDestDir)


	collectDict = {}
	collectPlatformDict = {}
	collectChannelDict = {}
	collectSimpleDict = {}

	dirs = os.listdir( inputDir )
	for file in dirs:
		path = os.path.join(inputDir, file)
		if not os.path.isdir(path) and path.endswith(".txt"):
			f = open(path, mode='r')
			content = f.read()

			matchObj = re.search( r'\[Error\] The AssetBundle \'(.*)\' could not be loaded', content, re.M|re.I)
			if matchObj:
				assetBundlue = matchObj.group(1)
				# collectDict
				if not collectDict.has_key(assetBundlue) :
					collectDict[assetBundlue] = 1
				else:
					collectDict[assetBundlue] = collectDict[assetBundlue] + 1


				# collectPlatformDict
				if assetBundlue.find("Platform/Android/") > 0:
					if not collectPlatformDict.has_key("Android") :
						collectPlatformDict["Android"] = 1
					else:
						collectPlatformDict["Android"] = collectPlatformDict["Android"] + 1
				elif assetBundlue.find("Platform/IOS/") > 0:
					if not collectPlatformDict.has_key("IOS") :
						collectPlatformDict["IOS"] = 1
					else:
						collectPlatformDict["IOS"] = collectPlatformDict["IOS"] + 1
				else :
					if not collectPlatformDict.has_key("Other") :
						collectPlatformDict["Other"] = 1
					else:
						collectPlatformDict["Other"] = collectPlatformDict["Other"] + 1


				assetBundlue = assetBundlue.replace("!assets/Platform/Android/", "://").replace("Platform/IOS/", "://").replace("Platform/OSX/", "://").replace("Platform/Windows/", "://")
				arr = assetBundlue.partition("://")
				chancel = arr[0]
				asset = arr[2]

				# collectChannelDict
				if not collectChannelDict.has_key(chancel) :
					collectChannelDict[chancel] = 1
				else:
					collectChannelDict[chancel] = collectChannelDict[chancel] + 1


				# collectSimpleDict
				if not collectSimpleDict.has_key(asset) :
					collectSimpleDict[asset] = 1
				else:
					collectSimpleDict[asset] = collectSimpleDict[asset] + 1



			f.close()

			if move and matchObj :
				dest = os.path.join(copyDestDir, file)
				shutil.move(path, dest)

	totalAll = 0
	totalLine = 0

	fo = open(outputDir + "/AssetBundleCouldNotLoaded.txt", 'w')
	for key in collectDict.keys() :
		print "%d 	%s" % (collectDict[key], key)
		fo.write( key + "\n")
		totalAll = totalAll + collectDict[key]
		totalLine = totalLine + 1
	fo.close()
	print

	totalSimalAll = 0
	totalSimalLine = 0
	fo = open(outputDir + "/AssetBundleCouldNotLoaded simple.txt", 'w')
	for key in collectSimpleDict.keys() :
		print "%d 	%s" % (collectSimpleDict[key], key)
		fo.write( key + "\n")
		totalSimalAll = totalSimalAll + collectSimpleDict[key]
		totalSimalLine = totalSimalLine + 1
	fo.close()


	print
	for key in collectChannelDict.keys() :
		print "%d 	%s" % (collectChannelDict[key], key)

	print
	for key in collectPlatformDict.keys() :
		print "%d 	%s" % (collectPlatformDict[key], key)

	print
	print "collectDict: totalAll=%d, 	totalLine=%d" % (totalAll, totalLine)
	print "collectSimpleDict: totalAll=%d, 	totalLine=%d" % (totalSimalAll, totalSimalLine)

	

			


main(sys.argv[1:])