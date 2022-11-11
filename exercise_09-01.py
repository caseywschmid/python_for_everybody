# Exercise 1: Download a copy of the file www.py4e.com/code3/words.txt Write a
# program that reads the words in words.txt and stores them as keys in a
# dictionary. It doesn’t matter what the values are. Then you can use the in
# operator as a fast way to check whether a string is in the dictionary.


name = input("Enter file:")
if len(name) < 1:
    name = "words.txt"

handle = open(name)
uniquewords = dict()
for line in handle : 
    line = line.rstrip()
    words = line.split()
    for word in words :
        if word not in uniquewords :
            uniquewords[word] = 1
# print(uniquewords)

while True :
    find = input("Enter the word you want to find. \nEnter \"Done!\" when finished:")
    if find == 'Done!' :
        quit()
    if find in uniquewords :
        print(find, 'is in', name)
    else :
        print(find, 'is not in', name)
        

