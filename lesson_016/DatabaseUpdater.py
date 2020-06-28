import sys
from datetime import datetime, timedelta

from playhouse.db_url import connect

import Postcards
import WeatherMaker
import models


class DatabaseUpdater:
    def __init__(self, period_start, period_end, db_url='sqlite:///weather.db'):
        self.database = connect(db_url)
        models.db.initialize(self.database)
        self.Weather = models.Weather
        self.Weather.create_table()
        self.period_start = datetime.strptime(period_start, '%Y-%m-%d').date()
        self.period_end = datetime.strptime(period_end, '%Y-%m-%d').date()
        self.delta = timedelta(days=1)

    def update_db(self):

        print("\nMODIFYING DB:", end='')
        delta = timedelta(days=1)
        p_start = self.period_start
        while p_start <= self.period_end:
            value = WeatherMaker.weather_base[p_start]
            create = self.Weather.get_or_create(day=value['date'],
                                                defaults={'daterus': value['дата'], 'temperature': value['температура'],
                                                          'condition': value['погода'], 'wind': value['ветер'],
                                                          'humidity': value['влажность'], 'pressure': value['давление'],
                                                          'picture': value['picture']})
            if create[1] is False:
                update = self.Weather.update(day=value['date'], daterus=value['дата'],
                                             temperature=value['температура'],
                                             condition=value['погода'],
                                             humidity=value['влажность'],
                                             pressure=value['давление'], picture=value['picture']).where(
                    self.Weather.id == create[0].id)
                update.execute()
                print('U', end='')
            else:
                print('C', end='')
            p_start += delta
        print(' Done')

    def show(self):
        for query in self.Weather.select().where(self.Weather.day.between(self.period_start, self.period_end)):
            print(query.daterus, query.temperature.replace('\n', ' '), query.condition, query.wind, query.humidity,
                  query.pressure)

    def read_db(self):
        weather_base = WeatherMaker.weather_base

        for query in self.Weather.select().where(self.Weather.day.between(self.period_start, self.period_end)):
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
        p_start = self.period_start
        while p_start <= self.period_end:
            wb = weather_base[p_start]

            temp = wb['температура'].replace('\n', ' ')
            print(
                f"{wb['дата']}:,температура: {temp}, осадки: {wb['погода']}, ветер: {wb['ветер']}, "
                f"давление:{wb['давление']}, влажность:{wb['влажность']}")
            p_start += self.delta

        return weather_base

    def make_postcards(self):
        count = 0

        print(self.period_start, self.period_end)
        for query in self.Weather.select().where(self.Weather.day.between(self.period_start, self.period_end)):
            postcard = Postcards.Postcards(query.daterus, query.temperature, query.condition, query.wind,
                                           query.humidity,
                                           query.pressure, query.picture, query.day)
            postcard.draw_postcard()
            count += 1
            print("\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b", end="")
            print('Creating postcards: {0:3}'.format(count), end='')
            sys.stdout.flush()
        print('\nPostcards created at \\images folder')
