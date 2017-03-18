#!/usr/bin/python
#coding=utf-8

# http://www.runoob.com/python/python-command-line-arguments.html

import sys, getopt
print "[getopt模块]"
print "getopt模块是专门处理命令行参数的模块，用于获取命令行选项和参数，也就是sys.argv。命令行选项使得程序的参数更加灵活。支持短选项模式（-）和长选项模式（--）。\n\
该模块提供了两个方法及一个异常处理来解析命令行参数。\n"

print "#getopt.getopt 方法"
print "\n	getopt.getopt(args, options[, long_options])\n"
print "方法参数说明："
print """		args: 要解析的命令行参数列表。
		options: 以列表的格式定义，options后的冒号(:)表示该选项必须有附加的参数，不带冒号表示该选项不附加参数。
		long_options: 以字符串的格式定义，long_options 后的等号(=)表示如果设置该选项，必须有附加的参数，否则就不附加参数。
		该方法返回值由两个元素组成: 第一个是 (option, value) 元组的列表。 第二个是参数列表，包含那些没有'-'或'--'的参数。"""

def main(argv):
	inputFile = ''
	outputFile = ''

	try:
		pts, args = getopt.getopt(argv, "hi:o:", ['ifile=', 'ofile='])
	except getopt.GetoptError:
		print "l06_getopt.py -i <inputFile> -o <outputFile>"
		sys.exit(2)

	for opt, arg in pts:

		if opt == '-h':
			print "l06_getopt.py -i <inputFile> -o <outputFile>"
			sys.exit()
		elif opt in ['-i', '--ifile'] :
			inputFile = arg
		elif opt in ['-o', '--ofile'] :
			outputFile = arg

	print 'inputFile=' + inputFile
	print 'outputFile=' + outputFile


print sys.argv
print sys.argv[1:]
if __name__ == '__main__':
	main(sys.argv[1:])



