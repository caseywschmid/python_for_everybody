# Exercise 2: Change your socket program so that it counts the number of
# characters it has received and stops displaying any text after it has shown
# 3000 characters. The program should retrieve the entire document and count
# the total number of characters and display the count of the number of
# characters at the end of the document.

import socket

myurl = input('Enter a url:')
if len(myurl) < 1 :
    myurl = 'http://data.pr4e.org/mbox-short.txt'
connectlist = myurl.split('/')
myconnect = connectlist[2]
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try :
    mysock.connect((myconnect, 80))
except :
    print('WEBSITE NOT FOUND')
    quit()

cmd_str = 'GET ' + myurl + ' HTTP/1.0\r\n\r\n'
cmd = cmd_str.encode()
mysock.send(cmd)

chars = list()
count = None
while True:
    # I had recv(512) and it was giving me this in the terminal:
    # 
    # 'HTTP/1.1 200 OK\r\nDate: Wed, 14 ... envious moon\nWho is already s' 
    # 'ick and pale with grief\n' 
    # 
    # I have not idea why. I changed recv(512) to
    # recv(5120) and it seems to have fixed the problem
    data = mysock.recv(5120)
    if len(data) < 1:
        break
    data = data.decode()
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
mysock.close()
