# This is just copied out of the book. The program seems to run fine but the
# image I get back is broken. 



# import socket

# HOST = 'data.pr4e.org'
# PORT = 80
# mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# mysock.connect((HOST, PORT))
# mysock.sendall(b'GET http://data.pr4e.org/cover3.jpg HTTP/1.0\r\n\r\n')
# count = 0
# picture = b''

# while True :
#     data = mysock.recv(5120)
#     if len(data) < 1 : break
#     count += len(data)
#     print(len(data), count)
#     picture += data

# mysock.close()

# pos = picture.find(b"\r\n\r\n")
# print('Header Length', pos)
# print(picture[:pos].decode())

# pos = picture[pos+4:]
# filehandle = open('stuff.jpg', 'wb')
# filehandle.write(picture)
# filehandle.close()

# This code worked for getting the image to appear. 
import urllib.request, urllib.parse, urllib.error
img = urllib.request.urlopen('http://data.pr4e.org/cover3.jpg') 
# The .jpg title is whatever you want the image to be called
fhand = open('cover_bob.jpg', 'wb') 
size = 0
while True : 
    info = img.read(100000)
    if len(info) < 1 : break
    size += len(info)
    fhand.write(info) 
print(size, 'characters copied.')
fhand.close()