from sys import argv

from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" %(from_file, to_file)

#we could do these two on one line too, how?
in_file = open(from_file)
indata = in_file.read()

print "The input file is %d butes long." %len(indata)

print "Does the output file exist? %r" %exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

out_file = open(to_file, 'w')
out_file.write(indata)

print "Alright, all done."

out_file.close()
in_file.close()
'''
结果：
源文件： ex17_src.txt, 目标文件： ex17_target.txt
考本结果：
Who are you?
Where are you from?
Where are you going?
'''
