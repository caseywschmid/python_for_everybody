import re
filename = input('Enter a file: ')
if len(filename) < 1 :
    filename = "regexp.txt"
filehandle = open(filename)
total = None
for line in filehandle:
    integers = re.findall('[0-9]+', line)
    for num in integers :
        num = int(num)
        if total is None :
            total = num
        else :
            total = total + num
print(total)        
