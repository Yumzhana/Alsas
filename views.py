from app import app, templateHTML

@app.route('/')
def homepage():
    return templateHTML('index.html')

@app.route('/results')
def results():
    return templateHTML('results.html')

@app.route('/event')
def event():
    return templateHTML('event.html')




