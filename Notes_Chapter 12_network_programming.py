 # To be able to communicate with different sockets you'll have to put down some
 # boilerplate code

# import socket
# # think of this as a filehandle with no file attached yet...
# mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# mysocket.connect(('data.pr4e.org', 80))

# Once you have the socket setup, you'll have to establish what kind of data you
# expect to send and what kind of data you expect to get back. This
# determination is called the "Application Protocol". The dominant protocol is
# the HTTP. Hyper Text Transfer Protocol is the set of rules to allow browsers
# to retrieve web documents from servers over the internet. 

# Write a web browser in Python. This program did not work for me at first. After
# some research I found that \r\n was the correct way to denote a new line
# despite what was shown in the lesson video
import socket
mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysocket.connect(('data.pr4e.org', 80))
# .encode() converts between unicode and UTF-8
# \r\n for new line or it won't work
cmd = 'GET https://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysocket.send(cmd)

while True :
    data = mysocket.recv(512)
    if (len(data)) < 1 :
        break   
    # The end='' adds a string to the end of your print statement. In this case,
    # a space
    print(data.decode(), end='')
mysocket.close()

# write a web browswer with urllib
# This will pull the romeo.txt file from the url and count the word frequency

import urllib.request, urllib.parse, urllib.error

filehandle = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

counts = dict()
for line in filehandle :
    words = line.decode().split()
    for word in words :
        counts[words] = counts.get(words, 0) + 1
print(counts)


# Get an image file from the internet using a Python written browser.
# This is just copied out of the book. The program seems to run fine but the
# image I get back is broken. 

import socket

HOST = 'data.pr4e.org'
PORT = 80
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((HOST, PORT))
mysock.sendall(b'GET http://data.pr4e.org/cover3.jpg HTTP/1.0\r\n\r\n')
count = 0
picture = b''

while True :
    data = mysock.recv(5120)
    if len(data) < 1 : break
    count += len(data)
    print(len(data), count)
    picture += data

mysock.close()

pos = picture.find(b"\r\n\r\n")
print('Header Length', pos)
print(picture[:pos].decode())

pos = picture[pos+4:]
filehandle = open('stuff.jpg', 'wb')
filehandle.write(picture)
filehandle.close()


# To copy a file from the intenet onto your computer do this: 
# This will work as long as the file is less than the memory of your computer. 


import urllib.request, urllib.parse, urllib.error
img = urllib.request.urlopen('http://data.pr4e.org/cover3.jpg').read() 
# Writing a file name that doesn't exist will create a new file with that name.
# The 'wb' stands for opening a binary file for write only. Once it has all the
# data, it'll copy it into the location where you want it all at once. 
fhand = open('cover3.jpg', 'wb') 
fhand.write(img) 
fhand.close()

# You can edit this to only get the data in chuncks. See below. That way, you
# can download a file of any size without it messing up.

import urllib.request, urllib.parse, urllib.error
img = urllib.request.urlopen('http://data.pr4e.org/cover3.jpg').read() 
fhand = open('cover3.jpg', 'wb') 
size = 0
while True : 
    info = img.read(100000)
    if len(info) < 1 : break
    size += len(info)
    fhand.write(info) 
print(size, 'characters copied.')
fhand.close()