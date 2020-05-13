# -*- coding: utf-8 -*-


# Задача: вычислить 3 тикера с максимальной и 3 тикера с минимальной волатильностью в МНОГОПОТОЧНОМ стиле
#
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
import csv
import os
import time
import threading


class VolatilityCalculator(threading.Thread):
    def __init__(self, file):
        super().__init__()
        self.quantity_total = 0
        self.price_total = 0
        self.cost_total = 0
        self.price_list = []
        self.file = file
        self.need_stop = False

    def run(self):
        try:
            self._calculate()
        except Exception as esc:
            print(esc)

    def _calculate(self):

        with open(self.file) as File:
            reader = csv.DictReader(File)
            ticker, volatility = None, None
            for row in reader:
                time.sleep(0.01)
                quantity = int(row['QUANTITY'])
                ticker = row['SECID']
                price = float(row['PRICE'])
                self.quantity_total += quantity
                cost = quantity * price
                self.price_total += price
                self.cost_total += cost
                self.price_list.append(float(row['PRICE']))

            average_price = (min(self.price_list) + max(self.price_list)) / 2
            volatility = ((max(self.price_list) - min(self.price_list)) / average_price) * 100
            fullvol.append((ticker, volatility))


def prepare(path):
    tickerlist = (os.listdir(path))
    for ticker in tickerlist:
        tickerfile = os.path.join(path, ticker)
        yield tickerfile


def output_new(fullvol):
    fullvol.sort(key=lambda x: x[1])
    print('Тикеры с минимальной волатильностью:')
    count = 0
    minlist = []
    for x, y in fullvol:
        if y > 0:
            count += 1
            minlist.append((x, y))
            if count == 3: break
    for x, y in reversed(minlist): print(f'{x} - {y:.03f}%')
    print('Тикеры с максимальной волатильностью:')
    for x, y in fullvol[:-4:-1]:
        print(f'{x} - {y:.03f}%')
    print('Тикеры с нулевой волатильностью:')
    fullvol.sort(key=lambda x: x[0])
    for x, y in fullvol:
        if y == 0:
            print(x, end=' ')


def time_track(func):
    def surrogate(*args, **kwargs):
        started_at = time.time()

        result = func(*args, **kwargs)

        ended_at = time.time()
        elapsed = round(ended_at - started_at, 4)
        print(f'Функция работала {elapsed} секунд(ы)')
        return result

    return surrogate


@time_track
def main():
    tickers = [VolatilityCalculator(file=file1) for file1 in tickerfile]

    for ticker in tickers:
        ticker.start()
        print('обработка потока', ticker.name)
    for ticker in tickers:
        if ticker.is_alive():  # Немного не понял, как завершить отработавший поток, поставил таймаут 0.5 в join
            # TODO Проблема скорее в том, что потоки обращаются к одному элементу fullvol
            # TODO Тут нужно либо Queue использовать, либо сбор информации добавить после join-ов (вне класса)
            # TODO т.е. в классе делаем расчёты, сохраняем данные в атрибуте объекта
            # TODO после join-а проходим по списку объектов и собираем информацию из атрибутов в одном списке
            # TODO А далее уже распечатываем
            ticker.need_stop = True
    for ticker in tickers:
        ticker.join()
        print('ожидание потока', ticker.name)


if __name__ == '__main__':
    tickerfile = prepare(path='trades\\')
    fullvol = []
    main()
    output_new(fullvol)
