# Import sqlite3 module (in standart library - do not need to install)
import sqlite3

# Connect ot Database - in local file app.db
conn = sqlite3.connect('app.db')
# Create a cursor - a
c = conn.cursor()

c.execute('''
CREATE TABLE list (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    job_title TEXT,
    workplace TEXT
)
''')

c.execute('''
CREATE TABLE list (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    author_id INTEGER
    FOREIGN KEY(author_id ) REFERENCES users(id),
)
''')

for user in users:
    c.execute("INSERT INTO users"
              "(login, name, workplace, job_title)"
              "VALUES"
              "('{login}', '{name}', '{workplace}', '{job_title}')".format(**user))

# Many to many connections
c.execute('''
    CREATE TABLE users_events (
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        author_id INTEGER,
        event_id INTEGER,
        FOREIGN KEY(user_id) REFERENCES users(id)
        FOREIGN KEY(event_id) REFERENCES events(id)
    )
''')



conn.commit()
