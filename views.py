# отвечает за пути, чтобы не засорять код приложения
from app import app, templateHTML
import db

@app.route('/')
def homepage():
    return templateHTML('index.html')

@app.route('/results')
def results():
    return templateHTML('results.html')

@app.route('/event')
def event():
    return templateHTML('event.html')

@app.route('/user/<username>')
def user_page(username):
    name_data = db._users.get(username)
    return templateHTML('index.html', user=name_data)








# сделать айди мероприятий






