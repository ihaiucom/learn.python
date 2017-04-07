#!/usr/bin/python
#coding=utf-8
import os
import sys
import getopt
import re
import shutil

def main(argv):

	inputDir = ''
	outputDir = ''

	try:
		pts, args = getopt.getopt(argv, "hi:o:", [ 'idir=', 'odir='])
	except getopt.GetoptError:
		print "recode.py  -i <inputDir> -o <outputDir>"
		sys.exit(2)

	for opt, arg in pts:

		if opt == '-h':
			print "recode.py  -i <inputDir> -o <outputDir>"
			sys.exit()
		elif opt in ['-i', '--idir'] :
			inputDir = arg
		elif opt in ['-o', '--odir'] :
			outputDir = arg


	root = os.getcwd()
	if inputDir == '':
		inputDir = root + "/protocol/retcode.proto"

	if outputDir == '':
		outputDir = root + "/retcode_lange.lua"




	if not os.path.exists(os.path.dirname(outputDir)) :
		os.makedirs(os.path.dirname(outputDir))


	collectDict = {}

	fo = open(outputDir, 'w')

	f = open(inputDir, mode='r')
	lines = f.readlines()
	for line in lines:
		matchObj = re.search( r'= (.*); //(.*)\r\n', line, re.I|re.L)
		if matchObj :
			print '   RETCODE_%s 	=	"%s",' % (matchObj.group(1), matchObj.group(2))
			fo.write( '   RETCODE_%s 	=	"%s",\n' % (matchObj.group(1), matchObj.group(2)) )


	fo.close()
	f.close()

	# content = f.read()

	# matchObj = re.search( r'= (.*); //(.*)\n', content, re.M|re.I|re.L|re.S)
	# i = 0
	# for item in matchObj.groups() :
	# 	print '%d 	%s' % (i, item)
	# 	i = i + 1


	# fo = open(outputDir + "/AssetManager.txt", 'w')
	# for key in collectDict.keys() :
	# 	print "%d 	%s" % (collectDict[key], key)
	# 	fo.write( "%d 	%s\n" % (collectDict[key], key) )
	# 	totalAll = totalAll + collectDict[key]
	# 	totalLine = totalLine + 1
	# fo.close()
	# print

	# print
	# print "collectDict: totalAll=%d, 	totalLine=%d" % (totalAll, totalLine)

	

			


main(sys.argv[1:])