# -*- coding: utf-8 -*-


# Описание предметной области:
#
# При торгах на бирже совершаются сделки - один купил, второй продал.
# Покупают и продают ценные бумаги (акции, облигации, фьючерсы, етс). Ценные бумаги - это по сути долговые расписки.
# Ценные бумаги выпускаются партиями, от десятка до несколько миллионов штук.
# Каждая такая партия (выпуск) имеет свой торговый код на бирже - тикер - https://goo.gl/MJQ5Lq
# Все бумаги из этой партии (выпуска) одинаковы в цене, поэтому говорят о цене одной бумаги.
# У разных выпусков бумаг - разные цены, которые могут отличаться в сотни и тысячи раз.
# Каждая биржевая сделка характеризуется:
#   тикер ценнной бумаги
#   время сделки
#   цена сделки
#   обьем сделки (сколько ценных бумаг было куплено)
#
# В ходе торгов цены сделок могут со временем расти и понижаться. Величина изменения цен называтея волатильностью.
# Например, если бумага №1 торговалась с ценами 11, 11, 12, 11, 12, 11, 11, 11 - то она мало волатильна.
# А если у бумаги №2 цены сделок были: 20, 15, 23, 56, 100, 50, 3, 10 - то такая бумага имеет большую волатильность.
# Волатильность можно считать разными способами, мы будем считать сильно упрощенным способом -
# отклонение в процентах от средней цены за торговую сессию:
#   средняя цена = (максимальная цена + минимальная цена) / 2
#   волатильность = ((максимальная цена - минимальная цена) / средняя цена) * 100%
# Например для бумаги №1:
#   average_price = (12 + 11) / 2 = 11.5
#   volatility = ((12 - 11) / average_price) * 100 = 8.7%
# Для бумаги №2:
#   average_price = (100 + 3) / 2 = 51.5
#   volatility = ((100 - 3) / average_price) * 100 = 188.34%
#
# В реальности волатильность рассчитывается так: https://goo.gl/VJNmmY
#
# Задача: вычислить 3 тикера с максимальной и 3 тикера с минимальной волатильностью.
# Бумаги с нулевой волатильностью вывести отдельно.
# Результаты вывести на консоль в виде:
#   Максимальная волатильность:
#       ТИКЕР1 - ХХХ.ХХ %
#       ТИКЕР2 - ХХХ.ХХ %
#       ТИКЕР3 - ХХХ.ХХ %
#   Минимальная волатильность:
#       ТИКЕР4 - ХХХ.ХХ %
#       ТИКЕР5 - ХХХ.ХХ %
#       ТИКЕР6 - ХХХ.ХХ %
#   Нулевая волатильность:
#       ТИКЕР7, ТИКЕР8, ТИКЕР9, ТИКЕР10, ТИКЕР11, ТИКЕР12
# Волатильности указывать в порядке убывания. Тикеры с нулевой волатильностью упорядочить по имени.
#
# Подготовка исходных данных
# 1. Скачать файл https://drive.google.com/file/d/1l5sia-9c-t91iIPiGyBc1s9mQ8RgTNqb/view?usp=sharing
#       (обратите внимание на значок скачивания в правом верхнем углу,
#       см https://drive.google.com/file/d/1M6mW1jI2RdZhdSCEmlbFi5eoAXOR3u6G/view?usp=sharing)
# 2. Раззиповать средствами операционной системы содержимое архива
#       в папку python_base_source/lesson_012/trades
# 3. В каждом файле в папке trades содержится данные по сделакам по одному тикеру, разделенные запятыми.
#   Первая строка - название колонок:
#       SECID - тикер
#       TRADETIME - время сделки
#       PRICE - цена сделки
#       QUANTITY - количество бумаг в этой сделке
#   Все последующие строки в файле - данные о сделках
#
# Подсказка: нужно последовательно открывать каждый файл, вычитывать данные, высчитывать волатильность и запоминать.
# Вывод на консоль можно сделать только после обработки всех файлов.
#
# Для плавного перехода к мультипоточности, код оформить в обьектном стиле, используя следующий каркас
#
# class <Название класса>:
#
#     def __init__(self, <параметры>):
#         <сохранение параметров>
#
#     def run(self):
#         <обработка данных>

import csv
import os


class VolatilityCalculator:
    def __init__(self, file):
        self.quantity_total = 0
        self.price_total = 0
        self.cost_total = 0
        self.price_list = []
        self.file = file

    def run(self):
        with open(self.file) as File:
            reader = csv.DictReader(File)
            for row in reader:
                quantity = int(row['QUANTITY'])
                ticker = row['SECID']
                price = float(row['PRICE'])
                # print(row['SECID'], row['TRADETIME'], row['PRICE'], row['QUANTITY'])
                self.quantity_total += quantity
                cost = quantity * price
                self.price_total += price
                self.cost_total += cost
                self.price_list.append(float(row['PRICE']))
            average_price = (min(self.price_list) + max(self.price_list)) / 2
            volatility = ((max(self.price_list) - min(self.price_list)) / average_price) * 100
            return ticker, volatility  # TODO стоит подстраховаться и задать ticker до цикла (хотя бы равным None)

            # avg_price = price_total / len(price_list)
            # avg_cost = cost_total / quantity_total
            # print(f'Средняя стоимость: {avg_cost}')
            # print(f'Средняя цена: {average_price}')
            # print(f'Волатильность: {volatility:.3f}%')
            # print(f'Минимальная цена {min(self.price_list)}')
            # print(f'Максимальная цена {max(self.price_list)}')


def prepare():  # TODO Эти функции можно обобщить, чтобы использовать в каждом из заданий
    # TODO Для этого из этой функции нужно сделать генератор путей по переданному параметром пути к директории
    #    global posvol, zerovol, path
    tickerlist = (os.listdir(path))
    for ticker in tickerlist:
        tickerfile = os.path.join(path, ticker)
        vc = VolatilityCalculator(file=tickerfile)  # TODO Само создание объектов класса и их запуск реализовать вне
        # TODO функции
        tickername, tickervol = vc.run()
        print(f'обработка тикера {tickername}')
        if tickervol > 0:
            posvol.append(vc.run())
        else:
            zerovol.append(vc.run())


def output():  # TODO А тут печатать данные, переданные параметром
    # global x
    posvol.sort(key=lambda x: x[1])
    print('Тикеры с минимальной волатильностью:')
    for x, y in reversed(posvol[:3]):
        print(f'{x} - {y:.03f}%')
    print('Тикеры с максимальной волатильностью:')
    for x, y in posvol[:-4:-1]:
        print(f'{x} - {y:.03f}%')
    print('Тикеры с нулевой волатильностью:')
    zerovol.sort(key=lambda x: x[0])
    for x, y in zerovol:
        print(x, end=' ')


posvol = []
zerovol = []
path = 'trades\\'

prepare()
output()
