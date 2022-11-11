# In computing, a regular expression, also called a "regex" or "regexp",
# provides a concise and flexible means for matching strings of text, such as
# particular characters, words, or patterns of characters. A regular expression
# is written in a formal language that can be interpreted by a regular
# expression processor.
# Really smart "Find" or "Search"

# Regular Expression Quick Guide

"^"         # Matches the beginning of a line
"$"         # Matches the end of the line
"."         # Matches any character (Wildcard)
"\s"        # Matches whitespace
"\S"        # Matches any non-whitespace character
"*"         # Repeats a character zero or more times 
"*?"        # Repeats a character zero or more times (non-greedy)
"+"         # Repeats a character one or more times
"+?"        # Repeats a character one or more times (non-greedy)
"[aeiou]"   # Matches a single character in the listed set
"[^XYZ]"    # Matches a single character not in the listed set
"[a-z0-9]"  # The set of characters can include a range
"("         # Indicates where a string extraction is to start
")"         # Indicates where a string extraction is to end

# To use this library, you've got to import it at the beginning with:

from http.client import ImproperConnectionState
import imp
import re

# Using re.search() like find()
# With strings
filehandle = open('mbox-short.txt')
for line in filehandle :
    line = line.rstrip()
    if line.find('From:') >= 0:
        print(line)

# With Regular Expressions
import re
filehandle = open('mbox-short.txt')
for line in filehandle:
    line = line.rstrip()
    if re.search('From:', line) : # re.search ('What to find', where to search)
        print(line)

# Using re.search() like startswith()
# With strings
filehandle = open('mbox-short.txt')
for line in filehandle :
    line = line.rstrip()
    if line.find('From:') >= 0:
        print(line)

# With Regular Expressions
import re
filehandle = open('mbox-short.txt')
for line in filehandle:
    line = line.rstrip()
    # The only difference is the carrot which denotes the beginning of the line. 
    # re.search ('What to find', where to search)
    if re.search('^From:', line) : 
        print(line)

# The dot character is a wildcard If you add the asterisk character, the
# preceding character becomes "any number of times" 

re.search('^X.*:') # This code would return all data in quotes.

"X-Sieve:" CMU Sieve 2.3
"X-DSPAM-Result:" Innocent
"X-DSPAM-Confidence:" 0.8475
"X-Content-Type-Message-Body:" text/plain
"X-Plane is behind schedule:" two weeks

# You could refine this code by being more specific with your search. Say you
# didn't want the last entry. Even though it meets your initial criteria, it's
# data you want to exlude from your search. Re-write your search like this:
 
re.search('^X-\S+:') 
# This code will return all but the last one. It basically says "Match the start
# of the line (^) for 'X-' followed by any non-whitespace character (\S) one or
# more times (+) followed by a ':'". Since the last line meets all the criteria
# except for the colon at the end, it is excluded from the search results. 

# The re.search() only returns whether or not the data exists (True or False).
# You can use re.findall() to actually extract the data and put it in a list.

import re
x = 'My 2 favorite numbers are 19 and 42'
# [0-9] is the allowed characters
# '+' means "any number of these characters"
y = re.findall('[0-9]+', x) 
print(y) # Prints ['2', '19', '42']

# Greedy matching means it will return the largest string that applies to the
# rules. To inhibit this behavior, simply add a ? to the end of the + or * to
# prefer the shorter strings.

# You can add a second set of parentesis inside the regular expression to be
# even more specific about what you want to extract. 

x = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
y = re.findall('\S+@\S+', x)
print(y) # Prints ['stephen.marquard@uct.ac.za']
z = re.findall('^From (\S+@\S+)', x)
print(z) # Prints ['stephen.marquard@uct.ac.za']

# How to parse strings with regex

import re
x = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
# @ is where to start
# ( ) means we only want that bit of info in the list
# [^ ] means match anything but what follows the carrot. 
# * means any number of non-blank characters afterwards
y = re.findall('@([^ ]*', x)
print(y) # Prints ['uct.ac.za']

# You can further refine this search

import re
x = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
# ^From_ is where to start
# .* means any number of characters
# @ means we'll see an @ at some point.  
# ( ) means we only want that bit of info in the list
# [^ ] means match anything but what follows the carrot. 
# * means any number of non-blank characters afterwards
y = re.findall('^From .*@([^ ]*', x)
print(y) # Prints ['uct.ac.za']

# To extract dollar amounts for example the code would look like this:
import re
x = 'We just received $10.00 for cookies.'
y = re. findall('\$[0-9.]+, x')
print(y) # Prints ['$10.00']


