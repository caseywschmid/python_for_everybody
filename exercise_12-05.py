# Exercise 5: (Advanced) Change the socket program so that it only shows data
# after the headers and a blank line have been received. Remember that recv
# receives characters (newlines and all), not lines.

import socket
import re

myurl = input('Enter a url:')
if len(myurl) < 1 :
    myurl = 'http://data.pr4e.org/romeo.txt'
connectlist = myurl.split('/')
myconnect = connectlist[2]

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# The connect call has to be changed as well
try :
    mysock.connect((myconnect, 80))
except :
    print('WEBSITE NOT FOUND')
    quit()

mysock.send(('GET ' + myurl + ' HTTP/1.0\r\n\r\n').encode())

while True:
    data = mysock.recv(1000)
    if len(data) < 1:
        break
    # repr prints all whitespace characters as well, e.g. \r\n
    data = data.decode()
    # print(data)
    # print(repr(data))
    content = re.findall('.+\r\n\r\n(.+)\n', data)
    # print(data.decode(),end='')
    print(content)

mysock.close()
