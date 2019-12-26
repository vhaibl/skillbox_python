# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd

sd.resolution = (1200, 600)
rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)
a = 50
b = 50
c = 350
d = 450
for rainbow in rainbow_colors:
    a += 5
    point1 = sd.get_point(a, b)
    point2 = sd.get_point(a+300, d)
    line = sd.line(start_point=point1, end_point=point2, color=rainbow, width=4, )

# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво
radius1 = 400
for rainbow2 in rainbow_colors:
    point = sd.get_point(1200, -50)
    radius1 += 20
    circle = sd.circle(center_position=point, width=20, color=rainbow2, radius=radius1)
sd.pause()
# В остальном отлично :)