import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL Certificate Errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

webpage = input('Enter a url:')
# When you add the .read() to the end, it will add the entire webpage in a
# single string and return it with new lines at the end of each line.
html = urllib.request.urlopen(webpage, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags :
    print(tag.get('href', None))



