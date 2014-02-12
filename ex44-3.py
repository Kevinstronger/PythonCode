class parent(object):
    def altered(self):
        print "PARENT altered()"
    
class Child(parent):
    def altered(self):
        print "CHILD, BEFORE PARENT altered()"
        super(Child, self).altered()
        print "CHILD, AFTER PARENT altered()"

dad = parent()
son = Child()

dad.altered()
son.altered()
'''
Result:
PARENT altered()
CHILD, BEFORE PARENT altered()
PARENT altered()
CHILD, AFTER PARENT altered()
'''