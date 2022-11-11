# Lists seem to be what Python calls an array. Its a variable that contains a
# collection of things. 

friends = ['Joseph', 'Glenn', 'Sally']

# A list element can be any Python object, even another list. A list can also be
# empty

stuff = [1, 98.6, 'red', [1, 2, 3]]

# Each list item has its corresponding position that can be called to pull out a
# specific piece of data from the list. 

friends = ['Joseph', 'Glenn', 'Sally']
print(friends[2])

# You can change the items in a list if you want. 

friends = ['Joseph', 'Glenn', 'Sally']
friends[1] = 'Bob'
print(friends) # This print out "['Joseph', 'Bob', 'Sally']""

# You can look up how long a list is by useing the len() funtion. 

friends = ['Joseph', 'Glenn', 'Sally']
print(len(friends)) # This prints out "3"

# The range() function returns a list of numbers from 0 to n-1

print(range(4)) # Prints "[0, 1, 2, 3]"

# This is useful because it allows you to create an index list for another list
# which can be used to construct for loops to iterate through a list

friends = ['Joseph', 'Glenn', 'Sally']
print(len(friends)) # Prints out "3"
print(range(len(friends))) # Prints out "[0, 1, 2]"

# Here is one way to iterate through a list using the method above

friends = ['Joseph', 'Glenn', 'Sally']
for i in range(len(friends)):
    friend = friends[i]
    print('Happy New Year:', friend)

# Here is another way to do the same thing that is prettier. 

friends = ['Joseph', 'Glenn', 'Sally']
for friend in friends:
    print('Happy New Year:', friend)

# You can concatenate two lists together using "+"

a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c) # Prints "[1, 2, 3, 4, 5, 6]" 

# You can also slice lists in the same way you can slice strings. 

t = [9, 41, 12, 3, 74, 15]
t[1:3] # Remember the second number is up to but not including
print(t[1,3]) # Prints "[41, 12]"
print(t[:4]) # Prints "[9, 41, 12, 3]"
print(t[3:]) # Prints "[3, 74, 15]"

# To create a list out of nothing use the list() Class

stuff = list()

# To add things to your list, call the .append() Method.

stuff.append('book')

# You can quickly check to see if something is in your list by using the "in"
# operator

some = [1, 9, 21, 10, 16]
9 in some # Returns True
15 in some # Returns False

# You can also check to see if something is not in your list by using the "not
# in" operator

some = [1, 9, 21, 10, 16]
10 not in some # Returns False
3 not in some # Returns True

# Lists are in order and therefore you can change the order i.e. sort

friends = ['Joseph', 'Glenn', 'Sally']
friends.sort() # This will put the list in alphebetical order
print(friends) # Prints ['Glenn', 'Joseph', 'Sally']

# Lists have built in functions 

nums = [3, 41, 12, 9, 74, 15]
print(len(nums)) # Prints "6"
print(max(nums)) # Prints "74"
print(min(nums)) # Prints "3"
print(sum(nums)) # Prints "154"
print(sum(nums)/len(nums)) # Prints "25.6". Finds the average

# You can use lists with strings. If you provide Python with a text line, you
# can take that line and split it into a list with each word taking up one
# postition on the list. This allows you to access a particualar word or loop
# through all the words. split() defaults to spaces. You can choose what
# character you want to split on (delimiter) by passing in a string argument.

abc = 'With three words'
stuff = abc.split()
print(stuff) # Prints "['With', 'three', 'words']". 
print(len(stuff)) # Prints "3". Could be a good way to count the words in a file

# You can do a double split. First you split on spaces and isolate the string
# you want. Then you split it again based on another delimeter. This can be used
# for example to parse out all the email addresses in a huge body of texts. 