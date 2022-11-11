# Python dictionaries are similar to lists in that they can store multiple
# values in a single variable. However, they are different in that there is no
# real order to the data stored in a dictionary and the data is accessed with
# the use of a key (or label) instead of its order in the list. You could think
# of a list as a Pringles can with all the chips stacked up neatly in order and
# a dictionary is a bag of Doritos with all the chips in the bag but in no
# particular order. This is Pythons most powerful data collection. Other
# languages have these and they go by different names: Property Bags, Hashmaps,
# Associative Arrays (for PHP and Perl), etc.

# To create a dictionary use the dict() Object. You can also use {}.

purse = dict()
bag = {}

# You can then put things into the dictonary by assigning each piece of data with a label. 

purse['money'] = 12
purse['candy'] = 3
purse['tissues'] = 75

# If you print the dictionary, you'll get all three items in no particular
# order. However, each piece of data will be attached to its key.

print(purse) # Prints "{'money': 12, 'tissues': 75, 'candy': 3}"

# You can ask Python to return a single piece of data from the dictionary

print(purse['candy']) # Prints "3"

# You can over write any piece of data in a dictionary. It will always use the
# most recent assignment for each key

purse['money'] = 12
purse['candy'] = 3
purse['tissues'] = 75
purse['money'] = 98
print(purse) # Prints "{'money': 98, 'tissues': 75, 'candy': 3}"

# Dictionaries are really great for counting things. They can be used to make
# histograms to display how frequently a particular piece of data shows up. 

# Create a dictionary that will count things for you. When you encounter a new
# thing, you'll have to add a new entry into the dictionary. If it is the second
# or time you're seeing the thing, add one to the count in the dictionary under
# that thing.

counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names :
    if name not in counts : 
        counts[name] = 1
    else :
        counts[name] = counts[name] + 1
print(counts)

# There is a handy method for dictionaries: .get(). To see if a key is already
# part of a dictionary (and assuming a default value if the key is not in the
# dictionary) you could write the code like this:

if name in counts :
    x = counts[name]
else : 
    x = 0 

# You can do the same exact thing with the .get() method and its a lot cleaner:

x = counts.get("key","default")
x = counts.get(name, 0) 

# This makes the code above a lot simpler (memorize this!!!): 

# This is the dictionary where the counting takes place
counts = dict()
# Here is the data to be analyzed 
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen'] 
for name in names :
    # This says that if the name is new, set it to 1. 
    counts[name] = counts.get(name, 0) + 1 #
print(counts)

# Count words in provided text

# Creates an empty dictionary
counts = {}
# Prompts user for input text
print('Enter a line of text: ')
# Sets variable to input line of text
line = input('')
# Sets variable to list of words in provided text
words = line.split()
# Prints the list
print('Words: ', words)
print('Counting...')
# For every word in the list
for word in words :
    # Count the number of times each word shows up
    counts[word] = counts.get(word, 0) + 1
# Print the results
print('Counts: ', counts)

# If you have an established dictionary it is easy to run a definite loop on every entry

counts = {'chuck', 3, 'fred', 42, 'jan', 100}
for key in counts : 
    print(key, counts[key])

# There are a few things you can specifically print out regarding dictionaries

jjj = {'chuck', 3, 'fred', 42, 'jan', 100}
print(list(jjj)) # Prints ['jan', 'chuck', 'fred'] in no particular order.
print(jjj.keys()) # Prints ['jan', 'chuck', 'fred'] in no particular order.
print(jjj.values()) # Prints [100, 3, 42] in no particular order. 
# If you ask for the keys and values together they will print out in a corresponding order
print(jjj.items()) # Prints {('jan', 100), ('chuck', 3), ('fred', 42)}

# You can loop through key-value pairs in a dictionary using two iteration variables (Python Only)

jjj = {'chuck', 3, 'fred', 42, 'jan', 100}
for aaa,bbb in jjj.items() :
    print(aaa,bbb) # Prints individual key-value pairs



# Asks user for file name 
name = input('Enter file: ')
# Assigns handle to file
handle = open(name)

# Creates new dictionary
counts = dict()
# for every line in the file
for line in handle : 
    # Create a list of whitespace separated words
    words = line.split()
    # for each word in the list
    for word in words : 
        # Counts the number of words, adding new entries for unique words
        counts[word] = counts.get(word, 0) + 1

# Initializes two varables
bigcount = None
bigword = None
# For each word-count key-value pair
for word,count in counts.items() :
    # Keeps track of the highest number and what word it belongs to
    if bigcount is None or count > bigcount :
        bigword = word
        bigcount = count

# Prints out the word that appeared the most and how many times it appeared. 
print(bigword, bigcount)


# You can sort dictionaries by value instead of key. This code prints out the 10
# most common words in a text file

fhand = open(romeo.txt)
counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

lst = list()
for key, val in counts.items():
    newtup = (val, key)
    lst.append(newtup)

lst = sorted(lst, reverse=True)

for val, key in lst[:10]:
    print(key, val)

# This can be written in a much more succint way. 

print(sorted([(val,key) for key,val in counts.items()]))
# Prints [(1, 'b'), (10, 'a'), (22, 'c')]