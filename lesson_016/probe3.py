
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

from playhouse.db_url import connect

import DatabaseUpdater
from Postcards import make_postcards
from WeatherMaker import GetWeather

db = connect('sqlite:///weather.db')
db.create_tables([Weather])

weatherbase = {}

monthsdict2 = {1: 'january', 2: 'february', 3: 'march', 4: 'april', 5: 'may', 6: 'june', 7: 'july', 8: 'august',
               9: 'september', 10: 'october', 11: 'november', 12: 'december'}


def write_to_dict(period_start, period_end):
    months = []
    years = []
    period_start = datetime.datetime.strptime(period_start, '%Y-%m-%d').date()
    period_start1 = period_start
    period_end = datetime.datetime.strptime(period_end, '%Y-%m-%d').date()

    deltam = datetime.timedelta(weeks=4)
    while period_start1 <= period_end + datetime.timedelta(days=30):
        if monthsdict2[period_start1.month] not in months:
            months.append((monthsdict2[period_start1.month], period_start1.year))
        period_start1 += deltam

    gw = GetWeather(weatherbase, months=months, years=years, period_start=period_start)
    gw.run()
    delta = datetime.timedelta(days=1)
    while period_start <= period_end:
        wb = weatherbase[period_start]
        # temp = wb['температура'].replace('\n', ' ')
        # print(
        #     f"{wb['дата']}:,температура: {temp}, осадки: {wb['погода']}, ветер: {wb['ветер']}, "
        #     f"давление:{wb['давление']}, влажность:{wb['влажность']}")
        print(f'Прогноз за {wb["дата"]} загружен')
        period_start += delta


def on_run():
    months = []
    years = []
    period_end = datetime.datetime.now()
    deltaa = datetime.timedelta(days=7)
    period_start = period_end - deltaa
    period_start1 = period_start

    deltam = datetime.timedelta(weeks=4)
    while period_start1 <= period_end + datetime.timedelta(days=30):
        if monthsdict2[period_start1.month] not in months:
            months.append((monthsdict2[period_start1.month], period_start1.year))
        period_start1 += deltam

    gw = GetWeather(weatherbase, months=months, years=years, period_start=period_start)
    gw.run()
    delta = datetime.timedelta(days=1)
    while period_start <= period_end:
        wb = weatherbase[period_start.date()]
        temp = wb['температура'].replace('\n', ' ')
        print(
            f"{wb['дата']}:,температура: {temp}, осадки: {wb['погода']}, ветер: {wb['ветер']}, "
            f"давление:{wb['давление']}, влажность:{wb['влажность']}")
        # print(f'Прогноз за {wb["дата"]} загружен')
        period_start += delta
    print(weatherbase)


def check_date(*start_date):
    re_date = re.compile(
        r"^([1-9]|0[1-9]|1[0-9]|2[0-9]|3[0-1])(\.|-|/)"
        r"([1-9]|0[1-9]|1[0-2])(\.|-|/)([0-9][0-9]|19[0-9][0-9]|20[0-9][0-9])$")
    deltadays = 14
    while True:
        user_date = input('>>> ')
        match = re.findall(re_date, user_date)

        if match:
            user_date = datetime.datetime.strptime(user_date, '%d-%m-%Y').date()
            if user_date > datetime.date.today() + datetime.timedelta(days=deltadays):
                print(f'Прогноз может быть не более, чем на {deltadays} дней вперед', end='')
            else:
                if not start_date:
                    return str(user_date)
                else:
                    if user_date < datetime.datetime.strptime(start_date[0], '%Y-%m-%d').date():
                        print(f'Конец диапазона не может быть раньше его начала', end='')
                    else:
                        return str(user_date)

        else:
            print('Неправильно указана дата. Введите в формате ДД-ММ-ГГГГ', end='')


start_date = None
end_datec = None
on_run()
while True:
    print(f'\n1(1) для задания диапазона дат\n' \
          f'(2) для загрузки данных из сети\n' \
          f'(3) для записи дат за указанный диапазон в базу данных\n' \
          f'(4) для чтения данных за указанный диапазон из базы данных\n' \
          f'(5) для создания открыток с погодой за указанный диапазон\n' \
          f'(6) для вывода прогнозов за указанный диапазон на экран\n' \
          f'(7) для выхода\n')

    user_choice = input('>>>')
    if user_choice == '1':
        print('Введите НАЧАЛО диапазона в формате ДД-ММ-ГГГГ', end='')
        start_date = check_date()
        print('Введите КОНЕЦ диапазона в формате ДД-ММ-ГГГГ', end='')
        end_date = check_date(start_date)
    elif user_choice == '2' and start_date:
        write_to_dict(start_date, end_date)
        DatabaseUpdater.update_db(weatherbase, start_date, end_date)
    elif user_choice == '3' and start_date:
        DatabaseUpdater.update_db(weatherbase, start_date, end_date)

    elif user_choice == '4' and start_date:
        weatherbase = DatabaseUpdater.read_db('2020-01-01', '2020-01-02')

        DatabaseUpdater.show(start_date, end_date)
    elif user_choice == '5' and start_date:
        make_postcards(start_date, end_date)
    elif user_choice == '6' and start_date:
        DatabaseUpdater.show(start_date, end_date)
    elif user_choice == '7':
        break
    elif start_date is None:
        print('Не указан диапазон дат')
