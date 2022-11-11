# Exercise 2: Write a program to look for lines of the form: 
# 
# New Revision: 39772
# 
# Extract the number from each of the lines using a regular expression and the
# findall() method. Compute the average of the numbers and print out the average
# as an integer. 
# 
# Enter file:mbox.txt 
# 38549 
# 
# Enter file:mbox-short.txt 
# 39756

from itertools import count
import re

name = input('Enter a file name:')
if len(name) < 1 :
    name = 'mbox.txt'

try :
    handle = open(name)
except :
    print('FILE NOT FOUND')
    quit()

revs = list()
for line in handle :
    line = line.rstrip()
    # I had '^N.+:.([0-9]*)' put it but that one didn't work on mbox.txt -> Changed
    rev = re.findall('^New Revision: ([0-9]*)', line)
    if len(rev) >= 1 :
        revs.append(rev)

int_revs = list()

# x in this case is the whole list (even though its only one index long). To get
# this code to work, I had to specifty which index I wanted to use the int() on.
for x in revs :
    int_revs.append(int(x[0]))

# I kept trying to use the "count" feature for lists. Turns out is "len"
print(int(sum(int_revs)/len(int_revs)))

