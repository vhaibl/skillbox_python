import re

# re_name = re.compile(r'^[\w\-\s]{3,40}$')
re_moscow = re.compile(r'[Мм][Оо][Сс][кк][Вв]')
re_london = re.compile(r'[Лл][Оо][Нн][Дд][Оо][Нн]')
re_paris = re.compile(r'[Пп][Аа][Рр][Ии][Жж]')
# re_date = re.compile(r'(\b^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)\b')
re_date = re.compile(r"[\d]{1,2}-[\d]{1,2}-[\d]{4}")

from datetime import timedelta, date, datetime
from pprint import pprint
from random import randint


def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)


def handler_from(text, context):
    # match = re.match(re_name, text)
    # if match:
    paris = re.match(re_paris, text)
    london = re.match(re_london, text)
    moscow = re.match(re_moscow, text)
    if paris:
        context['from'] = 'париж'
        return True
    if london:
        context['from'] = 'лондон'
        return True
    if moscow:
        context['from'] = 'москва'
        return True
    else:
        return False


def handler_to(text, context):
    paris = re.match(re_paris, text)
    london = re.match(re_london, text)
    moscow = re.match(re_moscow, text)
    if paris:
        context['to'] = 'париж'
    elif london:
        context['to'] = 'лондон'
    elif moscow:
        context['to'] = 'москва'
    else:
        return False

    if context['to'] == context['from']:
        print('одинаковые города')
        check = True
        return False

    elif context['from'] == 'париж' and context['to'] == 'москва':
        print('нет прямых рейсов')
        return False

    elif context['from'] == 'москва' and context['to'] == 'париж':
        print('нет прямых рейсов')
        return False

    else:
        return True


matches = []


def handler_date(text, context):
    global testdict

    start_date = datetime.strptime(text, '%d-%m-%Y').date()
    end_date = start_date + timedelta(days=365)

    testdict = {'москва': {'лондон': {}}, 'лондон': {'москва': {}, 'париж': {}}, 'париж': {'лондон': {}}}

    for single_date in daterange(start_date, end_date):

        if single_date.isoweekday() == 1 or single_date.isoweekday() == 3:
            if len(testdict['москва']['лондон']) <= 5:
                tour = (randint(100, 999))
                add_date = single_date.strftime("%d-%m-%Y")
                testdict['москва']['лондон'][tour] = add_date

        if single_date.isoweekday() == 2 or single_date.isoweekday() == 4:
            if len(testdict['лондон']['москва']) <= 5:
                tour = (randint(100, 999))
                add_date = single_date.strftime("%d-%m-%Y")
                testdict['лондон']['москва'][tour] = add_date

        if single_date.day == 10 or single_date.day == 20:
            if len(testdict['лондон']['париж']) <= 5:
                tour = (randint(100, 999))
                add_date = single_date.strftime("%d-%m-%Y")
                testdict['лондон']['париж'][tour] = add_date

        if single_date.day == 11 or single_date.day == 21:
            x = 0
            if len(testdict['париж']['лондон']) <= 5:
                tour = (randint(100, 999))
                add_date = single_date.strftime("%d-%m-%Y")
                testdict['париж']['лондон'][tour] = add_date
                x += 1

    match = re.search(re_date, text)

    if match:
        try:
            context['date'] = text
            context['list'] = testdict[context['from']][context['to']]
            return True
        except Exception as esc:
            print(esc)
            return False

    else:
        return False
