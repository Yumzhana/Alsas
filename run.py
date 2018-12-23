from flask import Flask, render_template, request, redirect
import sqlite3

class User():
    status = False

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
    c.execute("SELECT * FROM events")
    events = list(c.fetchall())
    events.reverse()
    return render_template('index.html', events=events, user=User)

@app.route('/add_events', methods=['GET', 'POST'])
def add_events():
   events_created = False

   if request.method == 'POST':
        _events = {}
        _events['title'] = request.form.get('title')
        _events['description'] = request.form.get('description')

        # save to database
        conn = sqlite3.connect('app.db')
        c = conn.cursor()
        c.execute("SELECT * FROM events where title='%s'" % _events['title'])
        c.execute("INSERT INTO events "
                 "(title, description) "
                 "VALUES "
                 "('{title}','{description}')"
                 "".format(**_events))
        conn.commit()
        events_created = True
        conn.close()

   if (events_created):
       return redirect('/')

   return render_template(
       "add_events.html",
       events_created=events_created
   )

@app.route('/registration', methods=['GET', 'POST'])
def add_user():
   user_created = False
   user_error = False

   if request.method == 'POST':
       user = {}
       user['login'] = request.form.get('login')
       user['password'] = request.form.get('password')
       
       conn = sqlite3.connect('app.db')
       c = conn.cursor()
       c.execute("SELECT * FROM users where login='%s'" % user['login'])
       if c.fetchone():
           user_error = True
       else:
           c.execute("INSERT INTO users "
                     "(login, password) "
                     "VALUES "
                     "('{login}','{password}')"
                     "".format(**user))
           conn.commit()
           user_created = True
           conn.close()
           User.status = True
           User.name = user['login']

   if (user_created):
        return redirect('/')

   return render_template(
        "registration.html",
       user_created=user_created,
       user_error = user_error
   )

@app.route('/login', methods=['GET', 'POST'])
def login_user():
    loginComplete = False
    loginError = False
    if request.method == 'POST':
        en_d = {}
        en_d['login'] = request.form.get('login')
        en_d['password'] = request.form.get('password')

        conn = sqlite3.connect('app.db')
        c = conn.cursor()
        c.execute("SELECT * FROM users where login='%s'" % en_d['login'])
        if c.fetchone():
            f = conn.cursor()
            f.execute("SELECT * FROM users where password='%s'" % en_d['password'])
            if f.fetchone():
                User.status = True
                loginComplete = True
            else:
                loginError = True
        else:
            loginError = True

    if (loginComplete):
        return redirect('/')
    return render_template("login.html", loginComplete=loginComplete, loginError=loginError)

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
        bgw = x.title()
        x = x.lower()
        c.execute("SELECT * FROM events WHERE title LIKE '%{q}%' OR title LIKE '%{k}%'"
                  "".format(q=x, k=bgw))

        list = c.fetchall()
        print(list)
        for y in list:
            result.append(y)

    conn.close()
    return render_template('search_result.html', result=result, user=User)



@app.route('/event/<event_id>')
def event_page(event_id):
    conn = sqlite3.connect('app.db')
    conn.row_factory = dict_factory
    c = conn.cursor()

    c.execute("SELECT * FROM events WHERE id LIKE '%{q}%'"
              "".format(q=event_id))
    events = list(c.fetchall())
    print(events)

    return render_template('event.html', event=events, user=User)

@app.route('/exit')
def exit():
    User.status = False
    return redirect('/')

if __name__ == "__main__":
    app.run()