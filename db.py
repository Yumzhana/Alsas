slovar = {
    'name': {
        'name2': 2,
        'name3': 3
    },
    'name2': {
        'name2': [1,2,3,4,5],
        'name3': [{ 'name': 1 }, { 'name': 2 }, { 'name': 3 }]
    }
}

_event = {
    'movie': [{'title': 'Богемская рапсодия', 'date': '26 ноября 2018', 'time': '15:00', 'location': 'кинотеатр Аврора'},
             {'title': 'Жена', 'date': '25 ноября 2018', 'time': '19:00', 'location': 'кинотеатр Пик'},
             {'title': 'Проклятье монахини', 'date': '29 ноября 2018', 'time': '20:30', 'location': 'кинотеатр Кинополис'}],

    'concert': [{'title': 'СБПЧ', 'date': '17 ноября 2018', 'time': '20:00', 'location': 'Новая Голландия'},
             {'title': 'Монеточка', 'date': '26 октября 2018', 'time': '20:00', 'location': 'Aurora Concert hall'},
             {'title': 'Motorama', 'date': '13 декабря 2018', 'time': '19:00', 'location': 'Какая-то концертная площадка'}]

}

def eventsearch(db, searchword):
    return db[searchword]



# return render_template('page01.html', user = user_data