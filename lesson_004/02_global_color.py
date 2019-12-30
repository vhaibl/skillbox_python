# -*- coding: utf-8 -*-
import simple_draw as sd

# Добавить цвет в функции рисования геом. фигур. из упр lesson_004/01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом

# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()
# и константы COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE
# Результат решения см lesson_004/results/exercise_02_global_color.jpg
colors = {}
colors = {'red': sd.COLOR_RED, 'orange': sd.COLOR_ORANGE, 'yellow': sd.COLOR_YELLOW, 'green': sd.COLOR_GREEN,
          'cyan': sd.COLOR_CYAN, 'blue': sd.COLOR_BLUE, 'purple': sd.COLOR_PURPLE}
print('Возможные цвета:')
for list in enumerate(colors):
    print(list)
ar123 = int(0)
ar123 = (int(input()))
if 0 < ar123 > 6:
    print("Неправильное значение")
    choose_color()
else:
    for i in enumerate(colors):
        if ar123 == i[0]:
            keyvalue = (i[1])
            break

color1 = colors[keyvalue]


def triangle(point, angle, length, color):
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
    v1.draw(color=color)
    v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 120, length=length, width=3)
    v2.draw(color=color)
    v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 240, length=length, width=3)
    v3.draw(color=color)


def square(point, angle, length, color):
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
    v1.draw(color=color)
    v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 90, length=length, width=3)
    v2.draw(color=color)
    v3 = sd.get_vector(start_point=v2.end_point, angle=angle - 180, length=length, width=3)
    v3.draw(color=color)
    v4 = sd.get_vector(start_point=v3.end_point, angle=angle - 90, length=length, width=3)
    v4.draw(color=color)


def penta(point, angle, length, color):
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
    v1.draw(color=color)
    v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 72, length=length, width=3)
    v2.draw(color=color)
    v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 144, length=length, width=3)
    v3.draw(color=color)
    v4 = sd.get_vector(start_point=v3.end_point, angle=angle + 216, length=length, width=3)
    v4.draw(color=color)
    v5 = sd.get_vector(start_point=v4.end_point, angle=angle - 72, length=length, width=3)
    v5.draw(color=color)


def hexa(point, angle, length, color):
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
    v1.draw(color=color)
    v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 60, length=length, width=3)
    v2.draw(color=color)
    v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 120, length=length, width=3)
    v3.draw(color=color)
    v4 = sd.get_vector(start_point=v3.end_point, angle=angle + 180, length=length, width=3)
    v4.draw(color=color)
    v5 = sd.get_vector(start_point=v4.end_point, angle=angle - 120, length=length, width=3)
    v5.draw(color=color)
    v6 = sd.get_vector(start_point=v5.end_point, angle=angle - 60, length=length, width=3)
    v6.draw(color=color)


point_triangle = sd.get_point(100, 400)
angle_triangle = 50
length_triangle = 100
triangle(point=point_triangle, angle=angle_triangle, length=length_triangle, color=color1)

point_square = sd.get_point(100, 100)
length_square = 100
angle_square = 0
square(point=point_square, angle=angle_square, length=length_square, color=color1)

point_penta = sd.get_point(400, 100)
length_penta = 100
angle_penta = 0
penta(point=point_penta, angle=angle_penta, length=length_penta, color=color1)

point_hexa = sd.get_point(400, 400)
length_hexa = 100
angle_hexa = 0
hexa(point=point_hexa, angle=angle_hexa, length=length_hexa, color=color1)
# TODO здесь ваш код

sd.pause()