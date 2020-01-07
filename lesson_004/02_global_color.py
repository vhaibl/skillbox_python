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

# def triangle(point, angle, length, color):
#     v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
#     v1.draw(color=color)
#     v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 120, length=length, width=3)
#     v2.draw(color=color)
#     v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 240, length=length, width=3)
#     v3.draw(color=color)
#
#
# def square(point, angle, length, color):
#     v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
#     v1.draw(color=color)
#     v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 90, length=length, width=3)
#     v2.draw(color=color)
#     v3 = sd.get_vector(start_point=v2.end_point, angle=angle - 180, length=length, width=3)
#     v3.draw(color=color)
#     v4 = sd.get_vector(start_point=v3.end_point, angle=angle - 90, length=length, width=3)
#     v4.draw(color=color)
#
#
# def penta(point, angle, length, color):
#     v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
#     v1.draw(color=color)
#     v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 72, length=length, width=3)
#     v2.draw(color=color)
#     v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 144, length=length, width=3)
#     v3.draw(color=color)
#     v4 = sd.get_vector(start_point=v3.end_point, angle=angle + 216, length=length, width=3)
#     v4.draw(color=color)
#     v5 = sd.get_vector(start_point=v4.end_point, angle=angle - 72, length=length, width=3)
#     v5.draw(color=color)
#
#
# def hexa(point, angle, length, color):
#     v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
#     v1.draw(color=color)
#     v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 60, length=length, width=3)
#     v2.draw(color=color)
#     v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 120, length=length, width=3)
#     v3.draw(color=color)
#     v4 = sd.get_vector(start_point=v3.end_point, angle=angle + 180, length=length, width=3)
#     v4.draw(color=color)
#     v5 = sd.get_vector(start_point=v4.end_point, angle=angle - 120, length=length, width=3)
#     v5.draw(color=color)
#     v6 = sd.get_vector(start_point=v5.end_point, angle=angle - 60, length=length, width=3)
#     v6.draw(color=color)


# colors = {, 'orange': sd.COLOR_ORANGE, 'yellow': sd.COLOR_YELLOW, 'green': sd.COLOR_GREEN,
# 'cyan': sd.COLOR_CYAN, 'blue': sd.COLOR_BLUE, 'purple': sd.COLOR_PURPLE}

def figure(point, tilt, length, sides):
    angle = (sides - 2) / sides * 180
    angle2 = tilt + angle
    point1 = point
    for i in range(sides - 1):
        v1 = sd.get_vector(point, angle2, length)
        v1.draw(color=color1)
        angle2 += 180 - angle
        point = v1.end_point
    sd.line(point1, point, color=color1)


def triangle(point, tilt, length):
    sides = 3
    figure(point, tilt, length, sides)


def square(point, tilt, length):
    sides = 4
    figure(point, tilt, length, sides)


def penta(point, tilt, length):
    sides = 5
    figure(point, tilt, length, sides)


def hexa(point, tilt, length):
    sides = 6
    figure(point, tilt, length, sides)


color_list = {'0': {'color_name': 'red', 'sd_name': sd.COLOR_RED},
              '1': {'color_name': 'orange', 'sd_name': sd.COLOR_ORANGE},
              '2': {'color_name': 'yellow', 'sd_name': sd.COLOR_YELLOW},
              '3': {'color_name': 'green', 'sd_name': sd.COLOR_GREEN},
              '4': {'color_name': 'cyan', 'sd_name': sd.COLOR_CYAN},
              '5': {'color_name': 'blue', 'sd_name': sd.COLOR_BLUE},
              '6': {'color_name': 'purple', 'sd_name': sd.COLOR_PURPLE}}

print('Возможные цвета:')
for number, color in color_list.items():
    print(number, ':', color.get('color_name'))

usercolor = input("Введите желаемый цвет > ")
while usercolor.isalpha() or int(usercolor) < 0 or int(usercolor) > 6:  # проверяем корректность ввода
    print('Вы ввели некорректный номер!')
    usercolor = input("Введите желаемый цвет > ")

color1 = color_list[usercolor]['sd_name']
angle = None
tilt = 0
length = 100

point = sd.get_point(150, 400)
triangle(point, tilt, length)

point = sd.get_point(200, 100)
square(point, tilt, length)

point = sd.get_point(500, 100)
penta(point, tilt, length)

point = sd.get_point(500, 400)
hexa(point, tilt, length)

# point_triangle = sd.get_point(100, 400)
# angle_triangle = 50
# length_triangle = 100
# triangle(point=point_triangle, angle=angle_triangle, length=length_triangle, color=color1)
#
# point_square = sd.get_point(100, 100)
# length_square = 100
# angle_square = 0
# square(point=point_square, angle=angle_square, length=length_square, color=color1)
#
# point_penta = sd.get_point(400, 100)
# length_penta = 100
# angle_penta = 0
# penta(point=point_penta, angle=angle_penta, length=length_penta, color=color1)
#
# point_hexa = sd.get_point(400, 400)
# length_hexa = 100
# angle_hexa = 0
# hexa(point=point_hexa, angle=angle_hexa, length=length_hexa, color=color1)

sd.pause()
