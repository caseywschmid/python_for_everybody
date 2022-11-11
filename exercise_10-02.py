# 10.2 Write a program to read through the mbox-short.txt and figure out the
# distribution by hour of the day for each of the messages. You can pull the
# hour out from the 'From ' line by finding the time and then splitting the
# string a second time using a colon. 
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008 
# Once you have accumulated the counts for each hour, print out
# the counts, sorted by hour as shown below.

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
filehandle = open(name)
counts = dict()
times = list()
for line in filehandle :
    line = line.rstrip()
    if line.startswith('From '):
        words = line.split()
        time = words[5].split(':')
        times.append(time[0])
for num in times:
    counts[num] = counts.get(num, 0) +1
# When you need to iterate through a dictionary, you've got to use the key-value
# pairs along with .items() or it won't work.
for k,v in sorted(counts.items()):
    print(k,v)