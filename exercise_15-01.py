import sqlite3

conn = sqlite3.connect('exercise_15-01_Ages.sqlite')
cur = conn.cursor()

# Do some setup
cur.executescript('''
                DROP TABLE IF EXISTS Ages;

                CREATE TABLE Ages (
                    name VARCHAR(128),
                    age INTEGER
                )
''')






# fname = input('Enter file name: ')
# if len(fname) < 1:
#     fname = 'roster_data_sample.json'

# # [
# #   [ "Charley", "si110", 1 ],
# #   [ "Mea", "si110", 0 ],

# str_data = open(fname).read()
# json_data = json.loads(str_data)

# for entry in json_data:

#     name = entry[0]
#     title = entry[1]
#     role = entry[2]

#     print((name, title))

#     cur.execute('''INSERT OR IGNORE INTO User (name)
#         VALUES ( ? )''', ( name, ) )
#     cur.execute('SELECT id FROM User WHERE name = ? ', (name, ))
#     user_id = cur.fetchone()[0]

#     cur.execute('''INSERT OR IGNORE INTO Course (title)
#         VALUES ( ? )''', ( title, ) )
#     cur.execute('SELECT id FROM Course WHERE title = ? ', (title, ))
#     course_id = cur.fetchone()[0]

#     cur.execute('''INSERT OR REPLACE INTO Member
#         (user_id, course_id, role) VALUES ( ?, ?, ? )''',
#         ( user_id, course_id, role ) )

#     conn.commit()
   

#   SELECT User.name, Member.role, Course.title
#   FROM User JOIN Member JOIN Course
#   ON Member.user_id = User.id AND Member.course_id = Course.id
#   ORDER BY Course.title, Member.role DESC, User.name