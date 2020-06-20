import re
from calendar import calendar
from collections import defaultdict
from pprint import pprint

import numpy as np
from bs4 import BeautifulSoup
import requests
import cv2
from PIL import ImageFont, ImageDraw, Image

weatherbase = {}

months = 'january', 'february', 'march', 'april', 'may', 'june'  # , 'july', 'august', 'september', 'october', 'november', 'december'


class GetWeather:
    def __init__(self, month, year, weatherbase):
        self.weatherbase = weatherbase
        self.month = month
        self.year = year

    def get_weather(self):
        descriptions = []
        day_temps = []
        humids = []
        winds = []
        pressures = []
        if self.year not in self.weatherbase:
            self.weatherbase[self.year] = {}
        if self.month not in self.weatherbase[self.year]:
            weatherbase[self.year][self.month] = {}
        response = requests.get(f'https://pogoda.mail.ru/prognoz/moskva/{self.month}-{self.year}/')
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
                # day_temps.append(day.replace('+', ' +'))

            for dates, daytemp, desc, humid, wind, pressure in zip(list_of_dates, day_temps, descriptions, humids,
                                                                   winds,
                                                                   pressures):
                short_month = self.weatherbase[self.year][self.month]

                if dates.text[:2] == 'Се':
                    short_month[int(dates.text[8:10])] = {}
                    short_month[int(dates.text[8:10])]['температура'] = daytemp
                    short_month[int(dates.text[8:10])]['погода'] = desc
                    short_month[int(dates.text[8:10])]['дата'] = ''.join(dates.text)
                    short_month[int(dates.text[8:10])]['влажность'] = humid
                    short_month[int(dates.text[8:10])]['ветер'] = wind
                    short_month[int(dates.text[8:10])]['давление'] = pressure

                else:
                    short_month[int(dates.text[:2])] = {}
                    short_month[int(dates.text[:2])]['температура'] = daytemp
                    short_month[int(dates.text[:2])]['погода'] = desc
                    short_month[int(dates.text[:2])]['дата'] = dates.text
                    short_month[int(dates.text[:2])]['влажность'] = humid
                    short_month[int(dates.text[:2])]['ветер'] = wind
                    short_month[int(dates.text[:2])]['давление'] = pressure
                if dates.text[:2] != 'Се':
                    if 'ясно' in short_month[int(dates.text[:2])]['погода']:
                        short_month[int(dates.text[:2])][
                            'picture'] = 'python_snippets\\external_data\\weather_img\\sun.jpg'
                    elif 'облачно' in short_month[int(dates.text[:2])]['погода']:
                        short_month[int(dates.text[:2])][
                            'picture'] = 'python_snippets\\external_data\\weather_img\\cloud.jpg'
                    elif 'снег' in short_month[int(dates.text[:2])]['погода']:
                        short_month[int(dates.text[:2])][
                            'picture'] = 'python_snippets\\external_data\\weather_img\\snow.jpg'
                    else:
                        short_month[int(dates.text[:2])][
                            'picture'] = 'python_snippets\\external_data\\weather_img\\rain.jpg'
                else:
                    if 'ясно' in short_month[int(dates.text[8:10])]['погода']:
                        short_month[int(dates.text[8:10])][
                            'picture'] = 'python_snippets\\external_data\\weather_img\\sun.jpg'
                    elif 'облачно' in short_month[int(dates.text[8:10])]['погода']:
                        short_month[int(dates.text[8:10])][
                            'picture'] = 'python_snippets\\external_data\\weather_img\\cloud.jpg'
                    elif 'снег' in short_month[int(dates.text[8:10])]['погода']:
                        short_month[int(dates.text[8:10])][
                            'picture'] = 'python_snippets\\external_data\\weather_img\\snow.jpg'
                    else:
                        short_month[int(dates.text[8:10])][
                            'picture'] = 'python_snippets\\external_data\\weather_img\\rain.jpg'

        else:
            print(response.status_code)


def viewImage(image, name_of_window):
    cv2.namedWindow(name_of_window, cv2.WINDOW_AUTOSIZE)
    cv2.imshow(name_of_window, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def make_postcard(selected):
    date = selected['дата']
    wind = selected['ветер']
    humid = selected['влажность']
    pressure = selected['давление']
    weather = selected['погода']
    temperature = selected['температура']
    picture = selected['picture']
    # global cv2_im_processed
    image = cv2.imread('python_snippets\\external_data\\probe.jpg')

    for y in range(255):
        weather_background = {'снег': (255, 255, y), 'ясно': (y, 255, 255), 'облачно': (y + 64, y + 64, y + 64),
                              'дождь': (255, y, y), 'дождь/гроза': (192, y - 64, y - 64)}
        if weather in weather_background:
            weather_state = weather_background[weather]
        else:
            weather_state = (y + 64, y + 64, y + 64)
        cv2.line(image, (0, y), (512, y), color=weather_state)
    cv2_im_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    pil_im = Image.fromarray(cv2_im_rgb)
    draw = ImageDraw.Draw(pil_im)
    font = ImageFont.truetype("python_snippets\\external_data\\fonts\\Aller Cyrillic.ttf", 26)
    font_date = ImageFont.truetype("python_snippets\\external_data\\fonts\\Aller Cyrillic.ttf", 32)
    font_temp = ImageFont.truetype("python_snippets\\external_data\\fonts\\Aller Cyrillic.ttf", 36)
    draw.text((200, 20), date, font=font_date, fill=(0, 0, 0))
    draw.text((260, 60), weather, font=font, fill=(0, 0, 0))
    draw.text((40, 132), temperature, font=font_temp, fill=(0, 0, 0))
    draw.text((270, 130), f'Влажность: {humid}', font=font, fill=(0, 0, 0))
    draw.text((270, 160), f'Давление: {pressure}', font=font, fill=(0, 0, 0))
    draw.text((270, 190), f'Ветер: {wind}', font=font, fill=(0, 0, 0))
    cv2_im_processed = cv2.cvtColor(np.array(pil_im), cv2.COLOR_RGB2BGR)
    s_img = cv2.imread(picture)
    x_offset = 48
    y_offset = 10
    cv2_im_processed[y_offset:y_offset + s_img.shape[0], x_offset:x_offset + s_img.shape[1]] = s_img

    return cv2_im_processed


for month in months:
    gw = GetWeather(month=month, year='2020', weatherbase=weatherbase)
    gw.get_weather()

selected = weatherbase['2020']['june'][21]
viewImage(make_postcard(selected=selected), 'Weather')
