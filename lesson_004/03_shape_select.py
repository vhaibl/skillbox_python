# -*- coding: utf-8 -*-

import simple_draw as sd


# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg
# figures = {'Треугольник': 'triangle', 'Квадрат': 'square', 'Пятиугольник': 'penta', 'Шестиугольник': 'hexa'}


# TODO Тут нужно будет скопировать код из 1ого задания, остальное всё хорошо!
def figure(point, tilt, length, sides):
    angle = 360 // sides
    angle2 = tilt + angle
    point1 = point
    for angle_step in range(0, 360 - angle, angle):
        v1 = sd.get_vector(point, angle2, length)
        v1.draw()
        angle2 -= angle
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

user_figure = input("Выберите фигуру > ")

while user_figure not in figures:  # проверяем корректность ввода
    print('Вы ввели некорректный номер!')
    user_figure = input("Выберите фигуру > ")

drawing = figures[user_figure]['sd_name']
tilt = 0
length = 100
point = sd.get_point(300, 300)

drawing(point, tilt, length)

sd.pause()
