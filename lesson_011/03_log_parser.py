# -*- coding: utf-8 -*-

# На основе своего кода из lesson_009/02_log_parser.py напишите итератор (или генератор)
# котрый читает исходный файл events.txt и выдает число событий NOK за каждую минуту
# <время> <число повторений>
#
# пример использования:
#
# grouped_events = <создание итератора/генератора>  # Итератор или генератор? выбирайте что вам более понятно
# for group_time, event_count in grouped_events:
#     print(f'[{group_time}] {event_count}')
#
# на консоли должно появится что-то вроде
#
# [2018-05-17 01:57] 1234

def generate(file_name):
    filtered = {'2018-05-14 19:37' : 1} #TODO получилось, но первое значение из словаря пришлось добавить вручную
    chkmin = None                       #TODO подскажите, плз, как сделать универсально
    with open(file_name, 'r', encoding='utf-8') as file:
        for line in file:
            filter = line[1:17]
            if chkmin is None : chkmin = filter

            if 'NOK' in line:
                    if filter in filtered:
                        filtered[filter] += 1
                    else:
                        filtered[filter] = 1
                        yield chkmin, filtered[chkmin]
                        chkmin = filter


grouped_events = generate(file_name='events.txt')
for a, b in grouped_events:
    print(f'[{a}]: {b}')
