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
    angle = 360 // sides
    point1 = point
    for angle_step in range(0, 360 - angle, angle):
        v1 = sd.get_vector(point, angle_step + tilt, length)
        v1.draw(color=color1)
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
while usercolor not in color_list:
    print('Вы ввели некорректный номер!')
    usercolor = input("Введите желаемый цвет > ")

color1 = color_list[usercolor]['sd_name']
tilt = 0
length = 100

point = sd.get_point(150, 150)
triangle(point, tilt, length)

point = sd.get_point(100, 400)
square(point, tilt, length)

point = sd.get_point(300, 150)
penta(point, tilt, length)

point = sd.get_point(300, 400)
hexa(point, tilt, length)
sd.pause()

#зачет!