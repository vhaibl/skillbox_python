# -*- coding: utf-8 -*-

# Подсчитать статистику по буквам в романе Война и Мир.
# Входные параметры: файл для сканирования
# Статистику считать только для букв алфавита (см функцию .isalpha() для строк)
#
# Вывести на консоль упорядоченную статистику в виде
# +---------+----------+
# |  буква  | частота  |
# +---------+----------+
# |    А    |   77777  |
# |    Б    |   55555  |
# |   ...   |   .....  |
# |    a    |   33333  |
# |    б    |   11111  |
# |   ...   |   .....  |
# +---------+----------+
# |  итого  | 9999999  |
# +---------+----------+
#
# Упорядочивание по частоте - по убыванию. Ширину таблицы подберите по своему вкусу
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.
import zipfile


class Sorter:

    def __init__(self, file_name):
        self.file_name = file_name
        self.stat = {}
        self.total = 0

    def unzip(self):
        zfile = zipfile.ZipFile(self.file_name, 'r')
        for filename in zfile.namelist():
            zfile.extract(filename)
        self.file_name = filename

    def collect(self):
        if self.file_name.endswith('.zip'):
            self.unzip()
        with open(self.file_name, 'r', encoding='cp1251') as file:
            for line in file:
                self._collect_for_line(line=line[:-1])

    def _collect_for_line(self, line):
        for char in line:
            if char.isalpha():
                if char in self.stat:
                    self.stat[char] += 1
                    self.total += 1
                else:
                    self.stat[char] = 1
            else:
                pass  # TODO else - pass не нужен

    def print_out(self):

        print('+---------+----------+')
        print('|  буква  | частота  |')
        print('+---------+----------+')
        for char, ch_val in self.sorted:  # TODO название sorted занято стандартными библиотеками
            print('|{:^9}|{:^10}|'.format(char, ch_val))
        print('+---------+----------+')
        print('+  Итого  | {:^9}+'.format(self.total))
        print('+---------+----------+')

# TODO Слишком много дублирования кода в наследниках получается
# TODO 1) Создайте метод, типа run, который будет запускать по-очереди нужные методы
# TODO 2) Создайте для сортировки отдельный метод и только его переопределяйте в наследниках
# TODO Чтобы в итоге у вас получилось
# деф run()
#     собрать информацию
#     сортировать
#     распечатать
class SortByAscending(Sorter):
    def print_out(self):
        self.sorted = sorted(sorter.stat.items(), key=lambda kv: kv[1], reverse=False)
        # TODO атрибут нужно сперва задать в init, а потом уже использовать где-то в методах
        # TODO либо просто использовать переменную, без self
        print('+---------+----------+')
        print('|  буква  | частота  |')
        print('+---------+----------+')
        for char, ch_val in self.sorted:
            print('|{:^9}|{:^10}|'.format(char, ch_val))
        print('+---------+----------+')
        print('+  Итого  | {:^9}+'.format(self.total))
        print('+---------+----------+')


class SortByDescending(Sorter):
    def print_out(self):
        self.sorted = sorted(sorter.stat.items(), key=lambda kv: kv[1], reverse=True)
        print('+---------+----------+')
        print('|  буква  | частота  |')
        print('+---------+----------+')
        for char, ch_val in self.sorted:
            print('|{:^9}|{:^10}|'.format(char, ch_val))
        print('+---------+----------+')
        print('+  Итого  | {:^9}+'.format(self.total))
        print('+---------+----------+')


class SortByAlphabet(Sorter):
    def print_out(self):
        self.sorted = sorted(sorter.stat.items(), key=lambda kv: kv[0], reverse=False)
        print('+---------+----------+')
        print('|  буква  | частота  |')
        print('+---------+----------+')
        for char, ch_val in self.sorted:
            print('|{:^9}|{:^10}|'.format(char, ch_val))
        print('+---------+----------+')
        print('+  Итого  | {:^9}+'.format(self.total))
        print('+---------+----------+')


class SortByReversedAlphabet(Sorter):
    def print_out(self):
        self.sorted = sorted(sorter.stat.items(), key=lambda kv: kv[0], reverse=True)
        print('+---------+----------+')
        print('|  буква  | частота  |')
        print('+---------+----------+')
        for char, ch_val in self.sorted:
            print('|{:^9}|{:^10}|'.format(char, ch_val))
        print('+---------+----------+')
        print('+  Итого  | {:^9}+'.format(self.total))
        print('+---------+----------+')


sorter = SortByAscending(file_name='python_snippets\\voyna-i-mir.txt.zip')
sorter.collect()
sorter.print_out()

sorter = SortByDescending(file_name='python_snippets\\voyna-i-mir.txt.zip')
sorter.collect()
sorter.print_out()

sorter = SortByAlphabet(file_name='python_snippets\\voyna-i-mir.txt.zip')
sorter.collect()
sorter.print_out()

sorter = SortByReversedAlphabet(file_name='python_snippets\\voyna-i-mir.txt.zip')
sorter.collect()
sorter.print_out()

# После выполнения первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию
# Для этого пригодится шаблон проектирование "Шаблонный метод"
#   см https://goo.gl/Vz4828
#   и пример https://gitlab.skillbox.ru/vadim_shandrinov/python_base_snippets/snippets/
