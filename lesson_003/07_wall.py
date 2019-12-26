# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for
# TODO :) код рабочий, спорить сложно
# TODO Но можно его сократить, практически в два раза
for y in range(000, 1001, 100):
    for x in range(000, 1001, 100):  # TODO Ведь различия по сути только в этой строке

        point1 = sd.get_point(x, y)
        point2 = sd.get_point(x + 100, y + 50)
        brick = sd.rectangle(point1, point2, width=1, color=sd.COLOR_DARK_RED)
    brick = sd.rectangle(point1, point2, width=1, color=sd.COLOR_DARK_RED)

for y in range(50, 1001, 100):
    # TODO Тк сдвиг зависит от номеря ряда, а ряд от внешнего цикла
    # TODO Будем нумеровать итерации в нём -
    # TODO for row, y in enumerate(range(...))
    # TODO Так, в row у нас будет номер ряда.
    # TODO Проверив его на чётность, мы сможем решить, двигать ли ряд, или нет
    # TODO (row % 2 == 0)
    # TODO Как добавить сдвиг, узнав о чётности ряда?
    # TODO Например, если ряд четный, начинать цикл с -50, если нет - то с 0
    # TODO Для этого до цикла создадим x0 и с помощью тернарного оператора будем менять его значения
    # TODO x0 = -50 if (условие четности ряда) else 0
    # TODO И этот x0 добавим в цикл фор вместо -50, которое там есть сейчас
    for x in range(-50, 1001, 100):
        point1 = sd.get_point(x, y)
        point2 = sd.get_point(x + 100, y + 50)
        brick = sd.rectangle(point1, point2, width=1, color=sd.COLOR_DARK_RED)
    brick = sd.rectangle(point1, point2, width=1, color=sd.COLOR_DARK_RED)

sd.pause()
