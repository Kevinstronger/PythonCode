#coding=UTF-8
#字典的操作
stuff = {'name': 'Zed', 'age': 36, 'height': 6*12+2}
print stuff['name']
print stuff['age']
print stuff['height']

stuff['city'] = 'San Francisco'
print stuff['city']

stuff[1] = 'WOW'
stuff[2] = 'Neato'

print stuff[1]
print stuff[2]

print stuff

#删除字典中的元素
del stuff['city']
del stuff[1]
del stuff[2]

print stuff
'''
Result:
Zed
36
74
San Francisco
WOW
Neato
{'city': 'San Francisco', 2: 'Neato', 'name': 'Zed', 1: 'WOW', 'age': 36, 'height': 74}
{'name': 'Zed', 'age': 36, 'height': 74}

'''
