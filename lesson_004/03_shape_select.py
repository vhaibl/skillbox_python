# -*- coding: utf-8 -*-

import simple_draw as sd

# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg

figures = {'Треугольник': 'triangle', 'Квадрат': 'square', 'Пятиугольник': 'penta', 'Шестиугольник': 'hexa'}


def triangle(point, angle, length):
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
    v1.draw()
    v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 120, length=length, width=3)
    v2.draw()
    v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 240, length=length, width=3)
    v3.draw()


def square(point, angle, length):
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
    v1.draw()
    v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 90, length=length, width=3)
    v2.draw()
    v3 = sd.get_vector(start_point=v2.end_point, angle=angle - 180, length=length, width=3)
    v3.draw()
    v4 = sd.get_vector(start_point=v3.end_point, angle=angle - 90, length=length, width=3)
    v4.draw()


def penta(point, angle, length):
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
    v1.draw()
    v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 72, length=length, width=3)
    v2.draw()
    v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 144, length=length, width=3)
    v3.draw()
    v4 = sd.get_vector(start_point=v3.end_point, angle=angle + 216, length=length, width=3)
    v4.draw()
    v5 = sd.get_vector(start_point=v4.end_point, angle=angle - 72, length=length, width=3)
    v5.draw()


def hexa(point, angle, length):
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
    v1.draw()
    v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 60, length=length, width=3)
    v2.draw()
    v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 120, length=length, width=3)
    v3.draw()
    v4 = sd.get_vector(start_point=v3.end_point, angle=angle + 180, length=length, width=3)
    v4.draw()
    v5 = sd.get_vector(start_point=v4.end_point, angle=angle - 120, length=length, width=3)
    v5.draw()
    v6 = sd.get_vector(start_point=v5.end_point, angle=angle - 60, length=length, width=3)
    v6.draw()


print('Возможные фигуры:')
for list in enumerate(figures):  # выводим словарь фигур
    print(list)

userfigure = input("Выберите фигуру > ")

while userfigure.isalpha() or int(userfigure) < 0 or int(userfigure) > 3:  # проверяем корректность ввода
    print('Вы ввели некорректный номер!')
    userfigure = input("Выберите фигуру > ")
userfigure = int(userfigure)  # переводим в integer, после проверки на правильность ввода
                              # (убедившись что значение не string)

for i in enumerate(figures):  # сравниваем  ввод пользователя со словарем
    if userfigure == i[0]:  # нашли
        key = (i[1])
        break

selected_figure = figures[key]

point = sd.get_point(250, 250)
angle = 0
length = 100

if selected_figure == 'hexa':  # в зависимости от содержания selected_figure рисуем фигуру
    hexa(point=point, angle=angle, length=length)
elif selected_figure == 'penta':
    penta(point=point, angle=angle, length=length)
elif selected_figure == 'square':
    square(point=point, angle=angle, length=length)
elif selected_figure == 'triangle':
    triangle(point=point, angle=angle, length=length)
sd.pause()
