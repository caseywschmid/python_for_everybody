# Exercise 3: Write a program that reads a file and prints the letters in
# decreasing order of frequency. Your program should convert all the input to
# lower case and only count the letters a-z. Your program should not count
# spaces, digits, punctuation, or anything other than the letters a-z. Find text
# samples from several different languages and see how letter frequency varies
# between languages. Compare your results with the tables at
# https://wikipedia.org/wiki/Letter_frequencies.

import string

filename = input('ENTER A FILE TO BE ANALYZED:')
if len(filename) < 1 :
    filename = 'mbox.txt'

try :
    filehandle = open(filename)
except :
    print('FILE CANNOT BE FOUND')
    quit()

letters = list()
for line in filehandle :
    line = line.strip()
    line = line.translate(line.maketrans(' ',' ', string.punctuation))
    line = line.translate(line.maketrans(' ',' ', string.digits))
    line = line.translate(line.maketrans(' ',' ', string.whitespace))
    line = line.lower()
    words = line.split()
    for word in words :
        for letter in word :
            letters.append(letter)

count = dict()
for letter in letters :
    count[letter] = count.get(letter, 0) +1

az = list()
for key, val in count.items():
    az.append((val, key))

az.sort(reverse = True)

for key, val in az :
    print(key,val)