#!/usr/bin/python
#coding=utf-8

import os
import sys
import re
import shutil

def lenOfIter(iterParam):
	return len(list(iterParam))

def lineNumber(strParam, pos):
	line = 1
	for x in range(pos):
		s = strParam[x]
		if s == "\n":
			line += 1

	return str(line)

def classifySum(sumPath):
	fileDir = sumPath
	files = os.listdir(sumPath)

	luaPath = fileDir + "/lua/"
	if os.path.exists(luaPath):
		shutil.rmtree(luaPath)
	os.mkdir(luaPath)

	csPath = fileDir + "/c#/"
	if os.path.exists(csPath):
		shutil.rmtree(csPath)
	os.mkdir(csPath)

	for fi in files:
		path = os.path.join(fileDir, fi)
		if not os.path.isdir(path) and os.path.splitext(path)[1][1:] == "txt":
			f = open(path, mode="r")
			r = f.read()
			
			mat = re.search("\nstack traceback:\n", r, re.MULTILINE)
			matLua = re.search("\[Exception\]\sLuaScriptException\:", r)
			src = fileDir + "/" + fi
			if mat or matLua:
				mat2 = re.search("\[.+/(.+)\"\]\:(\d+)\:.+\nstack\straceback:", r)
				if mat2:
					luaChildPath = luaPath + "[" + mat2.group(1) + "]" + mat2.group(2)
					if not os.path.exists(luaChildPath):
						os.mkdir(luaChildPath)

					luaChildPath += "/" + fi
					print("copying :" + luaChildPath + "...")
					shutil.copy(src, luaChildPath)
				else:
					luacpPath = luaPath + fi
					print("copying :" + luacpPath + "...")
					shutil.copy(src, luacpPath)
			else:
				cscpPath = csPath + fi
				print("copying :" + cscpPath + "...")
				shutil.copy(src, cscpPath)

def main():
	fileDir = os.getcwd()
	files = os.listdir(fileDir)

	# luaPath = fileDir + "/lua/"
	# if os.path.exists(luaPath):
	# 	shutil.rmtree(luaPath)
	# os.mkdir(luaPath)

	# csPath = fileDir + "/c#/"
	# if os.path.exists(csPath):
	# 	shutil.rmtree(csPath)
	# os.mkdir(csPath)

	allSum = {}
			
	for fi in files:
		path = os.path.join(fileDir, fi)
		if not os.path.isdir(path) and os.path.splitext(path)[1][1:] == "txt":
			f = open(path, mode="r")
			r = f.read()

			# mat = re.search("============= one log end ===========================================================================================================", r, re.MULTILINE)
			# matLua = re.search("\[Exception\]\sLuaScriptException\:", r)
			# src = fileDir + "/" + fi
			# if mat or matLua:
			# 	mat2 = re.search("\[.+/(.+)\"\]\:(\d+)\:.+\nstack\straceback:", r)
			# 	if mat2:
			# 		luaChildPath = luaPath + "[" + mat2.group(1) + "]" + mat2.group(2)
			# 		if not os.path.exists(luaChildPath):
			# 			os.mkdir(luaChildPath)

			# 		luaChildPath += "/" + fi
			# 		print("copying :" + luaChildPath + "...")
			# 		shutil.copy(src, luaChildPath)
			# 	else:
			# 		luacpPath = luaPath + fi
			# 		print("copying :" + luacpPath + "...")
			# 		shutil.copy(src, luacpPath)
			# else:
			# 	cscpPath = csPath + fi
			# 	print("copying :" + cscpPath + "...")
			# 	shutil.copy(src, cscpPath)

			def func(content, pos):
				if allSum.has_key(content):
					allSum[content]["path"] += "\n\t" + path + "(line:" + pos + ")"
					allSum[content]["count"] += 1
				else:
					allSum[content] = {"content":content, "path":"\t" + path + "(line:" + pos + ")", "count":1}

			sumMat1 = re.finditer("^\[string[\d\D]+?\n\n", r, re.MULTILINE)
			for it in sumMat1:
				func(it.group(0), lineNumber(r, it.start()))

			sumMat2 = re.finditer("^\[Exception\][\d\D]+?\n\n\n", r, re.MULTILINE)
			for it in sumMat2:
				func(it.group(0), lineNumber(r, it.start()))

			sumMat3 = re.finditer("^^\[Error\][\d\D]+?\n\n", r, re.MULTILINE)
			for it in sumMat3:
				func(it.group(0), lineNumber(r, it.start()))

	sumFile = "allSum"
	if os.path.exists(sumFile):
		shutil.rmtree(sumFile)

	os.mkdir(sumFile)

	allSumArr = sorted(allSum.iteritems(), key=lambda d:d[1]["count"], reverse=True)


	fileName = sumFile + "/Num({0})Count({1}).txt"
	number = 1
	for key, it in allSumArr:
		f = open(fileName.format(number, it["count"]), mode="w+")
		f.write(it["content"])
		f.write("relate path:\n[\n")
		f.write(it["path"])
		# f.write("\n]\n\n\n\n=========================================\n\n=========================================\n\n\n\n")
		f.close()
		number += 1

	classifySum(sumFile)

main()