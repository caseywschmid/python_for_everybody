# Exercise 1: Write a simple program to simulate the operation of the grep
# command on Unix. Ask the user to enter a regular expression and count the
# number of lines that matched the regular expression: 
# 
# $ python grep.py 
# Enter a regular expression: ^Author 
# mbox.txt had 1798 lines that matched ^Author $
# 
# python grep.py 
# Enter a regular expression: ^X- 
# mbox.txt had 14368 lines that matched ^X- 
# 
# $ python grep.py 
# Enter a regular expression: java$ 
# mbox.txt had
# 4175 lines that matched java$

import re

name = input('Enter a file name:')
if len(name) < 1 :
    name = 'mbox.txt'

exp = input('Enter a regular expression:')

try :
    handle = open(name)
except :
    print('FILE NOT FOUND')
    quit()

count = None
for line in handle :
    line = line.rstrip()
    if re.search(exp, line):
        if count is None :
            count = 1
        else :
            count += 1

print(name, 'had', count, 'lines that matched', exp)