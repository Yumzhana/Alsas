from flask import Flask, render_template, request # Импорт нужных функций
from database import list # Импорт нужного списка из базы данных

app = Flask(__name__) # Обозначение функции Flask как переменную app

def search(a, key): # Функция поиска по списку
    catalog = [] # Новвый список для всех результатов
    for n in a: # Цикл, который перебирает все элементы в списке
        if n == key: # Условие - если элемент совпадает с ключевым словом,
            catalog.append(n) # Этот элемент добавляется в список catalog
    return catalog # Возвращает список всех элементов, совпадающих с ключевым словом

@app.route('/') # Функция route для указания пути (маршрута)
def homepage(): # Задание функции
    return render_template('index.html') # Вывод html-файла по указанному маршруту

@app.route('/search') # Функция для указания маршрута
def search_for_event(): # Функция, которая выполняется сразу при переходе по заданному адресу
    q = request.args.get('query') # Создаем переменную, которая равна запросу
    events = search(list, q) # Создаем переменную, которая выполняет функцию search в конкретном списке и по конкретному запросу
    return render_template('results.html', t = q, g = events ) # Вывод html-файла и передача на него результатов поиска


if __name__ == "__main__": # Дефолтное выражение, проверяющее подключен ли фласк
    app.run() # Запуск приложения







