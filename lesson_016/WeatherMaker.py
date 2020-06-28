import datetime
import re

import requests
from bs4 import BeautifulSoup
# TODO Если эти переменные являются константами - то их надо писать с заглавной буквы
# TODO Если же они используются только в одном классе - то их надо внести в атрибуты этого класса
months_dict = {'january': '01', 'february': '02', 'march': '03', 'april': '04', 'may': '05', 'june': '06', 'july': '07',
               'august': '08', 'september': '09', 'october': '10', 'november': '11', 'december': '12'}
icon_paths = {'sun': 'python_snippets\\external_data\\weather_img\\sun.jpg',
              'cloud': 'python_snippets\\external_data\\weather_img\\cloud.jpg',
              'snow': 'python_snippets\\external_data\\weather_img\\snow.jpg',
              'rain': 'python_snippets\\external_data\\weather_img\\rain.jpg'
              }
monthsdict2 = {1: 'january', 2: 'february', 3: 'march', 4: 'april', 5: 'may', 6: 'june', 7: 'july', 8: 'august',
               9: 'september', 10: 'october', 11: 'november', 12: 'december'}
weather_base = {}


class GetWeather:
    def __init__(self, years, months, period_start):
        self.weather_base = weather_base
        self.years = years
        self.months = months
        self.period_start = period_start

    def run(self):
        try:
            self.get_weather()

        except Exception as esc:
            print(esc)

    def get_weather(self):
        for mnth, yrs in self.months:
            descriptions = []
            day_temps = []
            humids = []
            winds = []
            pressures = []
            response = requests.get(f'https://pogoda.mail.ru/prognoz/moskva/{mnth}-{yrs}/')
            print(f'Parsing {mnth} {yrs}')
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, features='html.parser')
                list_of_dates = soup.find_all('div', {'class': 'day__date'})
                list_of_temp_day = soup.find_all('div', {'class': 'day__temperature'})
                list_of_desc = soup.find_all('div', {'class': 'day__description'})
                list_of_humid = soup.find_all('span', {'title': re.compile('Влажность:')})
                list_of_wind = soup.find_all('span', {'title': re.compile('Ветер:')})
                list_of_press = soup.find_all('span', {'title': re.compile('Давление:')})
                for desc in list_of_desc: descriptions.append((''.join(desc.text.split())))
                for humid in list_of_humid: humids.append((''.join(humid.text.split())))
                for wind in list_of_wind: winds.append((' '.join(wind.text.split())))
                for pressure in list_of_press: pressures.append((' '.join(pressure.text.split())))
                for day in list_of_temp_day:
                    day = '\nНочью '.join(day.text.split())
                    day_temps.append(f'Днем {day}')

                for dates, daytemp, desc, humid, wind, pressure in zip(list_of_dates, day_temps, descriptions, humids,
                                                                       winds, pressures):
                    if dates.text[:2] == 'Се':
                        form_day = datetime.date(year=int(yrs), month=int(months_dict[mnth]), day=int(dates.text[8:10]))
                    else:
                        form_day = datetime.date(year=int(yrs), month=int(months_dict[mnth]), day=int(dates.text[:2]))
                    dateconv = datetime.date(int(yrs), int(months_dict[mnth]), int(form_day.day))
                    self.weather_base[form_day] = {}
                    self.weather_base[form_day]['температура'] = daytemp
                    self.weather_base[form_day]['погода'] = desc
                    self.weather_base[form_day]['дата'] = dates.text
                    self.weather_base[form_day]['влажность'] = humid
                    self.weather_base[form_day]['ветер'] = wind
                    self.weather_base[form_day]['давление'] = pressure
                    self.weather_base[form_day]['date'] = str(dateconv)
                    if 'ясно' in self.weather_base[form_day]['погода']:
                        self.weather_base[form_day]['picture'] = icon_paths['sun']
                    elif 'облачно' in self.weather_base[form_day]['погода']:
                        self.weather_base[form_day]['picture'] = icon_paths['cloud']
                    elif 'снег' in self.weather_base[form_day]['погода']:
                        self.weather_base[form_day]['picture'] = icon_paths['snow']
                    else:
                        self.weather_base[form_day]['picture'] = icon_paths['rain']

            else:
                raise RuntimeError('error', response.status_code)
                # break
                # TODO Лишняя строка?


class MakeWeather:
    def __init__(self):
        self.months = []
        self.years = []
        self.delta_month = datetime.timedelta(weeks=4)
        self.delta = datetime.timedelta(days=1)
        self.delta_week = datetime.timedelta(days=7)

    def on_run(self):
        period_end = datetime.datetime.now()
        period_start = period_end - self.delta_week
        period_start1 = period_start

        while period_start1 <= period_end + datetime.timedelta(days=30):
            if monthsdict2[period_start1.month] not in self.months:
                self.months.append((monthsdict2[period_start1.month], period_start1.year))
            period_start1 += self.delta_month

        gw = GetWeather(months=self.months, years=self.years, period_start=period_start)
        gw.run()
        while period_start <= period_end:
            wb = weather_base[period_start.date()]
            temp = wb['температура'].replace('\n', ' ')
            print(
                f"{wb['дата']}:,температура: {temp}, осадки: {wb['погода']}, ветер: {wb['ветер']}, "
                f"давление:{wb['давление']}, влажность:{wb['влажность']}")
            period_start += self.delta

    def write_to_dict(self, period_start, period_end):
        period_start = datetime.datetime.strptime(period_start, '%Y-%m-%d').date()
        period_start1 = period_start
        period_end = datetime.datetime.strptime(period_end, '%Y-%m-%d').date()

        while period_start1 <= period_end + datetime.timedelta(days=30):
            if monthsdict2[period_start1.month] not in self.months:
                self.months.append((monthsdict2[period_start1.month], period_start1.year))
            period_start1 += self.delta_month
        period_start1 = period_start  # TODO Тут и ниже 2 переменные, которые не используются?
        # TODO Нужно убрать
        gw = GetWeather(months=self.months, years=self.years, period_start=period_start)
        gw.run()
        p_start = period_start
        while p_start <= period_end:
            wb = weather_base[p_start]
            print(f'Прогноз за {wb["дата"]} загружен')
            p_start += self.delta
        p_start = period_start
        return weather_base
