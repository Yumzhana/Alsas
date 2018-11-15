from app import app

@app.route('/')
def homepage():
    return "Поиск"

@app.route('/results')
def results():
    return "Результаты поиска"

@app.route('/event')
def event():
    return "Мероприятие"




