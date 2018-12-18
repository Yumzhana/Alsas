# Import sqlite3 module (in standart library - do not need to install)
import sqlite3

# Connect ot Database - in local file app.db
conn = sqlite3.connect('app.db')
# Create a cursor - a
c = conn.cursor()

c.execute('''
CREATE TABLE events (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    description TEXT
)
''')

conn.commit()
#
# # Adding some data (feel free to use you own data)

c.execute('''
    INSERT INTO events (title, description)
     VALUES ("Поход в кино", "Предлагаю в воскресенье встретиться в кино")
 ''')

conn.commit()

#
# c.execute('''
#     ALTER TABLE users
#     ADD COLUMN login TEXT
# ''')
# conn.commit()
#
# c.execute('''
#     UPDATE users
#     SET login="paul"
#     WHERE name="Paul Okopnyi"
# ''')
# conn.commit()
#
#
# c.execute('''
#     ALTER TABLE users
#     ADD COLUMN photo TEXT
# ''')
# conn.commit()
#
#
# # Our base data
# users = [
#     {
#         'login': 'igor',
#         'name': 'Igor Novikov',
#         'job_title': 'Designer',
#         'workplace': 'ArtLebedev'
#     },
#     {
#         'login': 'boris',
#         'name': 'Boris Ivanov',
#         'job_title': 'Cat',
#         'workplace': 'HSE Sedova'
#     }
# ]
# # Adding it in the loop
# for user in users:
#     c.execute("INSERT INTO users "
#               "(login, name, workplace, job_title) "
#               "VALUES "
#               "('{login}','{name}','{workplace}','{job_title}')".format(**user))
#     conn.commit()
#
# # Add second table
# c.execute('''
#     CREATE TABLE events (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         name TEXT,
#         desc TEXT,
#         date DATETIME
#     )
# ''')
# conn.commit()
#
# c.execute('''
#     INSERT INTO events (name, desc, date)
#     VALUES
#     ("Tusa","HSE Party Hard", "2019-01-10 21:00:00")
# ''')
# conn.commit()
#
# # Many to many connection
# c.execute('''
#     CREATE TABLE users_events (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         user_id INTEGER,
#         event_id INTEGER
#     )
# ''')
#
# conn.commit()
#
# c.execute("INSERT INTO users_events (user_id, event_id) VALUES (1, 1)")
# conn.commit()
# c.execute("INSERT INTO users_events (user_id, event_id) VALUES (3, 1)")
# conn.commit()
#
#
# c.execute("SELECT u.* "
#           "FROM users_events ue "
#           "JOIN users u ON (u.id=ue.user_id) "
#           "WHERE ue.event_id=1")
#
#
# conn.close()
