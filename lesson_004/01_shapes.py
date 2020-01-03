# -*- coding: utf-8 -*-

import simple_draw as sd

# Часть 1.
# Написать функции рисования равносторонних геометрических фигур:
# - треугольника
# - квадрата
# - пятиугольника
# - шестиугольника
# Все функции должны принимать 3 параметра:
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Использование копи-пасты - обязательно! Даже тем кто уже знает про её пагубность. Для тренировки.
# Как работает копипаста:
#   - одну функцию написали,
#   - копипастим её, меняем название, чуть подправляем код,
#   - копипастим её, меняем название, чуть подправляем код,
#   - и так далее.
# В итоге должен получиться ПОЧТИ одинаковый код в каждой функции

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# sd.line()
# Результат решения см lesson_004/results/exercise_01_shapes.jpg


def figure(point, angle, length, sides):
    n = sides
    angle = (n - 2) / n * 180
    new_angle = 0 + angle
    point1 = point
    for _ in range(0, n - 1):
        v1 = sd.get_vector(point, new_angle, length, 5)
        v1.draw()
        new_angle += 180 - angle
        point = v1.end_point
    sd.line(point1, point, width=5)



point = sd.get_point(300, 300)
angle = 50
length = 100
sides = 5
figure(point=point, angle=angle, length=length, sides=3)
#
#
# def triangle(point, angle, length,):
#     v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
#     v1.draw()
#     v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 120, length=length, width=3)
#     v2.draw()
#     v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 240, length=length-1, width=3)
#     v3.draw()
#
# def triangle(point, angle, length):
#     v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
#     v1.draw()
#     v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 120, length=length, width=3)
#     v2.draw()
#     v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 240, length=length-1, width=3)
#     v3.draw()
#
# def square(point, angle, length):
#     v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
#     v1.draw()
#     v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 90, length=length, width=3)
#     v2.draw()
#     v3 = sd.get_vector(start_point=v2.end_point, angle=angle -180, length=length, width=3)
#     v3.draw()
#     v4 = sd.get_vector(start_point=v3.end_point, angle=angle -90, length=length-1, width=3)
#     v4.draw()
#
# def penta(point, angle, length):
#     v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
#     v1.draw()
#     v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 72, length=length, width=3)
#     v2.draw()
#     v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 144, length=length, width=3)
#     v3.draw()
#     v4 = sd.get_vector(start_point=v3.end_point, angle=angle + 216, length=length, width=3)
#     v4.draw()
#     v5 = sd.get_vector(start_point=v4.end_point, angle=angle -72, length=length-1, width=3)
#     v5.draw()
#
# def hexa(point, angle, length):
#     v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
#     v1.draw()
#     v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 60, length=length, width=3)
#     v2.draw()
#     v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 120, length=length, width=3)
#     v3.draw()
#     v4 = sd.get_vector(start_point=v3.end_point, angle=angle + 180, length=length, width=3)
#     v4.draw()
#     v5 = sd.get_vector(start_point=v4.end_point, angle=angle - 120, length=length, width=3)
#     v5.draw()
#     v6 = sd.get_vector(start_point=v5.end_point, angle=angle - 60, length=length-1, width=3)
#     v6.draw()
# # TODO Не забывайте про стиль - Code/Reformat Code попробуйте применить
# point_triangle = sd.get_point(100, 400)
# angle_triangle = 50
# length_triangle = 100
# triangle(point=point_triangle, angle=angle_triangle, length=length_triangle)
#
# point_square = sd.get_point(100, 100)
# length_square = 100
# angle_square = 0
# square(point=point_square, angle=angle_square,  length=length_square)
#
# point_penta = sd.get_point(400, 100)
# length_penta = 100
# angle_penta = 0
# penta(point=point_penta, angle=angle_penta,  length=length_penta)
#
# point_hexa = sd.get_point(400, 400)
# length_hexa = 100
# angle_hexa = 0
# hexa(point=point_hexa, angle=angle_hexa,  length=length_hexa)

# TODO Можете приступать ко второй части. Только обратите внимание на разрыв между последней и первой стороной фигуры
# TODO Его надо будет устранить
# Часть 1-бис.
# Попробуйте прикинуть обьем работы, если нужно будет внести изменения в этот код.
# Скажем, связывать точки не линиями, а дугами. Или двойными линиями. Или рисовать круги в угловых точках. Или...
# А если таких функций не 4, а 44? Код писать не нужно, просто представь объем работы... и запомни это.

# Часть 2 (делается после зачета первой части)
#
# Надо сформировать функцию, параметризированную в местах где была "небольшая правка".
# Это называется "Выделить общую часть алгоритма в отдельную функцию"
# Потом надо изменить функции рисования конкретных фигур - вызывать общую функцию вместо "почти" одинакового кода.
#
# В итоге должно получиться:
#   - одна общая функция со множеством параметров,
#   - все функции отрисовки треугольника/квадрата/етс берут 3 параметра и внутри себя ВЫЗЫВАЮТ общую функцию.
#
# Не забудте в этой общей функции придумать, как устранить разрыв
#   в начальной/конечной точках рисуемой фигуры (если он есть)

# Часть 2-бис.
# А теперь - сколько надо работы что бы внести изменения в код? Выгода на лицо :)
# Поэтому среди программистов есть принцип D.R.Y. https://clck.ru/GEsA9
# Будьте ленивыми, не используйте копи-пасту!


sd.pause()
