import datetime
import re

import requests
from bs4 import BeautifulSoup

months_dict = {'january': '01', 'february': '02', 'march': '03', 'april': '04', 'may': '05', 'june': '06', 'july': '07',
               'august': '08', 'september': '09', 'october': '10', 'november': '11', 'december': '12'}
icon_paths = {'sun': 'python_snippets\\external_data\\weather_img\\sun.jpg',
              'cloud': 'python_snippets\\external_data\\weather_img\\cloud.jpg',
              'snow': 'python_snippets\\external_data\\weather_img\\snow.jpg',
              'rain': 'python_snippets\\external_data\\weather_img\\rain.jpg'
              }


class GetWeather:
    def __init__(self, weather_base, years, months, period_start):
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
