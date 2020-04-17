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
        self.sorted_data = {}

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

    def sort_style(self):
        pass

    def print_out(self):

        print('+---------+----------+')
        print('|  буква  | частота  |')
        print('+---------+----------+')
        self.sort_style()
        print('+---------+----------+')
        print('+  Итого  | {:^9}+'.format(self.total))
        print('+---------+----------+')
        print('----------------------------------------------------')

    def run(self):
        self.collect()
        self.print_out()


class SortByAscending(Sorter):
    def sort_style(self):
        self.sorted_data = sorted(sorter.stat.items(), key=lambda kv: kv[1], reverse=False)
        for char, ch_val in self.sorted_data:
            print('|{:^9}|{:^10}|'.format(char, ch_val))


class SortByDescending(Sorter):
    def sort_style(self):
        self.sorted_data = sorted(sorter.stat.items(), key=lambda kv: kv[1], reverse=True)
        for char, ch_val in self.sorted_data:
            print('|{:^9}|{:^10}|'.format(char, ch_val))


class SortByAlphabet(Sorter):
    def sort_style(self):
        self.sorted_data = sorted(sorter.stat.items(), key=lambda kv: kv[0], reverse=False)
        for char, ch_val in self.sorted_data:
            print('|{:^9}|{:^10}|'.format(char, ch_val))


class SortByReversedAlphabet(Sorter):
    def sort_style(self):
        self.sorted_data = sorted(sorter.stat.items(), key=lambda kv: kv[0], reverse=True)
        for char, ch_val in self.sorted_data:
            print('|{:^9}|{:^10}|'.format(char, ch_val))


sorter = SortByAscending(file_name='python_snippets\\voyna-i-mir.txt.zip')
sorter.run()
sorter = SortByDescending(file_name='python_snippets\\voyna-i-mir.txt.zip')
sorter.run()
sorter = SortByAlphabet(file_name='python_snippets\\voyna-i-mir.txt.zip')
sorter.run()
sorter = SortByReversedAlphabet(file_name='python_snippets\\voyna-i-mir.txt.zip')
sorter.run()

# После выполнения первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию
# Для этого пригодится шаблон проектирование "Шаблонный метод"
#   см https://goo.gl/Vz4828
#   и пример https://gitlab.skillbox.ru/vadim_shandrinov/python_base_snippets/snippets/
#зачет!