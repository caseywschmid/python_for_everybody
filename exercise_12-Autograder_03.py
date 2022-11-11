import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter a URL - ')
if len(url) < 1 :
    url = 'http://py4e-data.dr-chuck.net/known_by_Amaarah.html'
c = input('Enter count:')
p = input('Enter position:')

# Convert string input to int
count = int(c)
pos = int(p)

#  Open and read URL
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Function creates list of links from provided url, finds desired link from list
# (position), and follows it the desired number of times (count). 
def followlinks(url, position, count) :
    while count >= 0:
        print('Retrieving:', url)
        # Open and read URL
        html = urllib.request.urlopen(url, context=ctx).read()
        soup = BeautifulSoup(html, 'html.parser')
        # Retrieve all of the anchor tags
        tags = soup('a')
        # Add tags to a list
        lst = list()
        for tag in tags :
            lst.append(tag.get('href', None))
        url = lst[int(position) - 1]
        count -= 1

print(followlinks(url,pos,count))