import urllib.request, urllib.parse, urllib.error
import http
import sqlite3
import json
import time
import ssl
import sys

api_key = 'AIzaSyDaqRnNevpKAd0iTkxsn_oMBcBd-Yt9bhU'
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'

if api_key is False:
    api_key = 42
    serviceurl = "http://py4e-data.dr-chuck.net/json?"
else :
    serviceurl = "https://maps.googleapis.com/maps/api/geocode/json?"

# Additional detail for urllib
# http.client.HTTPConnection.debuglevel = 1

conn = sqlite3.connect('geodata.sqlite')
cur = conn.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS Locations (address TEXT, geodata TEXT)''')

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

fh = open("where.data")
count = 0
for line in fh:
    if count > 200 :
        print('Retrieved 200 locations, restart to retrieve more')
        break

    address = line.strip()
    # print('')
    cur.execute("SELECT geodata FROM Locations WHERE address= ?",
        (memoryview(address.encode()), ))

    # This checks to see if the address it is currently looking at is already in
    # the database.
    try:
        data = cur.fetchone()[0]
        print("Found in database ",address)
        continue
    except:
        pass
    # Creates a dictionary with two key-value pairs. One key labled "address"
    # and another labeled "key". It then then takes those two items and puts
    # them into the url to be used for data extraction
    parms = dict()
    parms["address"] = address
    
    if api_key is not False: 
        parms['key'] = api_key
    
    print(parms)
    url = serviceurl + urllib.parse.urlencode(parms)
    print(url)
    print('Retrieving', url)

    # urllib.request.urlopen(url, [timeout, ]*, context=None)
    # Open the URL url, which can be either a string or a Request object.

    # The optional timeout parameter specifies a timeout in seconds for blocking
    # operations like the connection attempt (if not specified, the global default
    # timeout setting will be used). This actually only works for HTTP, HTTPS and
    # FTP connections.

    # If context is specified, it must be a ssl.SSLContext instance describing
    # the various SSL options. See
    # https://docs.python.org/3/library/http.client.html#http.client.HTTPSConnection
    # for more details.

    # This function always returns an object which can work as a context manager
    # and has the properties url, headers, and status. See
    # https://docs.python.org/3/library/urllib.request.html#urllib.response.addinfourl
    # for more detail on these properties.
    # Type: <class 'http.client.HTTPResponse'>
    uh = urllib.request.urlopen(url, context=ctx)

    data = uh.read().decode()

    print('Retrieved', len(data), 'characters', data[:20].replace('\n', ' '))
    count = count + 1

    try:
        js = json.loads(data)
    except:
        print(data)  # We print in case unicode causes an error
        continue

    if 'status' not in js or (js['status'] != 'OK' and js['status'] != 'ZERO_RESULTS') :
        print('==== Failure To Retrieve ====')
        print(data)
        break

    cur.execute('''INSERT INTO Locations (address, geodata)
            VALUES ( ?, ? )''', (memoryview(address.encode()), memoryview(data.encode()) ) )
    conn.commit()
    if count % 10 == 0 :
        print('Pausing for a bit...')
        time.sleep(5)
print("Run geodump.py to read the data from the database so you can vizualize it on a map.")
