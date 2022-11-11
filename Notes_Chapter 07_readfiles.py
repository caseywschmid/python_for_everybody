# To be able to read a file in Python, you'll have to be able to communicate
# with it. You start by creating a variable for the file using the open()
# function. This will create a 'file handle' that you will use to interact with
# the file of your choice. 

xfile = open('mbox.txt') # - This creates the file handle
for line in xfile: 
  print(line)

# This code essentially says "for every line in the document, print the line"
# 
# You can "read" the whole file into a single string. Use the .read() to
# set the contents of the file to a variable

xfile = open('mbox.txt')
input = 'mbox.txt'.read() # - This gives you a giant string variable

# You can search for lines of text that start with specific things

filehandle = open('mbox.txt')
for line in filehandle:
    if line.startswith('From'):
        print(line)

# You have to be careful with this because the line in print(line) is going to
# have a new line at the end (/n). ALSO, between each print statement, Python
# adds another new line; so you end up with two. To fix that, you need to use
# the string function strip(). We can strip whitespace from the right hand side
# of the string by using rstrip() from the string library. 

filehandle = open('mbox.txt')
for line in filehandle:
    line = line.rstrip()
    if line.startswith('From'):
        print(line)

# Another way to structure these loops is to skip the 'bad' lines instead of
# look for the 'good' ones. 

filehandle = open('mbox.txt')
for line in filehandle:
    line = line.rstrip()
    if not line.startswith('From'):
        continue # this just skips over the 'bad' lines
    print(line)

# A way to look for any string anywhere within a line is to use the 'in' operator. 

filehandle = open('mbox.txt')
for line in filehandle:
    line = line.rstrip()
    if not '@uct.ac.za' in line :
        continue    
    print(line)

# To get your program to prompt you for the file name, instead of making the
# file a constant in the program, create a variable that will take the user
# input and use that as the file name

filename = input('Enter the file name: ')
filehandle = open(filename)
for line in filehandle:
    line = line.rstrip()
    if line.startswith('From'):
        print(line)

# You can deal with bad user input by tweaking the code to attempt to open the
# file and if it doesn't work, to throw and error message and quit the program. 

filename = input('Enter the file name: ')
try:
    filehandle = open(filename)
except:
    print('File cannot be opened:', filename)
    quit() 
    # the QUIT here is important because if you don't quit, filehandle is not
    # properly defined and you'll get a traceback
for line in filehandle:
    line = line.rstrip()
    if line.startswith('From'):
        print(line)
