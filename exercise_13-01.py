# In this assignment you will write a Python program somewhat similar to
# http://www.py4e.com/code3/geoxml.py. The program will prompt for a URL, read
# the XML data from that URL using urllib and then parse and extract the comment
# counts from the XML data, compute the sum of the numbers in the file.

# We provide two files for this assignment. One is a sample file where we give
# you the sum for your testing and the other is the actual data you need to
# process for the assignment.

# Sample data: http://py4e-data.dr-chuck.net/comments_42.xml (Sum=2553) Actual
# data: http://py4e-data.dr-chuck.net/comments_1642643.xml (Sum ends with 27)
# You do not need to save these files to your folder since your program will
# read the data directly from the URL. Note: Each student will have a distinct
# data url for the assignment - so only use your own data url for analysis.

# You are to look through all the <comment> tags and find the <count> values sum
# the numbers. The closest sample code that shows how to parse XML is geoxml.py.
# But since the nesting of the elements in our data is different than the data
# we are parsing in that sample code you will have to make real changes to the
# code. To make the code a little simpler, you can use an XPath selector string
# to look through the entire tree of XML for any tag named 'count' with the
# following line of code:

# counts = tree.findall('.//count')

# Take a look at the Python ElementTree documentation and look for the supported
# XPath syntax for details. You could also work from the top of the XML down to
# the comments node and then loop through the child nodes of the comments node.
# Sample Execution

# $ python3 solution.py
# Enter location: http://py4e-data.dr-chuck.net/comments_42.xml
# Retrieving http://py4e-data.dr-chuck.net/comments_42.xml
# Retrieved 4189 characters
# Count: 50
# Sum: 2...

import urllib.request, urllib.parse, urllib.error
from xml.dom import xmlbuilder
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Asks for user input for URL
url = input('Enter URL: ')
if len(url) < 1: 
    url = 'http://py4e-data.dr-chuck.net/comments_1642643.xml'

print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read()
print('Retrieved', len(data), 'characters')
# print(data.decode())

# This provides you with the plug you need to start drilling down into the xml.
# Its the outermost tag in the xml. In this case its the <commentinfo> tag. 
commentinfo = ET.fromstring(data)

# This gets you into the parent tag where your info is 
# In this case its the <comments> tag followed by the <comment> tag
# This provides you a Python list of TAGS
commentlist = commentinfo.findall('comments/comment')
print('Count:', len(commentlist))

# Here is where you loop through your data to extract exactly what you're looking for. 
# In this case, its the comment count number text. 
counts = list()
for item in commentlist :
    counts.append(int(item.find('count').text))

print('Sum:', sum(counts))

# *****************************TERMINAL RESULTS*******************************

# Retrieving http://py4e-data.dr-chuck.net/comments_42.xml
# Retrieved 4189 characters
# <?xml version="1.0" encoding="UTF-8"?>
# <commentinfo>
#   <note>This file contains the sample data for testing</note>

#   <comments>
#     <comment>
#        <name>Romina</name>
#        <count>97</count>
#     </comment>
#     <comment>
#        <name>Laurie</name>
#        <count>97</count>
#     </comment>
#     <comment>
#        <name>Bayli</name>
#        <count>90</count>
#     </comment>
#   </comments>
# </commentinfo>