#!/usr/bin/python
#coding=utf-8

# http://www.runoob.com/python/python-command-line-arguments.html

print "\n============="
print "[Python 命令行参数]"
print "Python 提供了 getopt 模块来获取命令行参数。"
print "Python 中也可以所用 sys 的 sys.argv 来获取命令行参数："
print "		sys.argv 是命令行参数列表。"
print "		len(sys.argv) 是命令行参数个数。"
print "		注：sys.argv[0] 表示脚本名。"

import sys

print "\n~~~~"
print "# sys.argv"
print sys.argv

print "\n~~~~"
print "# len(sys.argv)"
print len(sys.argv)


print "\n~~~~"
print "# sys.argv[0]"
print sys.argv[0]
