# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for
for row, y in enumerate(range(000, 1001, 50)):
    for x in range(000, 1001, 100):
        if row % 2 == 0:
            x += -50
        point1 = sd.get_point(x, y)
        point2 = sd.get_point(x + 100, y + 50)
        brick = sd.rectangle(point1, point2, width=1, color=sd.COLOR_DARK_RED)

sd.pause()
