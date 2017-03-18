#!/usr/bin/python
#coding=utf-8




print "========="
print "[行和缩进]"
print "学习Python与其他语言最大的区别就是，Python的代码块不使用大括号（{}）来控制类，函数以及其他逻辑判断。python最具特色的就是用缩进来写模块。"
print "缩进的空白数量是可变的，但是所有代码块语句必须包含相同的缩进空白数量，这个必须严格执行。如下所示："

if True:
	print "True Code Block"
	print "he he"
else:
	print "False Code Block"





print ""
print "========="
print "[多行语句]"
print "Python语句中一般以新行作为为语句的结束符。"
print "但是我们可以使用斜杠（ \）将一行的语句分为多行显示，如下所示："


total = 1 + 2 \
	+3 \
	+4
print total

print "Hello\
 World"

print "\n------"
print "语句中包含[], {} 或 () 括号就不需要使用多行连接符。如下实例："
arr = [  1
		,2
		,3
		,4]

print arr


print ""
print "========="
print "[Python 引号]"
print """Python 可以使用引号( \' )、双引号( \" )、三引号( \'\'\' 或 \"\"\" ) 来表示字符串，引号的开始与结束必须的相同类型的。
其中三引号可以由多行组成，编写多行文本的快捷语法，常用语文档字符串，在文件的特定地点，被当做注释。"""

print '单引号测试'
print "双引号测试"

print """ 三引号
		测试 """

print ''' 三引号
 		测试2 '''

'''
这是多行注释，使用单引号。
这是多行注释，使用单引号。
这是多行注释，使用单引号。
'''

"""
这是多行注释，使用双引号。
这是多行注释，使用双引号。
这是多行注释，使用双引号。
"""

#注释1
print "注释" #注释2


