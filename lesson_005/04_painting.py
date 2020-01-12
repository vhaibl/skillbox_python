# -*- coding: utf-8 -*-

import simple_draw as sd
from picture.tree import tree
from picture.tree import tree2
from picture.sky import sun
# from picture.sky import sun2
from picture.sky import rainbow
from picture.house import house
from picture.redneck import smile
from picture.redneck import smile2
from picture.snowfall import snowfall

sd.resolution = (1200, 800)

sd.clear_screen()
counter = 0
while True:
    # TODO Общий цикл и счетчик тоже надо в пакет засунуть?
    counter += 1
    sd.start_drawing()
    tree()
    tree2()
    house()
    sun(counter)
    smile(counter)
    snowfall()
    sd.finish_drawing()

    rainbow()  # TODO по радуге пока не понятно, как сделать так, чтобы все цвета полностью не перебирались за
    # TODO один проход общего цикла

    if counter > 100: counter = 0
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


# Усложненное задание (делать по желанию)
# Анимировать картину.
# Пусть слева идет снегопад, радуга переливается цветами, смайлик моргает, солнце крутит лучами, етс.
# Задержку в анимировании все равно надо ставить, пусть даже 0.01 сек - так библиотека устойчивей работает.
sd.pause()
