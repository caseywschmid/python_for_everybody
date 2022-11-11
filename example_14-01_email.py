import sqlite3

# If you name a file that doesn't exist, it will create the file into the
# current directory
connection = sqlite3.connect('emaildb.sqlite')

# This is the variable that we're interested in. It works kind of like a file
# handle. Its not as simple as just open it and read it. You'll send commands to
# SQL through the cursor and get back your responses from there as well. 
curser = connection.cursor()

# The DROP TABLE statement removes a table added with the CREATE TABLE
# statement. The name specified is the table name. The dropped table is
# completely removed from the database schema and the disk file. The table can
# not be recovered. All indices and triggers associated with the table are also
# deleted. The optional IF EXISTS clause suppresses the error that would
# normally result if the table does not exist. This is not normally something
# you'll do. For this example, I'm starting with a fresh database and want to
# make sure that I'm starting with a clean slate. 
curser.execute('DROP TABLE IF EXISTS Counts')

# This will create a table inside the emaildb.sqlite that has two columns: Email
# (type Text) and Count (type Integer)
curser.execute('CREATE TABLE Counts (email TEXT, count INTEGER)')

filename = input('Enter file name: ')
if (len(filename) < 1): 
    filename = 'mbox-short.txt'
filehandle = open(filename)
for line in filehandle:
    if not line.startswith('From: '): 
        continue
    pieces = line.split()
    email = pieces[1]
    
    #************************ Dictionary Part *************************
    
    # Select the Count column in the table of the emaildb.sqlite where an email
    # has been entered. The "? '" is a placeholder to prevent SQL Injection
    # (basically a way for people to gain access to the database contents by
    # manipulating the user input to be pieces of SQL code so that when the
    # final command is concatenated it is legit SQL code that could do something
    # sinister like print out the entire list of users and thier passwords). 
    # The tuple at the end will be what gets replaced with the placeholder. 
    # This line is essentially like opening a file. It doesn't acutally read anything. 
    curser.execute('SELECT count FROM Counts WHERE email = ? ', (email,))
    # This varaible is where the actual data goes. 
    row = curser.fetchone()
    
    if row is None:
        # If the email doesn't exist, then it needs to be added to the database
        # and its count initialized to 1.
        curser.execute('''INSERT INTO Counts (email, count)
                VALUES (?, 1)''', (email,))
    else:
        # If it already exists in the database, update the count column. Its
        # always better to use UPDATE via SQL and increment a count that way
        # instead of doing it ouside of SQL inside Python
        curser.execute('UPDATE Counts SET count = count + 1 WHERE email = ?', (email,))

    #************************ Dictionary Part *************************

    # The code will keep everything in memory until you tell it 'commit' the data where it will get officially changed in the database. In this example, we're committing every time the loop cycles. Sometimes you may want to commit every 10 or 100 cycles. 
    connection.commit()

# https://www.sqlite.org/lang_select.html
# This code says "Select the email and count columns in the Counts table of the emaildb.sqlite file, sort them by count from highest to lowest, and return the top 10 entries"
sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'

# This print statement will generate a 'table' in the Terminal of the data requested
for row in curser.execute(sqlstr):
    print(str(row[0]), row[1])

curser.close()