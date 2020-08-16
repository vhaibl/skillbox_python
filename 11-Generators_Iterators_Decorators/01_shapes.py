# -*- coding: utf-8 -*-

import simple_draw as sd

# На основе вашего кода из решения lesson_004/01_shapes.py сделать функцию-фабрику,
# которая возвращает функции рисования треугольника, четырехугольника, пятиугольника и т.д.
#
# Функция рисования должна принимать параметры
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Функция-фабрика должна принимать параметр n - количество сторон.


def get_polygon(n):

    def figure(point, length, tilt):
        angle = 360 // n
        point1 = point
        for angle_step in range(0, 360 - angle, angle):
            v1 = sd.get_vector(point, angle_step + tilt, length)
            v1.draw()
            point = v1.end_point
        sd.line(point1, point)
        return point
    return figure


draw_triangle = get_polygon(n=3)
draw_triangle(point=sd.get_point(200, 200), tilt=13, length=100)


sd.pause()
#зачет!