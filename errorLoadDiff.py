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
	print 

	pathA = outputDir + "/LoadAssetBundleFromFileDict.txt"
	pathB = outputDir + "/Unable to open archive file simple.txt"

	dictA = {}
	dictB = {}

	fo = open(pathA, "r")
	lines = fo.readlines()
	for item in lines:
		dictA[item.replace("\n", "")] = 1
	fo.close()


	fo = open(pathB, "r")
	lines = fo.readlines()
	for item in lines:
		dictB[item.replace("\n", "")] = 1
	fo.close()


	listDiffAdd = []
	listDiffRemove = []
	listDiffSame = []

	for key in dictB.keys():
		if dictA.has_key(key) :
			listDiffSame.append(key)
		else:
			listDiffAdd.append(key)


	for key in dictA.keys():
		if not dictB.has_key(key) :
			listDiffRemove.append(key)




	pathDiff = outputDir + "/LoadDiff-Same.txt"
	fo = open(pathDiff, 'w')
	for item in listDiffSame :
		print "E 	%s" % (item)
		fo.write( item + "\n")
	fo.close()


	pathDiff = outputDir + "/LoadDiff-Delete.txt"
	fo = open(pathDiff, 'w')
	for item in listDiffRemove :
		print "D 	%s" % (item)
		fo.write( item + "\n")
	fo.close()

	pathDiff = outputDir + "/LoadDiff-Add.txt"
	fo = open(pathDiff, 'w')
	for item in listDiffAdd :
		print "A 	%s" % (item)
		fo.write( item + "\n")
	fo.close()






	print
	print "Diff: same=%d, 	add=%d, 	del=%d" % (len(listDiffSame), len(listDiffAdd), len(listDiffRemove))



	

			


main(sys.argv[1:])