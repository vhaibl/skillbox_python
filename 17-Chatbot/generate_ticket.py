from io import BytesIO

import requests
from PIL import Image, ImageFont, ImageDraw

TEMPLATE_PATH = 'files/template.png'
FONT_PATH = 'files/CoreSans.ttf'
FONT_SIZE = 14
BLACK = (0, 0, 0, 255)
FROM_OFFSET = (47, 200)
TO_OFFSET = (47, 266)
DATE_OFFSET = (287, 266)
NAME_OFFSET = (47, 135)
PHONE_OFFSET = (287, 135)
AVATAR_SIZE = 100
AVATAR_OFFSET = (430, 105)


def generate_ticket(city_from, city_to, flight_date, phone, name):
    base = Image.open(TEMPLATE_PATH).convert('RGBA')
    font = ImageFont.truetype(FONT_PATH, FONT_SIZE)
    draw = ImageDraw.Draw(base)

    draw.text(NAME_OFFSET, name, font=font, fill=BLACK)
    draw.text(FROM_OFFSET, city_from, font=font, fill=BLACK)
    draw.text(PHONE_OFFSET, phone, font=font, fill=BLACK)
    draw.text(DATE_OFFSET, flight_date, font=font, fill=BLACK)
    draw.text(TO_OFFSET, city_to, font=font, fill=BLACK)

    response = requests.get(url=f'https://api.adorable.io/avatars/{AVATAR_SIZE}/{phone}.png')
    avatar_file_like = BytesIO(response.content)
    avatar = Image.open(avatar_file_like)
    base.paste(avatar, AVATAR_OFFSET)

    temp_file = BytesIO()
    base.save(temp_file, 'png')
    temp_file.seek(0)

    return temp_file

# generate_ticket('Москва', 'Лондон', 'test', '22-06-2020', 'Василий')
