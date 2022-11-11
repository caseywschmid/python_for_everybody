# Exercise 3: Use urllib to replicate the previous exercise of (1) retrieving
# the document from a URL, (2) displaying up to 3000 characters, and (3)
# counting the overall number of characters in the document. Don’t worry about
# the headers for this exercise, simply show the first 3000 characters of the
# document contents.

import urllib.request, urllib.parse, urllib.error

myurl = input('Enter a url:')
if len(myurl) < 1 :
    myurl = 'http://data.pr4e.org/romeo-full.txt'

try: 
    filehandle = urllib.request.urlopen(myurl)
except : 
    print('WEBSITE NOT FOUND')
    quit()

#   ******THIS IS IMPORTANT******

# This line allows you to access the data for analysis  
data = filehandle.read().decode()

#   ******THIS IS IMPORTANT******


chars = list()
count = None

for char in data :
    if count is None :
        count = 1
        chars.append(char)
    else : 
        count += 1
        chars.append(char)



# Create display text that contains only the first 3000 characters
display = ''
for char in chars[:3000] :
    display += char

print(display)
print(count)