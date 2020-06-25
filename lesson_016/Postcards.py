import datetime
import sys

import cv2
import numpy as np
from PIL import ImageDraw, ImageFont, Image
# TODO Попробуйте обойтись совсем без PIL
# TODO для русских букв в openCV используйте шрифт cv2.FONT_HERSHEY_COMPLEX
from models import Weather


# TODO Сами эти функции надо тоже обернуть в класс
# TODO Пути и словари вынести в атрибуты
def draw_postcard(daterus, temperature, condition, wind, humidity, pressure, picture, day):
    image = cv2.imread('python_snippets\\external_data\\probe.jpg')
    # TODO Градиент тоже хорошо бы отдельным методом сделать
    for y in range(255):
        weather_background = {'снег': (255, 255, y), 'ясно': (y, 255, 255), 'облачно': (y + 64, y + 64, y + 64),
                              'дождь': (255, y, y), 'дождь/гроза': (192, y - 64, y - 64)}
        if condition in weather_background:
            weather_state = weather_background[condition]
        else:
            weather_state = (y + 64, y + 64, y + 64)
        cv2.line(image, (0, y), (512, y), color=weather_state)
    cv2_im_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    pil_im = Image.fromarray(cv2_im_rgb)
    draw = ImageDraw.Draw(pil_im)
    font = ImageFont.truetype("python_snippets\\external_data\\fonts\\Aller Cyrillic.ttf", 26)
    font_date = ImageFont.truetype("python_snippets\\external_data\\fonts\\Aller Cyrillic.ttf", 32)
    font_temp = ImageFont.truetype("python_snippets\\external_data\\fonts\\Aller Cyrillic.ttf", 36)
    draw.text((200, 20), daterus, font=font_date, fill=(0, 0, 0))
    draw.text((260, 60), condition, font=font, fill=(0, 0, 0))
    draw.text((40, 132), temperature, font=font_temp, fill=(0, 0, 0))
    draw.text((270, 130), f'Влажность: {humidity}', font=font, fill=(0, 0, 0))
    draw.text((270, 160), f'Давление: {pressure}', font=font, fill=(0, 0, 0))
    draw.text((270, 190), f'Ветер: {wind}', font=font, fill=(0, 0, 0))
    cv2_im_processed = cv2.cvtColor(np.array(pil_im), cv2.COLOR_RGB2BGR)
    s_img = cv2.imread(picture)
    x_offset = 48
    y_offset = 10
    cv2_im_processed[y_offset:y_offset + s_img.shape[0], x_offset:x_offset + s_img.shape[1]] = s_img
    image_path = f'images/{day}.jpg'
    cv2.imwrite(image_path, cv2_im_processed, [int(cv2.IMWRITE_JPEG_QUALITY), 90])
    # TODO хорошо бы проверить, есть ли папка images и создать её при необходимости
    return cv2_im_processed


def make_postcards(period_start, period_end):
    count = 0
    # TODO Всю работу с базой - реализовать в классе, который этим должен заниматься
    # TODO Здесь оставить просто метод, который по указанному прогнозу делает карточку
    # TODO Вообще всё управление надо собирать в одном классе-менеджере
    # TODO Который будет принимать класс для работы с изображениями, класс для работы с базами данных
    # TODO И получив ввод пользователя этот класс будет тащить информацию из базы при помощи методов
    # TODO соответственного класса.
    # TODO Далее менеджер передает данные в методы класса с картинками и делает открытки.
    for query in Weather.select().where(Weather.day.between(period_start, period_end)):
        draw_postcard(query.daterus, query.temperature, query.condition, query.wind, query.humidity, query.pressure,
                      query.picture, query.day)
        count += 1
        print("\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b", end="")
        print('Creating postcards: {0:3}'.format(count), end='')
        # TODO нужно указывать путь к созданным открыткам
        sys.stdout.flush()


def postcards(period_start, period_end):
    count = 0
    period_start = datetime.datetime.strptime(period_start, '%Y-%m-%d').date()
    period_end = datetime.datetime.strptime(period_end, '%Y-%m-%d').date()
    history = Weather.select().where(Weather.day.between(period_start, period_end))
    print("\n")
    for query in history:
        draw_postcard(query.daterus, query.temperature, query.condition, query.wind, query.humidity, query.pressure,
                      query.picture, query.day)


def viewImage(image, name_of_window):
    cv2.namedWindow(name_of_window, cv2.WINDOW_AUTOSIZE)
    cv2.imshow(name_of_window, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
