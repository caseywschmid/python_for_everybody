# Exercise 2: Write a program that categorizes each mail message by which day of
# the week the commit was done. To do this look for lines that start with
# “From”, then look for the third word and keep a running count of each of the
# days of the week. At the end of the program print out the contents of your
# dictionary (order does not matter). 
# 
# Sample Line: 
# From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008
# 
# Sample Execution: 
# python dow.py 
# Enter a file name: mbox-short.txt 
# {'Fri': 20, 'Thu': 6, 'Sat': 1}

filename = input('Enter a file name: ')
if len(filename) < 1 :
    filename = 'mbox.txt'

try :
    filehandle = open(filename)
except :
    print('File not found')
    quit()

days = list()
counter = dict()
for line in filehandle :
    line = line.rstrip()
    if not line.startswith('From ') :
        continue
    words = line.split()
    days.append(words[2])
for day in days :
    counter[day] = counter.get(day, 0) + 1
print(counter)

# I'm figuring out that one way to create a "counter dictionary" is to first
# create a list of the words you want to count. Then iterate through that list
# and add each entry to a dictionary with the counts as the values and the words
# as the key.