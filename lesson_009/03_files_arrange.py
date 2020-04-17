# -*- coding: utf-8 -*-

import os, time, shutil

# Нужно написать скрипт для упорядочивания фотографий (вообще любых файлов)
# Скрипт должен разложить файлы из одной папки по годам и месяцам в другую.
# Например, так:
#   исходная папка
#       icons/cat.jpg
#       icons/man.jpg
#       icons/new_year_01.jpg
#   результирующая папка
#       icons_by_year/2018/05/cat.jpg
#       icons_by_year/2018/05/man.jpg
#       icons_by_year/2017/12/new_year_01.jpg
#
# Входные параметры основной функции: папка для сканирования, целевая папка.
# Имена файлов в процессе работы скрипта не менять, год и месяц взять из времени создания файла.
# Обработчик файлов делать в обьектном стиле - на классах.
#
# Файлы для работы взять из архива icons.zip - раззиповать проводником в папку icons перед написанием кода.
# Имя целевой папки - icons_by_year (тогда она не попадет в коммит)
#
# Пригодятся функции:
#   os.walk
#   os.path.dirname
#   os.path.join
#   os.path.normpath
#   os.path.getmtime
#   time.gmtime
#   os.makedirs
#   shutil.copy2
#
# Чтение документации/гугла по функциям - приветствуется. Как и поиск альтернативных вариантов :)
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.

import time
import os
import shutil


class Sorter:
    def __init__(self, path, new_path):
        self.path = path
        self.new_path = new_path
        self.path_normalized = os.path.normpath(path)

    def takefromfolder(self):
        for dirpath, dirnames, filenames in os.walk(self.path_normalized):
            for file in filenames:
                full_file_path = os.path.join(dirpath, file)
                secs = os.path.getmtime(full_file_path)
                file_time = time.gmtime(secs)
                new_dest = self.sortby(file_time)
                print(new_dest)
                if not os.path.exists(new_dest):
                    os.makedirs(new_dest)
                shutil.copy2(full_file_path, new_dest)

    def sortby(self, file_time):
        new_dest = os.path.join(str(new_path) + '\\' + str(file_time.tm_year) + '\\' + str(file_time.tm_mon))
        return new_dest


path = 'icons'
new_path = 'sorted_icons'
sorticons = Sorter(path=path, new_path=new_path)
sorticons.takefromfolder()

# _________________________________
# Не могу разобраться с усложненной частью. Вроде создаю список с отсортированными путями, но все равно
# добавляются лишние папки

import zipfile
from pprint import pprint

outdir = 'sorted_icons2'
pathlist = []
archive = zipfile.ZipFile('icons.zip', 'r')
for afile in archive.filelist:
    ayear = afile.date_time[0]
    amonth = afile.date_time[1]
    aday = afile.date_time[2]
    apath = str(outdir) + '\\' + str(ayear) + '\\' + str(amonth) + '\\' + str(afile.filename.split('/')[-1])
    pathlist.append(apath)
    pprint(pathlist)
    archive.extract(member=afile, path=apath)
    # TODO Этот метод создает свои пути внутри себя
    # TODO Нужно использовать что-то другое например shutil.copyfileobj

# Усложненное задание (делать по желанию)
# Нужно обрабатывать zip-файл, содержащий фотографии, без предварительного извлечения файлов в папку.
# Это относится ктолько к чтению файлов в архиве. В случае паттерна "Шаблонный метод" изменяется способ
# получения данных (читаем os.walk() или zip.namelist и т.д.)
# Документация по zipfile: API https://docs.python.org/3/library/zipfile.html
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
