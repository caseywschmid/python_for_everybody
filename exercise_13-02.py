# Extracting Data from JSON

# In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/json2.py. The program will prompt for a URL, read the JSON data from that URL using urllib and then parse and extract the comment counts from the JSON data, compute the sum of the numbers in the file and enter the sum below:

# We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.

# Sample data: http://py4e-data.dr-chuck.net/comments_42.json (Sum=2553)
# Actual data: http://py4e-data.dr-chuck.net/comments_1642644.json (Sum ends with 58)
# You do not need to save these files to your folder since your program will read the data directly from the URL. Note: Each student will have a distinct data url for the assignment - so only use your own data url for analysis.

# Data Format
# The data consists of a number of names and comment counts in JSON as follows:

# {
#   comments: [
#     {
#       name: "Matthias"
#       count: 97
#     },
#     {
#       name: "Geomer"
#       count: 97
#     }
#     ...
#   ]
# }
# The closest sample code that shows how to parse JSON and extract a list is json2.py. You might also want to look at geoxml.py to see how to prompt for a URL and retrieve data from a URL.

# Sample Execution

# $ python3 solution.py
# Enter location: http://py4e-data.dr-chuck.net/comments_42.json
# Retrieving http://py4e-data.dr-chuck.net/comments_42.json
# Retrieved 2733 characters
# Count: 50
# Sum: 2...

import json
import urllib.request, urllib.parse, urllib.error
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Asks for user input for URL
url = input('Enter URL: ')
if len(url) < 1: 
    url = 'http://py4e-data.dr-chuck.net/comments_1642644.json'

print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read()
print('Retrieved', len(data), 'characters')

# This will get your requested information and store it in a dictionary or a list, depending on how the data is encoded. 
try :
    info = json.loads(data)
except : 
    info = None

# This will print the data in a readable format in the terminal:
# print(json.dumps(info, indent=4))

# This opens up the parent where the data you want is stored.
count = info['comments']

counts = list()
# Cycles through each list item and extracts the info and adds it to the list
for item in count:
    num = item['count']
    counts.append(num)

print('Count: ', len(counts))
print('Sum: ', sum(counts))
# *****************************TERMINAL RESULTS*******************************

# Enter URL: 
# Retrieving http://py4e-data.dr-chuck.net/comments_42.json
# Retrieved 2711 characters
# {
#     "note": "This file contains the sample data for testing",
#     "comments": [
#         {
#             "name": "Romina",
#             "count": 97
#         },
#         {
#             "name": "Laurie",
#             "count": 97
#         },
#         {
#             "name": "Bayli",
#             "count": 90
#         }
#     ]
# }
