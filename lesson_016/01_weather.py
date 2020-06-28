# -*- coding: utf-8 -*-

# В очередной спешке, проверив приложение с прогнозом погоды, вы выбежали
# навстречу ревью вашего кода, которое ожидало вас в офисе.
# И тут же день стал хуже - вместо обещанной облачности вас встретил ливень.

# Вы промокли, настроение было испорчено, и на ревью вы уже пришли не в духе.
# В итоге такого сокрушительного дня вы решили написать свою программу для прогноза погоды
# из источника, которому вы доверяете.

# Для этого вам нужно:

# Создать модуль-движок с классом WeatherMaker, необходимым для получения и формирования предсказаний.
# В нём должен быть метод, получающий прогноз с выбранного вами сайта (парсинг + re) за некоторый диапазон дат,
# а затем, получив данные, сформировать их в словарь {погода: Облачная, температура: 10, дата:datetime...}

# Добавить класс ImageMaker.
# Снабдить его методом рисования открытки
# (использовать OpenCV, в качестве заготовки брать lesson_016/python_snippets/external_data/probe.jpg):
#   С текстом, состоящим из полученных данных (пригодится cv2.putText)
#   С изображением, соответствующим типу погоды
# (хранятся в lesson_016/python_snippets/external_data/weather_img ,но можно нарисовать/добавить свои)
#   В качестве фона добавить градиент цвета, отражающего тип погоды
# Солнечно - от желтого к белому
# Дождь - от синего к белому
# Снег - от голубого к белому
# Облачно - от серого к белому

# Добавить класс DatabaseUpdater с методами:
#   Получающим данные из базы данных за указанный диапазон дат.
#   Сохраняющим прогнозы в базу данных (использовать peewee)

# Сделать программу с консольным интерфейсом, постаравшись все выполняемые действия вынести в отдельные функции.
# Среди действий, доступных пользователю, должны быть:
#   Добавление прогнозов за диапазон дат в базу данных
#   Получение прогнозов за диапазон дат из базы
#   Создание открыток из полученных прогнозов
#   Выведение полученных прогнозов на консоль
# При старте консольная утилита должна загружать прогнозы за прошедшую неделю.

# Рекомендации:
# Можно создать отдельный модуль для инициализирования базы данных.
# Как далее использовать эту базу данных в движке:
# Передавать DatabaseUpdater url-путь
# https://peewee.readthedocs.io/en/latest/peewee/playhouse.html#db-url
# Приконнектится по полученному url-пути к базе данных
# Инициализировать её через DatabaseProxy()
# https://peewee.readthedocs.io/en/latest/peewee/database.html#dynamically-defining-a-database
import datetime
import re

import DatabaseUpdater
from WeatherMaker import MakeWeather

weather_base = {}

monthsdict2 = {1: 'january', 2: 'february', 3: 'march', 4: 'april', 5: 'may', 6: 'june', 7: 'july', 8: 'august',
               9: 'september', 10: 'october', 11: 'november', 12: 'december'}


class Start:
    def __init__(self):
        self.start_date = None
        self.end_date = None
        self.db_updater = None

        self.actions = {'1': self.define_dates, '2': self.update_dict, '3': self.update, '4': self.read_db,
                        '5': self.make_cards, '6': self.show}

    def check_date(*start_date):
        re_date = re.compile(
            r"^([1-9]|0[1-9]|1[0-9]|2[0-9]|3[0-1])(\.|-|/)"
            r"([1-9]|0[1-9]|1[0-2])(\.|-|/)([0-9][0-9]|19[0-9][0-9]|20[0-9][0-9])$")
        delta_days = 14
        while True:
            user_date = input('>>> ')
            match = re.findall(re_date, user_date)
            if not match:
                print('Неправильно указана дата. Введите в формате ДД-ММ-ГГГГ', end='')
                continue
            user_date = datetime.datetime.strptime(user_date, '%d-%m-%Y').date()
            if user_date > datetime.date.today() + datetime.timedelta(days=delta_days):
                print(f'Прогноз может быть не более, чем на {delta_days} дней вперед', end='')
            elif start_date and user_date < datetime.datetime.strptime(start_date[0], '%Y-%m-%d').date():
                print(f'Конец диапазона не может быть раньше его начала', end='')
            else:
                return str(user_date)

    def define_dates(self):
        print('Введите НАЧАЛО диапазона в формате ДД-ММ-ГГГГ', end='')
        self.start_date = Start.check_date()
        print('Введите КОНЕЦ диапазона в формате ДД-ММ-ГГГГ', end='')
        self.end_date = Start.check_date(self.start_date)
        self.db_updater = DatabaseUpdater.DatabaseUpdater(self.start_date, self.end_date)

    def update_dict(self):
        MakeWeather().write_to_dict(self.start_date, self.end_date)

    def update(self):
        MakeWeather().write_to_dict(self.start_date, self.end_date)
        self.db_updater.update_db()

    def read_db(self):
        self.weather_base = self.db_updater.read_db()

    def make_cards(self):
        self.db_updater.make_postcards()

    def show(self):
        self.db_updater.show()

    def menu(self):

        while True:
            print('''
        (1) для задания диапазона дат
        (2) для загрузки данных из сети
        (3) для записи дат за указанный диапазон в базу данных
        (4) для чтения данных за указанный диапазон из базы данных
        (5) для создания открыток с погодой за указанный диапазон
        (6) для вывода прогнозов за указанный диапазон на экран
        (7) для выхода''')

            user_choice = input('>>>')
            if '1' in user_choice:
                self.define_dates()
            elif user_choice in self.actions and self.start_date:
                now = self.actions[user_choice]
                now()
            elif '7' in user_choice:
                break
            elif self.start_date is None:
                print('Не указан диапазон дат')


MakeWeather().on_run()
Start().menu()
