from datetime import datetime, timedelta, date

from models import Weather


def update_db(weatherbase, period_start, period_end):
    # gw = GetWeather(weatherbase, months=months, years=years)
    # gw.run()
    period_start = datetime.strptime(period_start, '%Y-%m-%d').date()
    period_end = datetime.strptime(period_end, '%Y-%m-%d').date()

    print("\nMODIFYING DB:", end='')
    delta = timedelta(days=1)

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
            print(('DB UPDATED'))
            pass
        else:
            print('UPDATING DB')
            update_db()

