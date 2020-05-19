# -*- coding: utf-8 -*-

# Прибежал менеджер и сказал что нужно срочно просчитать протокол турнира по боулингу в файле tournament.txt
#
# Пример записи из лога турнира
#   ### Tour 1
#   Алексей	35612/----2/8-6/3/4/
#   Татьяна	62334/6/4/44X361/X
#   Давид	--8/--8/4/8/-224----
#   Павел	----15623113-95/7/26
#   Роман	7/428/--4-533/34811/
#   winner is .........
#
# Нужно сформировать выходной файл tournament_result.txt c записями вида
#   ### Tour 1
#   Алексей	35612/----2/8-6/3/4/    98
#   Татьяна	62334/6/4/44X361/X      131
#   Давид	--8/--8/4/8/-224----    68
#   Павел	----15623113-95/7/26    69
#   Роман	7/428/--4-533/34811/    94
#   winner is Татьяна

# Код обаботки файла расположить отдельном модуле, модуль bowling использовать для получения количества очков
# одного участника. Если захочется изменить содержимое модуля bowling - тесты должны помочь.
#
# Из текущего файла сделать консольный скрипт для формирования файла с результатами турнира.
# Параметры скрипта: --input <файл протокола турнира> и --output <файл результатов турнира>
from collections import defaultdict
from pprint import pprint

from bowling import get_score

input_file = 'tournament.txt'
output_file = 'tournament_result.txt'
game = None
respas = []
respas2 = []

forout = None
gamedict = defaultdict()
with open(output_file, 'w', encoding='utf-8') as out:
    with open(input_file, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip('\n')
            if '###' in line:
                out.write('{}\n'.format(line))
                gamenumber = line.strip('### Tour')
            elif 'winner' in line:
                pass
            elif '	' in line:
                respas = line.split('	')
                try:
                    respas.append(get_score(respas[1]))
                    out.write('{} {}\n'.format(line, get_score(respas[1])))
                except Exception as esc:
                    respas.append('0')
                    out.write('{} 0 - {}\n'.format(line, esc))
                respas.append(gamenumber)
                respas2.append(respas)
                # out.write(forout)


#
# print(game)
pprint(respas2)
# Усложненное задание (делать по желанию)
#
# После обработки протокола турнира вывести на консоль рейтинг игроков в виде таблицы:
#
# +----------+------------------+--------------+
# | Игрок    |  сыграно матчей  |  всего побед |
# +----------+------------------+--------------+
# | Татьяна  |        99        |      23      |
# ...
# | Алексей  |        20        |       5      |
# +----------+------------------+--------------+
