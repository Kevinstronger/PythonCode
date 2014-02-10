#coding=UTF-8
from sys import argv

script, filename = argv

txt = open(filename)

print "Here's your file %r:" %filename
print txt.read()

print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()
'''
Here's your file 'ex15_sample.txt':
This is stuff I typed into a file.
It is really cool stuff.
Lots and lots of fun to have in here.
这是第一个读取文件的示例代码。
Type the filename again:
> ex15_sample.txt
This is stuff I typed into a file.
It is really cool stuff.
Lots and lots of fun to have in here.
这是第一个读取文件的示例代码。
'''