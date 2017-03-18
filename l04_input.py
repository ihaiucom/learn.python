#!/usr/bin/python
#coding=utf-8

# http://www.runoob.com/python/python-basic-syntax.html


print ""
print "========="
print "[等待用户输入]"
raw_input ("\n\n 请在这里输入Enter键退出:")



print ""
print "========="
print "[同一行显示多条语句]"
print "Python可以在同一行中使用多条语句，语句之间使用分号(;)分割，以下是一个简单的实例："
import sys; x='abc'; sys.stdout.write(x + '\n');



print ""
print "========="
print "[Print 输出]"
print "print 默认输出是换行的，如果要实现不换行需要在变量末尾加上逗号："

x = 'a'
y = 'b'
print x
print y

print '---------'

print x,
print y,

print 
print '---------'
print x, y