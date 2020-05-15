# -*- coding: utf-8 -*-


# Заполнить все поля в билете на самолет.
# Создать функцию, принимающую параметры: ФИО, откуда, куда, дата вылета,
# и заполняющую ими шаблон билета Skillbox Airline.
# Шаблон взять в файле lesson_013/images/ticket_template.png
# Пример заполнения lesson_013/images/ticket_sample.png
# Подходящий шрифт искать на сайте ofont.ru
import argparse
import os
from PIL import Image, ImageDraw, ImageFont, ImageColor


def make_ticket(fio, from_, to, date, template=None, font_path=None, out_path=None):
    template = os.path.join("images", "ticket_template.png") if template is None else template
    im = Image.open(template)
    draw = ImageDraw.Draw(im)
    if font_path is None:
        font_path = os.path.join("fonts", "ofont.ru_Core Sans.ttf")
    else:
        font_path = font_path
    font = ImageFont.truetype(font_path, size=14)
    y = im.size[1] - 260 - font.size
    message = fio
    draw.text((47, y), message, font=font, fill=ImageColor.colormap['black'])

    y = im.size[1] - 260 + (font.size) * 4
    message = from_
    draw.text((47, y), message, font=font, fill=ImageColor.colormap['black'])

    y = im.size[1] - 260 + (font.size + 1) * 8 + 2
    message = to
    draw.text((47, y), message, font=font, fill=ImageColor.colormap['black'])

    y = im.size[1] - 260 + (font.size + 1) * 8 + 2
    message = date
    draw.text((287, y), message, font=font, fill=ImageColor.colormap['black'])

    out_path = out_path if out_path else 'probe.png'
    im.save(out_path)
    print(f'Ticked saved as {out_path}')


parser = argparse.ArgumentParser(description='Videos to images')
parser.add_argument('fio', type=str, help='ФИО')
parser.add_argument('from_', type=str, help='Откуда')
parser.add_argument('to', type=str, help='Куда')
parser.add_argument('date', type=str, help='Когда')
parser.add_argument('--out_path', type=str, default='qqq1.png', help='Путь ')
args = parser.parse_args()

make_ticket(fio=args.fio, from_=args.from_, to=args.to, date=args.date, out_path=args.out_path)

# Использование в консоли; 01_ticket.py "NAME SURNAME" FROM TO DATE --out_path PATH

# Усложненное задание (делать по желанию).
# Написать консольный скрипт c помощью встроенного python-модуля argparse.
# Скрипт должен принимать параметры:
#   --fio - обязательный, фамилия.
#   --from - обязательный, откуда летим.
#   --to - обязательный, куда летим.
#   --date - обязательный, когда летим.
#   --save_to - необязательный, путь для сохранения заполненнего билета.
# и заполнять билет.
#зачет!