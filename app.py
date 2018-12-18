from flask import Flask, render_template, request
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
    return render_template('_index.html', events=events)

@app.route('/add_user', methods=['GET', 'POST'])
def add_user():
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
        # return redirect('/user/%s/' % user['title'])


   return render_template(
        "add_events.html",
       events_created=events_created
   )


if __name__ == "__main__":
    app.run()