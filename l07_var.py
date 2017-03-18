#!/usr/bin/python
#coding=utf-8

# http://www.runoob.com/python/python-variable-types.html

numA = 1
numB = 2

numC = numD = 3

age, name, sex = 20, 'ZF', '男'

print numA, numB, numC, numD
print age, name, sex

del numD


print numA, numB, numC
print age, name, sex

str = "abcdefg"
print str
print str[0]
print str[-1]
print str[1:3]
print str[1:]
print str[:3]
print len(str)

print 

a = 'abc'
b = '123'

print a
print b

print a + b
print a * 2
print a * 0
print a * 1
print a * 10


listA =['Hello', 'World', 2017]
listB = ["年", 3, '月', 17, '日']

listC = listA + listB

print listA
print listB
print listC

print listC[1:6]

listD = listA * 5
print listD


print
print '========'
print """Python元组
元组是另一个数据类型，类似于List（列表）。
元组用"()"标识。内部元素用逗号隔开。但是元组不能二次赋值，相当于只读列表。"""

tupleA = ("A", "B", "C", 1, 2, 3)
print tupleA
print tupleA * 2
print tupleA[1:4]
