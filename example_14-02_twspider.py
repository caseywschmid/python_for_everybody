from urllib.request import urlopen
import twurl
import json
import sqlite3
import ssl

TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'


conn = sqlite3.connect('spider.sqlite')

# *** DIR SQLITE3 *** 
# ['Binary', 'Connection', 'Cursor', 'DataError',
# 'DatabaseError', 'Date', 'DateFromTicks', 'Error', 'IntegrityError',
# 'InterfaceError', 'InternalError', 'NotSupportedError', 'OperationalError',
# 'PARSE_COLNAMES', 'PARSE_DECLTYPES', 'PrepareProtocol', 'ProgrammingError',
# 'Row', 'SQLITE_ALTER_TABLE', 'SQLITE_ANALYZE', 'SQLITE_ATTACH',
# 'SQLITE_CREATE_INDEX', 'SQLITE_CREATE_TABLE', 'SQLITE_CREATE_TEMP_INDEX',
# 'SQLITE_CREATE_TEMP_TABLE', 'SQLITE_CREATE_TEMP_TRIGGER',
# 'SQLITE_CREATE_TEMP_VIEW', 'SQLITE_CREATE_TRIGGER', 'SQLITE_CREATE_VIEW',
# 'SQLITE_CREATE_VTABLE', 'SQLITE_DELETE', 'SQLITE_DENY', 'SQLITE_DETACH',
# 'SQLITE_DONE', 'SQLITE_DROP_INDEX', 'SQLITE_DROP_TABLE',
# 'SQLITE_DROP_TEMP_INDEX', 'SQLITE_DROP_TEMP_TABLE',
# 'SQLITE_DROP_TEMP_TRIGGER', 'SQLITE_DROP_TEMP_VIEW', 'SQLITE_DROP_TRIGGER',
# 'SQLITE_DROP_VIEW', 'SQLITE_DROP_VTABLE', 'SQLITE_FUNCTION', 'SQLITE_IGNORE',
# 'SQLITE_INSERT', 'SQLITE_OK', 'SQLITE_PRAGMA', 'SQLITE_READ',
# 'SQLITE_RECURSIVE', 'SQLITE_REINDEX', 'SQLITE_SAVEPOINT', 'SQLITE_SELECT',
# 'SQLITE_TRANSACTION', 'SQLITE_UPDATE', 'Time', 'TimeFromTicks', 'Timestamp',
# 'TimestampFromTicks', 'Warning', 'adapt', 'adapters', 'apilevel',
# 'collections', 'complete_statement', 'connect', 'converters', 'datetime',
# 'dbapi2', 'enable_callback_tracebacks', 'enable_shared_cache', 'paramstyle',
# 'register_adapter', 'register_converter', 'sqlite_version',
# 'sqlite_version_info', 'threadsafety', 'time', 'version', 'version_info']

# *** DIR CONN *** 
# ['DataError', 'DatabaseError', 'Error', 'IntegrityError',
# 'InterfaceError', 'InternalError', 'NotSupportedError', 'OperationalError',
# 'ProgrammingError', 'Warning', 'backup', 'close', 'commit',
# 'create_aggregate', 'create_collation', 'create_function', 'cursor',
# 'execute', 'executemany', 'executescript', 'in_transaction', 'interrupt',
# 'isolation_level', 'iterdump', 'rollback', 'row_factory', 'set_authorizer',
# 'set_progress_handler', 'set_trace_callback', 'text_factory', 'total_changes']

# This is the variable that we're interested in. It works kind of like a file
# handle. Its not as simple as just open it and read it. You'll send commands to
# SQL through the cursor and get back your responses from there as well.
cur = conn.cursor()

# *** DIR CUR *** 
# 'close', 'connection', 'description', 'execute', 'executemany',
# 'executescript', 'fetchall', 'fetchmany', 'fetchone', 'lastrowid',
# 'row_factory', 'rowcount', 'setinputsizes', 'setoutputsize']

# This is creating a table named Twitter with column names 'retrieved' and
# 'friends' and placing it in the spider.sqlite database created earlier
cur.execute(''' 
                CREATE TABLE IF NOT EXISTS Twitter (name TEXT,
                retrieved INTEGER, friends INTEGER)''')

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# This loop will run until the user tells it to quit
while True:
    # Gets Twitter account name from user
    acct = input('Enter a Twitter account (type \'quit\' to quit): ')
    if (acct == 'quit'):
        break
    # If the user just hits 'Enter' instead of typing a Twitter account name,
    # the program will randomly choose a person from the spider.sqlite database
    # who has not yet had their data retreived (WHERE retrieved = 1).
    if (len(acct) < 1):
        cur.execute('SELECT name FROM Twitter WHERE retrieved = 0 LIMIT 1')
        try:
            # This will set the acct variable to the first argument after SELECT
            # in the .execute() statement above; in this case it's 'name'.
            # fetchone() means "get one row from the database" 
            # [0] means "get the first column of the first row"
            acct = cur.fetchone()[0]
        # If the above fails, it means that there are no accounts in the
        # database that have not been retreived already. 
        except:
            print('No unretrieved Twitter accounts found')
            continue
    
    # This uses the twurl.py file to generate the required URL adding on the
    # hidden keys needed to get the code to work.
    url = twurl.augment(TWITTER_URL, {'screen_name': acct, 'count': '5'})
    print('Retrieving', url)

    connection = urlopen(url, context=ctx)
    # This returns the data only with no headers. Doesn't actually print anything. 
    # .read() gives you data in UTF-8 (bytes)
    # .decode() gives you data in Unicode which is what you need in Python
    data = connection.read().decode()
    # If you want your headers, you've got to ask for them. In this case, we
    # want the headers beacuse it has some important information in there. Like
    # how many more times we can run this code before Twitter cuts us off. 
    headers = dict(connection.getheaders())

    # Prints out how many remaining times we can run the code.
    print('Remaining', headers['x-rate-limit-remaining'])
    
#     # This loads the data so you can use it.
#     js = json.loads(data)
    
#     # Debugging
#     # print json.dumps(js, indent=4)

#     # This will update the Twitter table in the database to change the
#     # 'retrieved' column from 0 to 1 to keep track of who has been looked up and
#     # who has not. The "? '" is a placeholder to prevent SQL Injection
#     # (basically a way for people to gain access to the database contents by
#     # manipulating the user input field to be pieces of SQL code so that when the
#     # final command is concatenated it is legit SQL code that could do something
#     # sinister like print out the entire list of users and their passwords). The
#     # tuple at the end will be what gets replaced with the placeholder. This
#     # line is essentially like opening a file. It doesn't acutally read
#     # anything. 
#     cur.execute('UPDATE Twitter SET retrieved = 1 WHERE name = ?', (acct, ))

#     # This code will loop through every 'user' in the data. It will set a
#     # variable (friend') to the users 'screen_name' and print that out. Next it
#     # will select the 'friends' column of the Twitter table in the spider.sqlite
#     # database with the 'friend' screen-name. It will then update the friends
#     # count number for the friend. If not, it will add the new friend to the
#     # database and initialize its retrieved count to 0.
#     countnew = 0
#     countold = 0
#     for u in js['users']:
#         friend = u['screen_name']
#         print(friend)
#         cur.execute('SELECT friends FROM Twitter WHERE name = ? LIMIT 1', (friend, ))
#         try:
#             count = cur.fetchone()[0]
#             cur.execute('UPDATE Twitter SET friends = ? WHERE name = ?', (count + 1, friend))
#             countold = countold + 1
#         except:
#             cur.execute('INSERT INTO Twitter (name, retrieved, friends) VALUES (?, 0, 1)', (friend, ))
#             countnew = countnew + 1
#     print('New accounts=', countnew, ' revisited=', countold)
#     conn.commit()
# cur.close()
