import datetime
import re

import requests
from bs4 import BeautifulSoup

weather_base = {}
MONTHS_DICT2 = {1: 'january', 2: 'february', 3: 'march', 4: 'april', 5: 'may', 6: 'june', 7: 'july',
                8: 'august', 9: 'september', 10: 'october', 11: 'november', 12: 'december'}


class GetWeather:
    def __init__(self, years, months, period_start):
        self.weather_base = weather_base
        self.years = years
        self.months = months
        self.period_start = period_start

        self.ICON_PATHS = {'sun': 'python_snippets\\external_data\\weather_img\\sun.jpg',
                           'cloud': 'python_snippets\\external_data\\weather_img\\cloud.jpg',
                           'snow': 'python_snippets\\external_data\\weather_img\\snow.jpg',
                           'rain': 'python_snippets\\external_data\\weather_img\\rain.jpg'}

        self.MONTHS_DICT = {'january': '01', 'february': '02', 'march': '03', 'april': '04', 'may': '05', 'june': '06',
                            'july': '07',
                            'august': '08', 'september': '09', 'october': '10', 'november': '11', 'december': '12'}

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
                        form_day = datetime.date(year=int(yrs), month=int(self.MONTHS_DICT[mnth]),
                                                 day=int(dates.text[8:10]))
                    else:
                        form_day = datetime.date(year=int(yrs), month=int(self.MONTHS_DICT[mnth]),
                                                 day=int(dates.text[:2]))
                    dateconv = datetime.date(int(yrs), int(self.MONTHS_DICT[mnth]), int(form_day.day))
                    self.weather_base[form_day] = {}
                    self.weather_base[form_day]['температура'] = daytemp
                    self.weather_base[form_day]['погода'] = desc
                    self.weather_base[form_day]['дата'] = dates.text
                    self.weather_base[form_day]['влажность'] = humid
                    self.weather_base[form_day]['ветер'] = wind
                    self.weather_base[form_day]['давление'] = pressure
                    self.weather_base[form_day]['date'] = str(dateconv)
                    if 'ясно' in self.weather_base[form_day]['погода']:
                        self.weather_base[form_day]['picture'] = self.ICON_PATHS['sun']
                    elif 'облачно' in self.weather_base[form_day]['погода']:
                        self.weather_base[form_day]['picture'] = self.ICON_PATHS['cloud']
                    elif 'снег' in self.weather_base[form_day]['погода']:
                        self.weather_base[form_day]['picture'] = self.ICON_PATHS['snow']
                    else:
                        self.weather_base[form_day]['picture'] = self.ICON_PATHS['rain']

            else:
                raise RuntimeError('error', response.status_code)


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
            if MONTHS_DICT2[period_start1.month] not in self.months:
                self.months.append((MONTHS_DICT2[period_start1.month], period_start1.year))
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
            if MONTHS_DICT2[period_start1.month] not in self.months:
                self.months.append((MONTHS_DICT2[period_start1.month], period_start1.year))
            period_start1 += self.delta_month
        gw = GetWeather(months=self.months, years=self.years, period_start=period_start)
        gw.run()
        p_start = period_start
        while p_start <= period_end:
            wb = weather_base[p_start]
            print(f'Прогноз за {wb["дата"]} загружен')
            p_start += self.delta
        return weather_base
