from sys import argv

script, user_name = argv
prompt = "> "

print "Hi %s, I'm the %s script." %(user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" %user_name
likes = raw_input(prompt)

print "Where do you live %s?" %user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" %(likes, lives, computer)
'''
Result:
Hi Andy, I'm the D:\PY_Workspace\FirstPro\src\training\ex14.py script.
I'd like to ask you a few questions.
Do you like me Andy?
> yes
Where do you live Andy?
> Beijing
What kind of computer do you have?
> IBM

Alright, so you said 'yes' about liking me.
You live in 'Beijing'. Not sure where that is.
And you have a 'IBM' computer. Nice.
'''