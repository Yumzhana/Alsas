from flask import Flask, render_template, request

app = Flask(__name__)

def search(a, key):
    catalog = []
    for n in a:
        if n == key:
            catalog.append(n)
    return catalog

# @app.route('/')
# def homepage():
#     return render_template('index.html')

@app.route('/')
def helloworld():
    # conn = sqlite3.connect('app.db')
    # c = conn.cursor()
    #
    # c.execute("SELECT + FROM users")
    # users = list(c.fetchall())
    #
    # conn.close()
    return render_template('_index.html', users = users) # Вывод html-файла по указанному маршруту

@app.route('/search') # Функция для указания маршрута
def search_for_event(): # Функция, которая выполняется сразу при переходе по заданному адресу
    q = request.args.get('query') # Создаем переменную, которая равна запросу
    events = search(list, q) # Создаем переменную, которая выполняет функцию search в конкретном списке и по конкретному запросу
    return render_template('results.html', t = q, g = events ) # Вывод html-файла и передача на него результатов поиска


if __name__ == "__main__": # Дефолтное выражение, проверяющее подключен ли фласк
    app.run() # Запуск приложения







