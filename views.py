# отвечает за пути, чтобы не засорять код приложения
from app import app, templateHTML
import db

@app.route('/')
def homepage():
    return templateHTML('_index.html')


@app.route('/events/<events>')
def user_page(events):
    name_data = db._event.get(events)
    return templateHTML('_event.html', info=name_data, type=events)








# сделать айди мероприятий






