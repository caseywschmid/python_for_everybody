import xml.etree.ElementTree as ET
import sqlite3

conn = sqlite3.connect('trackdb.sqlite')
cur = conn.cursor()

# Make some fresh tables using executescript() NO COMMAS after the last column
# name in each table. It won't work Ensure you have semicolons after each table
# statement. INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE is the way to get
# SQLite to auto generate and auto increment the primary keys for each entry
cur.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;
DROP TABLE IF EXISTS Genre;

CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE
);

CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE
);

CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title TEXT UNIQUE
);

CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY 
        AUTOINCREMENT UNIQUE,
    title TEXT UNIQUE,
    album_id INTEGER,
    genre_id INTEGER,
    length INTEGER, rating INTEGER, count INTEGER
);
''')


filename = input('Enter file name: ')
if ( len(filename) < 1 ) : 
    filename = 'My_Library.xml'

# <key>Track ID</key><integer>369</integer>
# <key>Name</key><string>Another One Bites The Dust</string>
# <key>Artist</key><string>Queen</string>
def lookup(d, key):
    found = False
    for child in d:
        if found : return child.text
        if child.tag == 'key' and child.text == key :
            found = True
    return None

# This gives you back an element tree 
stuff = ET.parse(filename)
# This will extract all data from the 'directory' you told it to use; in this
# case, dict/dict/dict. It returns all the data in the form of a list of XML
# Elements 
# [<Element 'dict' at 0x10081c400>, <Element 'dict' at 0x10081d710>,
# <Element 'dict' at 0x10081ea20>, <Element 'dict' at 0x10081fe70>, <Element
# 'dict' at 0x1008291c0>, ..., ...]
all = stuff.findall('dict/dict/dict')
print('Dict count:', len(all))
# This loop goes through every entry in the all element list and performs a
# lookup() on whatever values you want to pull and prints that out. Here's an
# example of one track in the XML:

#           <key>Track ID</key><integer>321</integer>
# 			<key>Name</key><string>Straight Away</string>
# 			<key>Artist</key><string>Mat Kearney</string>
# 			<key>Album Artist</key><string>Mat Kearney</string>
# 			<key>Composer</key><string>Mat Kearney</string>
# 			<key>Album</key><string>City of Black &#38; White</string>
# 			<key>Genre</key><string>Rock</string>
# 			<key>Kind</key><string>Purchased AAC audio file</string>
# 			<key>Size</key><integer>8158098</integer>
# 			<key>Total Time</key><integer>230453</integer>
# 			<key>Disc Number</key><integer>1</integer>
# 			<key>Disc Count</key><integer>1</integer>
# 			<key>Track Number</key><integer>10</integer>
# 			<key>Track Count</key><integer>12</integer>
# 			<key>Year</key><integer>2009</integer>
# 			<key>Date Modified</key><date>2019-02-13T04:51:53Z</date>
# 			<key>Date Added</key><date>2014-02-14T18:25:12Z</date>
# 			<key>Bit Rate</key><integer>256</integer>
# 			<key>Sample Rate</key><integer>44100</integer>
# 			<key>Release Date</key><date>2009-05-18T12:00:00Z</date>
# 			<key>Artwork Count</key><integer>1</integer>
# 			<key>Sort Album</key><string>City of Black &#38; White</string>
# 			<key>Sort Artist</key><string>Mat Kearney</string>
# 			<key>Sort Name</key><string>Straight Away</string>
# 			<key>Persistent ID</key><string>1A03511158209680</string>
# 			<key>Track Type</key><string>Remote</string>
# 			<key>Purchased</key><true/>

for entry in all:
    if ( lookup(entry, 'Track ID') is None ) : 
        continue
    name = lookup(entry, 'Name')
    genre = lookup(entry, 'Genre')
    artist = lookup(entry, 'Artist')
    album = lookup(entry, 'Album')
    count = lookup(entry, 'Play Count')
    rating = lookup(entry, 'Rating')
    length = lookup(entry, 'Total Time')

    if name is None or artist is None or album is None : 
        continue

    print(name, genre, artist, album, count, rating, length)

    # What you're going to do now is start putting all this data you just
    # printed into the database you created earlier. You listed Artist name as
    # UNIQUE. If you try to search the same artist name twice, this code will
    # blow up. Adding the INSERT OR IGNORE says "If there's already an artist
    # has already been insterted, don't insert it again" This line of code reads
    # "Insert into the Artist Table in the name column the artist it retrieved
    # from the XML. If it's already listed, then ignore it." The ? in the VALUES
    # is a placeholder for the info that will get put in there. To pass the
    # info, it has to be in the form of a tuple. This is how you write a "one
    # tuple" in Python
    cur.execute('INSERT OR IGNORE INTO Artist (name) VALUES ( ? )', ( artist, ) )
    # The above line may or may not have done the insert. But now you need to
    # know what the artist_id is. To look that up, you select the cell first
    # using the code below, then set the info in that cell to a variable. 
    cur.execute('SELECT id FROM Artist WHERE name = ? ', (artist, ))            
    artist_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Genre (name) 
        VALUES ( ? )''', ( genre, ) )
    cur.execute('SELECT id FROM Genre WHERE name = ? ', (genre, ))
    genre_id = cur.fetchone()[0]

    # Now that you have the artist_id stored you can use that to set up your
    # Album Table
    cur.execute('''INSERT OR IGNORE INTO Album (title, artist_id) 
        VALUES ( ?, ? )''', ( album, artist_id ) )
    cur.execute('SELECT id FROM Album WHERE title = ? ', (album, ))
    album_id = cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Track
        (title, album_id, genre_id, length, rating, count) 
        VALUES ( ?, ?, ?, ?, ?, ? )''', 
        ( name, album_id, genre_id, length, rating, count ) )

    conn.commit()