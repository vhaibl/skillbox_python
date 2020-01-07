# -*- coding: utf-8 -*-

import simple_draw as sd


# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg
# figures = {'Треугольник': 'triangle', 'Квадрат': 'square', 'Пятиугольник': 'penta', 'Шестиугольник': 'hexa'}


def figure(point, tilt, length, sides):
    angle = (sides - 2) / sides * 180
    # print(angle)
    angle2 = tilt + angle
    point1 = point
    for i in range(sides - 1):
        v1 = sd.get_vector(point, angle2, length)
        v1.draw()
        angle2 += 180 - angle
        # print(angle, angle2)
        point = v1.end_point
    sd.line(point1, point)


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


figures = {'0': {'figure': 'треугольник', 'sd_name': triangle},
           '1': {'figure': 'квадрат', 'sd_name': square},
           '2': {'figure': 'пятиугольник', 'sd_name': penta},
           '3': {'figure': 'шестиугольник', 'sd_name': hexa},
           }

print('Возможные фигуры:')
for list, name in figures.items():  # выводим словарь фигур
    print(list, name.get('figure'))

userfigure = input("Выберите фигуру > ")
# TODO Тут можно хитро воспользоваться тем, что input() передает ввод пользователя в строках (str)
# TODO И ключи у нас в словаре строчные '0'...
# TODO Можем просто написать условие while ввод не в словаре
while userfigure.isalpha() or int(userfigure) < 0 or int(userfigure) > 3:  # проверяем корректность ввода
    print('Вы ввели некорректный номер!')
    userfigure = input("Выберите фигуру > ")

drawing = figures[userfigure]['sd_name']
angle = None  # TODO А зачем нужен angle этот?
tilt = 0
length = 100
point = sd.get_point(300, 300)

drawing(point, tilt, length)

sd.pause()
