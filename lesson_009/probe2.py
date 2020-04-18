# -*- coding: utf-8 -*-

# Сделать генератор текста на основе статистики
# Идея проста: подсчитаем какие буквы наиболее часто стоят рядом
# Точнее, подсчитаем как часто за буковой Х идет буква У, на основе некоего текста.
# После этого начнем с произвольной буквы и каждую следующую будем выбирать в зависимости от
# частоты её появления в статистике.
import zipfile
from pprint import pprint

outdir = 'sorted_icons2'
pathlist=[]
archive = zipfile.ZipFile('icons.zip', 'r')
for afile in archive.filelist:
    ayear = afile.date_time[0]
    amonth = afile.date_time[1]
    aday = afile.date_time[2]
    apath = str(outdir) + '\\' + str(ayear) + '\\' + str(amonth) + '\\' + str(afile.filename.split('/')[-1])
    pathlist.append(apath)
    pprint(pathlist)
    archive.extract(member=afile, path=apath)





