# Calling a JSON API

# In this assignment you will write a Python program somewhat similar to
# http://www.py4e.com/code3/geojson.py. The program will prompt for a location,
# contact a web service and retrieve JSON for the web service and parse that
# data, and retrieve the first place_id from the JSON. A place ID is a textual
# identifier that uniquely identifies a place as within Google Maps.

# API End Points 
# To complete this assignment, you should use this API endpoint
# that has a static subset of the Google Data:

# http://py4e-data.dr-chuck.net/json?

# This API uses the same parameter (address) as the Google API. This API also
# has no rate limit so you can test as often as you like. If you visit the URL
# with no parameters, you get "No address..." response. To call the API, you
# need to include a key= parameter and provide the address that you are
# requesting as the address= parameter that is properly URL encoded using the
# urllib.parse.urlencode() function as shown in
# http://www.py4e.com/code3/geojson.py

# Make sure to check that your code is using the API endpoint as shown above.
# You will get different results from the geojson and json endpoints so make
# sure you are using the same end point as this autograder is using.

# Test Data / Sample Execution
# You can test to see if your program is working with a location of "South
# Federal University" which will have a place_id of
# "ChIJNeHD4p-540AR2Q0_ZjwmKJ8".

# $ python3 solution.py
# Enter location: South Federal University
# Retrieving http://...
# Retrieved 2445 characters
# Place id ChIJNeHD4p-540AR2Q0_ZjwmKJ8

import urllib.request, urllib.parse, urllib.error
import json
import ssl

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

address = input('Enter location: ')
if len(address) < 1:
    address = 'Kazan Federal University'

parms = dict()
parms['address'] = address

if api_key is not False: 
    parms['key'] = api_key

url = serviceurl + urllib.parse.urlencode(parms)
print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')

try:
    js = json.loads(data)
except:
    js = None

if not js or 'status' not in js or js['status'] != 'OK':
    print('==== Failure To Retrieve ====')
    print(data)
    quit()

# print(json.dumps(js, indent=4))

placeID = js['results'][0]['place_id']
print('Place id', placeID)


# *****************************TERMINAL RESULTS*******************************

# Enter location: 
# Retrieving http://py4e-data.dr-chuck.net/json?address=South+Federal+University&key=42
# Retrieved 2443 characters
# {
#     "results": [
#         {
#             "address_components": [
#                 {
#                     "long_name": "105/42",
#                     "short_name": "105/42",
#                     "types": [
#                         "street_number"
#                     ]
#                 },
#                 {
#                     "long_name": "Bol'shaya Sadovaya Ulitsa",
#                     "short_name": "Bol'shaya Sadovaya Ulitsa",
#                     "types": [
#                         "route"
#                     ]
#                 },
#                 {
#                     "long_name": "Rostov",
#                     "short_name": "Rostov",
#                     "types": [
#                         "locality",
#                         "political"
#                     ]
#                 },
#                 {
#                     "long_name": "Kirovskiy",
#                     "short_name": "Kirovskiy",
#                     "types": [
#                         "administrative_area_level_3",
#                         "political"
#                     ]
#                 },
#                 {
#                     "long_name": "Gorod Rostov-On-Don",
#                     "short_name": "Gorod Rostov-On-Don",
#                     "types": [
#                         "administrative_area_level_2",
#                         "political"
#                     ]
#                 },
#                 {
#                     "long_name": "Rostovskaya oblast'",
#                     "short_name": "Rostovskaya oblast'",
#                     "types": [
#                         "administrative_area_level_1",
#                         "political"
#                     ]
#                 },
#                 {
#                     "long_name": "Russia",
#                     "short_name": "RU",
#                     "types": [
#                         "country",
#                         "political"
#                     ]
#                 },
#                 {
#                     "long_name": "344006",
#                     "short_name": "344006",
#                     "types": [
#                         "postal_code"
#                     ]
#                 }
#             ],
#             "formatted_address": "\u0443\u043b, Bol'shaya Sadovaya Ulitsa, 105/42, Rostov, Rostovskaya oblast', Russia, 344006",
#             "geometry": {
#                 "location": {
#                     "lat": 47.224719,
#                     "lng": 39.7283339
#                 },
#                 "location_type": "ROOFTOP",
#                 "viewport": {
#                     "northeast": {
#                         "lat": 47.2259369802915,
#                         "lng": 39.72971083029149
#                     },
#                     "southwest": {
#                         "lat": 47.2232390197085,
#                         "lng": 39.7270128697085
#                     }
#                 }
#             },
#             "partial_match": true,
#             "place_id": "ChIJNeHD4p-540AR2Q0_ZjwmKJ8",
#             "plus_code": {
#                 "compound_code": "6PFH+V8 Rostov-on-Don, Rostov Oblast, Russia",
#                 "global_code": "8GVX6PFH+V8"
#             },
#             "types": [
#                 "establishment",
#                 "point_of_interest",
#                 "university"
#             ]
#         }
#     ],
#     "status": "OK"
# }
