# -*- coding: utf-8 -*-
import random

import simple_draw as sd

sd.resolution = (1200, 600)

radius = 50
point = sd.get_point(100, 100)
for _ in range(3):
    radius += 5
    circle = sd.circle(center_position=point, radius=radius, width=2)


# Написать функцию рисования пузырька, принммающую 2 (или более) параметра: точка рисовании и шаг
def bubble(point, step):
    radius = 50
    for _ in range(3):
        radius += step
        sd.circle(center_position=point, radius=radius, width=2)


# Нарисовать 10 пузырьков в ряд

for x in range(100, 1001, 100):
    point = sd.get_point(x, 100)
    bubble(point=point, step=5)

# Нарисовать три ряда по 10 пузырьков

for y in range(100, 301, 100):
    for x in range(100, 1001, 100):
        point = sd.get_point(x, y)
        bubble(point=point, step=5)


# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами


def bubble(point, step, color):
    radius = random.randint(1, 50)
    for _ in range(3):
        radius += step
        sd.circle(center_position=point, radius=radius, width=2, color=color)


for _ in range(101):
    point = sd.random_point()
    color = sd.random_color()
    step = random.randint(2, 10)
    bubble(point=point, step=step, color=color)
sd.pause()
#зачет!