#coding=UTF-8
i = 0
numbers = []

while i < 6:
    print "At the top i is %d" %i 
    numbers.append(i)
    
    i = i + 1
    print "Numbers now:", numbers
    print "At the bottom i is %d" %i
print "The numbers:"
for num in numbers:
    print num

'''
Result:
At the top i is 0
Numbers now: [0]
At the bottom i is 1
At the top i is 1
Numbers now: [0, 1]
At the bottom i is 2
At the top i is 2
Numbers now: [0, 1, 2]
At the bottom i is 3
At the top i is 3
Numbers now: [0, 1, 2, 3]
At the bottom i is 4
At the top i is 4
Numbers now: [0, 1, 2, 3, 4]
At the bottom i is 5
At the top i is 5
Numbers now: [0, 1, 2, 3, 4, 5]
At the bottom i is 6
The numbers:
0
1
2
3
4
5
'''
#将这个 while 循环改成一个函数，将测试条件(i < 6)中的 6 换成一个变量。
def append_num(num):
    i = 0
    numbers = []
    while i < num:
        print "At the top i is %d" %i 
        numbers.append(i)
        i = i + 1
    return numbers

count = append_num(6)
print "The count----------:"
for num in count:
    print num

