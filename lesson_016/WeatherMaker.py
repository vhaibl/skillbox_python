import datetime
import re

import requests
from bs4 import BeautifulSoup

monthsdict = {'january': '01', 'february': '02', 'march': '03', 'april': '04', 'may': '05', 'june': '06', 'july': '07',
              'august': '08', 'september': '09', 'october': '10', 'november': '11', 'december': '12'}


class GetWeather():
    def __init__(self, weatherbase, years, months, period_start):
        self.weatherbase = weatherbase
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

                for dates, daytemp, desc, humid, wind, pressure in zip(list_of_dates, day_temps, descriptions,
                                                                       humids, winds, pressures):
                    today = dates.text[8:10]
                    day = dates.text[:2]

                    if dates.text[:2] == 'Се':
                        form_today = datetime.date(year=int(yrs), month=int(monthsdict[mnth]), day=int(today))

                        self.weatherbase[form_today] = {}
                        self.weatherbase[form_today]['температура'] = daytemp
                        self.weatherbase[form_today]['погода'] = desc
                        self.weatherbase[form_today]['дата'] = ''.join(dates.text)
                        self.weatherbase[form_today]['влажность'] = humid
                        self.weatherbase[form_today]['ветер'] = wind
                        self.weatherbase[form_today]['давление'] = pressure
                        self.weatherbase[form_today]['date'] = datetime.date.today()
                        if 'ясно' in self.weatherbase[form_today]['погода']:
                            self.weatherbase[form_today][
                                'picture'] = 'python_snippets\\external_data\\weather_img\\sun.jpg'
                        elif 'облачно' in self.weatherbase[form_today]['погода']:
                            self.weatherbase[form_today][
                                'picture'] = 'python_snippets\\external_data\\weather_img\\cloud.jpg'
                        elif 'снег' in self.weatherbase[form_today]['погода']:
                            self.weatherbase[form_today][
                                'picture'] = 'python_snippets\\external_data\\weather_img\\snow.jpg'
                        else:
                            self.weatherbase[form_today][
                                'picture'] = 'python_snippets\\external_data\\weather_img\\rain.jpg'
                    else:
                        form_day = datetime.date(year=int(yrs), month=int(monthsdict[mnth]),
                                                 day=int(dates.text[:2]))
                        dateconv = datetime.date(int(yrs), int(monthsdict[mnth]), int(dates.text[:2]))
                        self.weatherbase[form_day] = {}
                        self.weatherbase[form_day]['температура'] = daytemp
                        self.weatherbase[form_day]['погода'] = desc
                        self.weatherbase[form_day]['дата'] = dates.text
                        self.weatherbase[form_day]['влажность'] = humid
                        self.weatherbase[form_day]['ветер'] = wind
                        self.weatherbase[form_day]['давление'] = pressure
                        self.weatherbase[form_day]['date'] = str(dateconv)
                        if 'ясно' in self.weatherbase[form_day]['погода']:
                            self.weatherbase[form_day][
                                'picture'] = 'python_snippets\\external_data\\weather_img\\sun.jpg'
                        elif 'облачно' in self.weatherbase[form_day]['погода']:
                            self.weatherbase[form_day][
                                'picture'] = 'python_snippets\\external_data\\weather_img\\cloud.jpg'
                        elif 'снег' in self.weatherbase[form_day]['погода']:
                            self.weatherbase[form_day][
                                'picture'] = 'python_snippets\\external_data\\weather_img\\snow.jpg'
                        else:
                            self.weatherbase[form_day][
                                'picture'] = 'python_snippets\\external_data\\weather_img\\rain.jpg'

            else:
                raise RuntimeError(response.status_code)
                # break
