# Exercise 1: Revise a previous program as follows: Read and parse the “From”
# lines and pull out the addresses from the line. Count the number of messages
# from each person using a dictionary. After all the data has been read, print
# the person with the most commits by creating a list of (count, email) tuples
# from the dictionary. Then sort the list in reverse order and print out the
# person who has the most commits. 
# 
# Sample Line: 
# From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008 
# 
# Enter a file name: mbox-short.txt 
# cwen@iupui.edu 5
# 
# Enter a file name: mbox.txt 
# zqian@umich.edu 195


filename = input("Enter file:")
if len(filename) < 1:
    name = "mbox-short.txt"
filehandle = open(name)

addresses = list()
for line in filehandle :
    if not line.startswith('From ') :
        continue
    line = line.rstrip()
    words = line.split()
    addresses.append(words[1])

count = dict()
for name in addresses :
    count[name] = count.get(name, 0) + 1

emailcounts = list()
for email, freq in count.items():
    # DONT FORGET THE SECOND SET OF PARENTHISES!!
    # ALSO THAT HOW YOU ARRANGE THE TUPLE MATTERS
    emailcounts.append((freq, email))

# Sorts from lowest to highest count by default. Don't forget to reverse it!
emailcounts.sort(reverse = True)
# To get the list to print out as text, use a for loop...
for key, val in emailcounts[:1]:
    print(val, key)