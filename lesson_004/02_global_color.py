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
# TODO Тут можно хитро воспользоваться тем, что input() передает ввод пользователя в строках (str)
# TODO И ключи у нас в словаре строчные '0'...
# TODO Можем просто написать условие while ввод не в словаре
while usercolor.isalpha() or int(usercolor) < 0 or int(usercolor) > 6:  # проверяем корректность ввода
    print('Вы ввели некорректный номер!')
    usercolor = input("Введите желаемый цвет > ")

color1 = color_list[usercolor]['sd_name']
angle = None  # TODO Зачем нужен этот angle?
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
sd.pause()
