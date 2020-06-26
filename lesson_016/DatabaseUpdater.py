from datetime import datetime, timedelta, date

# from models import Weather
from playhouse import db_url
from playhouse.db_url import connect, SqliteDatabase

#
# import models
#
# Weather = models.
# TODO Тоже обернуть в класс всё, добавить инициализацию БД по db_url
# TODO Вынести всё нужное в атрибуты классы

#TODO Не могу понять, как инициальизировать базу

import models

db = connect(db_url)
models.db_proxy.initialize(SqliteDatabase('weather.db'))
db.create_tables([db])




def update_db(weather_base, period_start, period_end):
    period_start = datetime.strptime(period_start, '%Y-%m-%d').date()
    period_end = datetime.strptime(period_end, '%Y-%m-%d').date()

    print("\nMODIFYING DB:", end='')
    delta = timedelta(days=1)
    while period_start <= period_end:
        value = weather_base[period_start]
        value['date'] = db.get_or_create(day=value['date'], daterus=value['дата'], temperature=value['температура'],
                                condition=value['погода'], wind=value['ветер'], humidity=value['влажность'],
                                pressure=value['давление'], picture=value['picture'])
        print('O', end='')
        period_start += delta
    print(' Done')


def show(period_start, period_end):
    for query in db.select().where(Weather.day.between(period_start, period_end)):
        print(query.daterus, query.temperature.replace('\n', ' '), query.condition, query.wind, query.humidity,
              query.pressure)

#
# def check_for_update():
#     for zxc in Weather.select().where(Weather.daterus.contains('Сегодня')):
#         if str(zxc.day) == str(date.today()):
#             print('DB UPDATED')
#             pass
#         else:
#             print('UPDATING DB')
#             update_db()


def read_db(period_start, period_end):
    weather_base = {}
    delta = timedelta(days=1)

    for query in db.select().where(db.day.between(period_start, period_end)):
        dbdate = datetime.strptime(query.day, '%Y-%m-%d').date()

        weather_base[dbdate] = {}
        weather_base[dbdate]['температура'] = query.temperature
        weather_base[dbdate]['погода'] = query.condition
        weather_base[dbdate]['дата'] = query.daterus
        weather_base[dbdate]['влажность'] = query.humidity
        weather_base[dbdate]['ветер'] = query.wind
        weather_base[dbdate]['давление'] = query.pressure
        weather_base[dbdate]['date'] = query.day
        weather_base[dbdate]['picture'] = query.picture
    period_start = datetime.strptime(period_start, '%Y-%m-%d').date()
    period_end = datetime.strptime(period_end, '%Y-%m-%d').date()
    while period_start <= period_end:
        wb = weather_base[period_start]
        temp = wb['температура'].replace('\n', ' ')
        print(
            f"{wb['дата']}:,температура: {temp}, осадки: {wb['погода']}, ветер: {wb['ветер']}, "
            f"давление:{wb['давление']}, влажность:{wb['влажность']}")
        period_start += delta

    return weather_base
