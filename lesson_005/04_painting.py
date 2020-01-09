# -*- coding: utf-8 -*-

import simple_draw as sd
from picture.tree import draw_bunches
from picture.sky import sun
from picture.sky import rainbow
from picture.house import house
from picture.redneck import smile
from picture.snowfall import snowfall
sd.resolution = (1200,800)

def tree():
    root_point = sd.get_point(900, 30)
    color = sd.COLOR_DARK_YELLOW
   # sd.start_drawing()
    draw_bunches(start_point=root_point, angle=90, length=80, color=color)

    #sd.finish_drawing()
def tree2():
    root_point = sd.get_point(1100, 00)
    color = sd.COLOR_DARK_RED
   # sd.start_drawing()
    draw_bunches(start_point=root_point, angle=90, length=50, color=color)
   # sd.finish_drawing()

sd.clear_screen()
while True:

    sd.start_drawing()
    tree_clear = sd.get_point(700, 0)
    sd.square(tree_clear, side=550, color=sd.background_color, width=0)
    tree()
    tree2()
    house()
    rainbow()
    sun()
    smile(color=sd.COLOR_DARK_YELLOW, x=550,  y=200)
    #picture.snowfall.animate = 200
    snowfall()

    sd.finish_drawing()
    sd.sleep(0.01)

# Создать пакет, в который скопировать функции отрисовки из предыдущего урока
#  - радуги
#  - стены
#  - дерева
#  - смайлика
#  - снежинок
# Функции по модулям разместить по тематике. Название пакета и модулей - по смыслу.
# Создать модуль с функцией отрисовки кирпичного дома с широким окном и крышей.

# С помощью созданного пакета нарисовать эпохальное полотно "Утро в деревне".
# На картине должны быть:
#  - кирпичный дом, в окошке - смайлик.
#  - слева от дома - сугроб (предположим что это ранняя весна)
#  - справа от дома - дерево (можно несколько)
#  - справа в небе - радуга, слева - солнце (весна же!)
# пример см. lesson_005/results/04_painting.jpg
# Приправить своей фантазией по вкусу (коты? коровы? люди? трактор? что придумается)

# TODO здесь ваш код

# Усложненное задание (делать по желанию)
# Анимировать картину.
# Пусть слева идет снегопад, радуга переливается цветами, смайлик моргает, солнце крутит лучами, етс.
# Задержку в анимировании все равно надо ставить, пусть даже 0.01 сек - так библиотека устойчивей работает.
sd.pause()