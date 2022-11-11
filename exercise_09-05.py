# Exercise 5: This program records the domain name (instead of the address)
# where the message was sent from instead of who the mail came from (i.e., the
# whole email address). At the end of the program, print out the contents of
# your dictionary. 

# python schoolcount.py 
# Enter a file name: mbox-short.txt
# {'media.berkeley.edu': 4, 'uct.ac.za': 6, 'umich.edu': 7, 'gmail.com': 1,
# 'caret.cam.ac.uk': 1, 'iupui.edu': 8}


from re import L


name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"

try :
    handle = open(name)
except :
    print('FILE NOT FOUND')
    quit()

domains = list()
for line in handle : 
    line = line.rstrip()
    if line.startswith('From '):
        words = line.split()
        domain = words[1].split('@')
        domains.append(domain[1])

counts = dict()
for domain in domains :
    counts[domain] = counts.get(domain, 0) + 1

print(counts)