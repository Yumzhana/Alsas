from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

@app.route('/')
def index():
    conn = sqlite3.connect('app.db')
    conn.row_factory = dict_factory
    c = conn.cursor()

    # Handler logic here
    c.execute("SELECT * FROM events")
    events = list(c.fetchall())

    events.reverse()

    return render_template('_index.html', events=events)

@app.route('/add_events', methods=['GET', 'POST'])
def add_events():
   events_created = False

   if request.method == 'POST':
        # add new user data
        user = {}
        user['title'] = request.form.get('title')
        user['description'] = request.form.get('description')

        # save to database
        conn = sqlite3.connect('app.db')
        c = conn.cursor()
        c.execute("SELECT * FROM events where title='%s'" % user['title'])
        c.execute("INSERT INTO events "
                 "(title, description) "
                 "VALUES "
                 "('{title}','{description}')"
                 "".format(**user))
        conn.commit()
        events_created = True
        conn.close()

   return render_template(
       "add_events.html",
       events_created=events_created
   )

@app.route('/registration', methods=['GET', 'POST'])
def add_user():
   events_created = False

   if request.method == 'POST':
       user = {}
       user['login'] = request.form.get('login')
       user['password'] = request.form.get('password')
       user['name'] = request.form.get('password')
       user['img'] = request.form.get('password')

       # save to database
       conn = sqlite3.connect('app.db')
       c = conn.cursor()
       c.execute("SELECT * FROM users where title='%s'" % user['login'])
       c.execute("INSERT INTO users "
                 "(login, password, name, img) "
                 "VALUES "
                 "('{login}','{password}','{name}','{img}')"
                 "".format(**user))
       conn.commit()
       events_created = True
       conn.close()


   return render_template(
        "registration.html",
       events_created=events_created
   )


@app.route('/search')
def search_for_person():
    q = request.args.get('query')
    w = q.split(' ')
    print(w)
    result = []

    conn = sqlite3.connect('app.db')
    conn.row_factory = dict_factory
    c = conn.cursor()

    for x in w:
        print(x)
        c.execute("SELECT * FROM events WHERE title LIKE '%{q}%' OR id LIKE '%{q}%'"
                  "".format(q=x))

        list = c.fetchall()
        print(list)
        for y in list:
            result.append(y)

    # Close connection
    conn.close()
    return render_template('search_result.html', result=result)




if __name__ == "__main__":
    app.run()