# Exercise 1: Write a program to read through a file and print the contents of
# the file (line by line) all in upper case.
filename = input("Enter file name: ")
if len(filename) < 1 :
    filename = 'mbox-short.txt'
filehandle = open(filename)
for line in filehandle:
    line = line.rstrip()
    print(line.upper())


    