import re

re_moscow = re.compile(r'[Мм][Оо][Сс][кк][Вв]')
re_london = re.compile(r'[Лл][Оо][Нн][Дд][Оо][Нн]')
re_paris = re.compile(r'[Пп][Аа][Рр][Ии][Жж]')
re_flight = re.compile(r'^\d{3}$')
re_quantity = re.compile(r'^[1-5]$')
re_yes = re.compile(r'^[Дд][аА]$')
re_no = re.compile(r'^[Нн][Ее][Тт]$')
re_date = re.compile(r"[\d]{1,2}-[\d]{1,2}-[\d]{4}")
re_phone = re.compile(r'^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$')
from datetime import timedelta, date, datetime
from pprint import pprint
from random import randint


def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)


def handler_from(text, context):
    # match = re.match(re_name, text)
    # if match:
    context['same'] = None
    context['confirm'] = 'Yes'
    paris = re.findall(re_paris, text)
    london = re.findall(re_london, text)
    moscow = re.findall(re_moscow, text)
    if paris:
        context['city_from'] = 'Париж'
        return True
    if london:
        context['city_from'] = 'Лондон'
        return True
    if moscow:
        context['city_from'] = 'Москва'
        return True
    else:
        return False


def handler_to(text, context):
    paris = re.match(re_paris, text)
    london = re.match(re_london, text)
    moscow = re.match(re_moscow, text)
    if paris:
        context['city_to'] = 'Париж'
    elif london:
        context['city_to'] = 'Лондон'
    elif moscow:
        context['city_to'] = 'Москва'
    else:
        return False

    if context['city_to'] == context['city_from']:
        context['same'] = 'одинаковые города'
        return False

    elif context['city_from'] == 'Париж' and context['city_to'] == 'Москва':
        context['same'] = 'нет прямых рейсов'
        return False

    elif context['city_from'] == 'Москва' and context['city_to'] == 'Париж':
        context['same'] = 'нет прямых рейсов'
        return False

    else:
        return True


matches = []


def handler_date(text, context):
    global flights
    match = re.search(re_date, text)
    current_date = date.today()
    start_date = datetime.strptime(text, '%d-%m-%Y').date()

    if match and start_date >= current_date:
        try:

            end_date = start_date + timedelta(days=365)

            flights = {'Москва': {'Лондон': {}}, 'Лондон': {'Москва': {}, 'Париж': {}}, 'Париж': {'Лондон': {}}}
            for single_date in daterange(start_date, end_date):

                if single_date.isoweekday() == 1 or single_date.isoweekday() == 3:
                    if len(flights['Москва']['Лондон']) < 5:
                        tour = str((randint(100, 999)))
                        add_date = single_date.strftime("%d-%m-%Y")
                        flights['Москва']['Лондон'][tour] = add_date

                if single_date.isoweekday() == 2 or single_date.isoweekday() == 4:
                    if len(flights['Лондон']['Москва']) < 5:
                        tour = str((randint(100, 999)))
                        add_date = single_date.strftime("%d-%m-%Y")
                        flights['Лондон']['Москва'][tour] = add_date

                if single_date.day == 10 or single_date.day == 20:
                    if len(flights['Лондон']['Париж']) < 5:
                        tour = str((randint(100, 999)))
                        add_date = single_date.strftime("%d-%m-%Y")
                        flights['Лондон']['Париж'][tour] = add_date

                if single_date.day == 11 or single_date.day == 21:
                    x = 0
                    if len(flights['Париж']['Лондон']) < 5:
                        tour = str((randint(100, 999)))
                        add_date = single_date.strftime("%d-%m-%Y")
                        flights['Париж']['Лондон'][tour] = add_date
                        x += 1
            context['date'] = text
            context['list'] = ''

            for i, v in flights[context['city_from']][context['city_to']].items():
                context['list'] += (f"Рейс {i} - Дата {v}\n")
            return True
        except Exception as esc:
            print(esc)
            return False

    else:
        return False

def handler_flight(text, context):
    match = re.match(re_flight, text)
    if match:
        if text in flights[context['city_from']][context['city_to']].keys():
            context['flight'] = text
            context['flight_date'] = flights[context['city_from']][context['city_to']][text]

            return True
        else:
            return False
    else:
        return False


def handler_quantity(text, context):
    match = re.match(re_quantity, text)
    if match:
        context['quantity'] = text
        return True
    else:
        return False

def handler_comment(text, context):

    context['comment'] = text

    return True

def handler_confirm(text, context):
    yes = re.match(re_yes, text)
    no = re.match(re_no, text)
    if yes:
        print("match yes")
        context['confirm'] = 'Yes'
        return True
    elif no:
        print('match no')
        context['confirm'] = 'No'
        return True
    else:
        return False

def handler_phone(text, context):
    match = re.match(re_phone, text)
    if match:
        context['phone'] = text
        return True
    else:
        return False
