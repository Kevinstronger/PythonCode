#coding=UTF-8
import math

#Python print函数用法，print 格式化输出
'''
使用print输出各种类型：
字符串
整数
浮点数
出度及精度控制
'''
#1. 格式化输出整数
strHello = "Hello, Python."
fStr = "The length of '%s' is %d" %('strHello', len('strHello'))
print fStr
#输入结果: The length of 'strHello' is 8

#2. 格式化输出浮点（float）
print "PI=%f" %math.pi
#width = 10, precise = 3, align = left
print "PI=%10.3f" %math.pi
#width = 10, precise = 3, align = right
print "PI=%-10.3f" %math.pi
#前面填充字符
print "PI=%06d" %int(math.pi)
#%f 格式符选项对应一个十进制浮点数，不指定精度时打印 6 位小数
print "Today's stock price: %f" %50.4625
#使用包含“.2”精度修正符的 %f 格式符选项将只打印 2 位小数。
print "Today's stock price: %.2f" %50.4625
#添加 + 修正符用于在数值之前显示一个正号或负号。注意“.2”精度修正符仍旧在它原来的位置，用于只打印 2 位小数。
print "Change since yesterday: %+.2f" %1.5
'''
输出结果为：
PI=3.141593
PI=     3.142
PI=3.142     
PI=000003
Today's stock price: 50.462500
Today's stock price: 50.46
Change since yesterday: +1.50
'''
#3. 格式化字符串
uid = "sa"
pwd = "secret"
print "%s is not a good password for %s." %(pwd, uid)
#(userCount, ) 是一个只包含一个元素的 tuple。是的，语法有一点奇怪，但是使用它的理由就是：显示地指出它是一个 tuple，而不是其他。实际上，当定义一个 list、tuple 或 dictionary 时，您可以总是在最后一个元素后面跟上一个逗号，但是当定义一个只包含一个元素的 tuple 时逗号是必须的。如果省略逗号，Python 不会知道 (userCount) 究竟是一个只包含一个元素的 tuple 还是变量 userCount 的值。
#字符串格式化通过将 %s 替换成 %d 即可处理整数。
userCount = 6
print "Users connected: %d" %(userCount, ) 
'''
输出结果：
secret is not a good password for sa.
Users connected: 6
'''
