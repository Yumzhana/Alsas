# Import sqlite3 module (in standart library - do not need to install)
import sqlite3

# Connect ot Database - in local file app.db
conn = sqlite3.connect('app.db')
# Create a cursor - a
c = conn.cursor()

c.execute('''
CREATE TABLE events (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    description TEXT
)
''')

conn.commit()

c.execute('''
CREATE TABLE users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    password TEXT,
    login TEXT
    name TEXT
    img TEXT
)
''')

conn.commit()

#
# # Adding some data (feel free to use you own data)

c.execute('''
    INSERT INTO events (title, description)
     VALUES ("Поход в кино", "Предлагаю в воскресенье встретиться в кино")
 ''')

conn.commit()

user_list = [
    {
        'login': 'admin',
        'password': 'admin',
    },
    {
        'login': 'Masha',
        'password': '12345',
    },
    {
        'login': 'Alesha',
        'password': 'qwerty',
    }
]

for user in user_list:
    c.execute("INSERT INTO users "

    "(login, password) "
    "VALUES "
    "('{login}','{password}')".format(**user))
    conn.commit()

event_list = [
    {
        'title': 'Концерт Монеточки',
        'description': '5 февраля, 2019 года',
    },
    {
        'title': 'Спектакль Мастер и Маргарита',
        'description': 'Собираюсь в театр. 10 января жду всех',
    },
    {
        'title': 'Театр Балтийский дом',
        'description': 'Пошлите в театр',
    },    {
        'title': 'Концерт Монеточки',
        'description': '5 февраля, 2019 года',
    },
    {
        'title': 'Спектакль Мастер и Маргарита',
        'description': 'Собираюсь в театр. 10 января жду всех',
    },
    {
        'title': 'Театр Балтийский дом',
        'description': 'Пошлите в театр',
    },
    {
        'title': 'Иммерсивное шоу "Безликие"',
        'description': 'Одному стремно, ищу компнию. 1 февраля',
    },
    {
        'title': 'DnD в PlayLoft Gaga',
        'description': 'Ищу команду для захвата подземелья',
    },
    {
        'title': 'Ярмарка Boom freedom Bazaar',
        'description': 'Го покупать новогодние подарки',
    },
    {
        'title': 'Вечер живого джаза в Музее советских игровых автоматов',
        'description': 'Ищу ценителей джазовой музыки. Только 18+!!!!',
    },
    {
        'title': 'Концерт Rammstein',
        'description': '2 августа 2019 года. Да, я планирую жизнь заранее',
    },
    {
        'title': 'Концерт «Рождественский орган» от Amadeus Concerts',
        'description': 'Хочу провести рожденственский вечер в кругу хорошой музыки и эрудированных людей',
    },
    {
        'title': 'Встреча в баре "Пробирочная"',
        'description': 'Давайте напьемся!!',
    },
    {
        'title': 'Кино "Человек-паук: Через вселенные"',
        'description': 'Я смотрел этот фильм 7 раз. На 8ой мои друзья отказались со мной идти',
    },
    {
        'title': 'Спектакль «С Чарльзом Буковски за барной стойкой»',
        'description': 'Очень нужна компания!',
    },
    {
        'title': 'Спектакль «Разговоры» в «Квартире»',
        'description': 'Всех приглашаю на эксперементальный спектакль',
    },
    {
        'title': 'Мой др',
        'description': 'Давайте гулять, смеяться и петь песни во все горло. Делать это в одиночестве крайне странно',
    },
    {
        'title': 'Зимний «Каток у моря» в «Севкабель Порт»',
        'description': 'Научите меня кататься на коньках, кто-нибудь',
    },
    {
        'title': 'Киноночь',
        'description': '12 марта, давайте сходим в Люмбер-Холл',
    },
    {
        'title': 'Фестиваль технологий, науки и изобретений TECHWeekend',
        'description': '3-6 января, с 11 до 20',
    },
    {
        'title': 'Мастер-класс гончарного мастерства',
        'description': 'У меня сгорает сертификат на двоих. Кто-нибудь хочет сходить? бесплатно',
    }
]

for event in event_list:
    c.execute("INSERT INTO events "
              "(title, description) "
              "VALUES "
              "('{title}','{description}')".format(**event))
    conn.commit()