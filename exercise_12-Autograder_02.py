# # Exercise 4: Change the urllinks.py program to extract and count paragraph
# # (p) tags from the retrieved HTML document and display the count of the
# # paragraphs as the output of your program. Do not display the paragraph text,
# # only count them. Test your program on several small web pages as well as some
# # larger web pages.

# import urllib.request, urllib.parse, urllib.error
# from bs4 import BeautifulSoup
# import ssl
# import re

# # Ignore SSL certificate errors
# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE

# # Get URL from User
# url = input('Enter - ')
# if len(url) < 1 :
#     url = 'http://py4e-data.dr-chuck.net/comments_1642641.html'
# html = urllib.request.urlopen(url, context=ctx).read()
# soup = BeautifulSoup(html, 'html.parser')

# # Retrieve all of the span tags
# tags = soup('span')

# spans = list()
# # Converted list of BS4 Tags to list of strings
# for tag in tags :
#     spans.append(str(tag))

# digits = list()
# # Used Regular Expressions to pull the numbers
# for span in spans :
#     nums = re.findall('[0-9]+', span)
#     # Pulled number from single index RegEx list
#     for num in nums :
#         # Converted string to int
#         digits.append(int(num))

# # Used sum() to add the numbers
# print(sum(digits))



# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
if len(url) < 1 :
    url = 'http://py4e-data.dr-chuck.net/comments_1642641.html'
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup('span')
for tag in tags:
    # Look at the parts of a tag
    print('TAG:', tag)
    print('URL:', tag.get('href', None))
    # ****** Could have used this on your course ******
    print('Contents:', tag.contents[0])
    print('Attrs:', tag.attrs)