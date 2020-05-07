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
# TODO Тут нужно применить другую логику) так было бы слишком легко.
# TODO Ваша программа сейчас читает весь файл, а только потом запускает цикл по значениям.
# TODO Надо сделать так, чтобы файл читался построчно и отправлял данные в процессе чтения.
# TODO Т.е. обратились один раз к генератору - он прочитал строки за первую минуту, посчитал НОКИ и отправил yield-ом
# TODO обратились ещё раз - продолжил чтение со следующей строки, прочитал строки до другой минуты и отправил yield-ом
def generate(file_name):
    filtered = {}
    with open(file_name, 'r', encoding='utf-8') as file:
        for line in file:
            filter = line[1:17]
            minute = line[15:17]
#TODO Никак не могу понять, как мне читать поминутно. Через цикл while по срезу минут? но как его вставить, и как при
#TODO втором обращении начать с другой минуты?
            if 'NOK' in line:

                if filter in line:
                    if filter in filtered:
                       filtered[filter] += 1

                    else:
                        filtered[filter] = 1
                    if filter in filtered:
                      yield filter, filtered[filter]


                else:
                    filtered = {filter: 1}


grouped_events = generate(file_name='events.txt')
for a,b in grouped_events:
    print(f'[{a}]: {b}')
