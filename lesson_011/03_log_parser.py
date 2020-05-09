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
    filtered = {}
    chkmin = None
    with open(file_name, 'r', encoding='utf-8') as file:
        for line in file:
            filter = line[1:17]
            if 'NOK' in line:
                if filter in filtered:
                    filtered[filter] += 1
                else:
                    filtered[filter] = 1
                    if chkmin is None:
                        chkmin = filter
                        continue  # Вот сюда если перенести всё будет работать верно
                    yield chkmin, filtered[chkmin]
                    chkmin = filter
        yield chkmin, filtered[chkmin]


grouped_events = generate(file_name='events.txt')
for a, b in grouped_events:
    print(f'[{a}]: {b}')
