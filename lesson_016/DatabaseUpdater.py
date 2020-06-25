from datetime import datetime, timedelta, date

from models import Weather

# TODO Тоже обернуть в класс всё, добавить инициализацию БД по db_url
# TODO Вынести всё нужное в атрибуты классы
def update_db(weatherbase, period_start, period_end):
    # gw = GetWeather(weatherbase, months=months, years=years)
    # gw.run()
    period_start = datetime.strptime(period_start, '%Y-%m-%d').date()
    period_end = datetime.strptime(period_end, '%Y-%m-%d').date()

    print("\nMODIFYING DB:", end='')
    delta = timedelta(days=1)
    # TODO Для обновления попробуйте воспользоваться get_or_create методом
    while period_start <= period_end:
        value = weatherbase[period_start]
        if Weather.select().where(Weather.day == value['date']):
            print('X', end='')
        else:
            value['date'] = Weather(day=value['date'], daterus=value['дата'], temperature=value['температура'],
                                    condition=value['погода'], wind=value['ветер'], humidity=value['влажность'],
                                    pressure=value['давление'], picture=value['picture'])
            value['date'].save()
            print('O', end='')
        period_start += delta
    print(' Done')


def show(period_start, period_end):
    for query in Weather.select().where(Weather.day.between(period_start, period_end)):
        print(query.daterus, query.temperature.replace('\n', ' '), query.condition, query.wind, query.humidity,
              query.pressure)


def check_for_update():
    for zxc in Weather.select().where(Weather.daterus.contains('Сегодня')):
        if str(zxc.day) == str(date.today()):
            print(('DB UPDATED'))  # TODO лишние скобки
            pass
        else:
            print('UPDATING DB')
            update_db()


def read_db(period_start, period_end):
    weatherbase = {}
    delta = timedelta(days=1)

    for query in Weather.select().where(Weather.day.between(period_start, period_end)):
        dbdate = datetime.strptime(query.day, '%Y-%m-%d').date()

        weatherbase[dbdate] = {}
        weatherbase[dbdate]['температура'] = query.temperature
        # print(weatherbase[dbdate]['температура'],1)
        weatherbase[dbdate]['погода'] = query.condition
        weatherbase[dbdate]['дата'] = query.daterus
        weatherbase[dbdate]['влажность'] = query.humidity
        weatherbase[dbdate]['ветер'] = query.wind
        weatherbase[dbdate]['давление'] = query.pressure
        weatherbase[dbdate]['date'] = query.day
        weatherbase[dbdate]['picture'] = query.picture
    period_start = datetime.strptime(period_start, '%Y-%m-%d').date()
    period_end = datetime.strptime(period_end, '%Y-%m-%d').date()
    while period_start <= period_end:
        print(period_start, period_start)
        wb = weatherbase[period_start]
        temp = wb['температура'].replace('\n', ' ')
        print(
            f"{wb['дата']}:,температура: {temp}, осадки: {wb['погода']}, ветер: {wb['ветер']}, "
            f"давление:{wb['давление']}, влажность:{wb['влажность']}")
        # print(f'Прогноз за {wb["дата"]} загружен')
        period_start += delta

    return weatherbase
    # print (weatherbase)
