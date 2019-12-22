# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd

def second():
    a, b, c, d = -50, -50, 50, 0
    for i in range(10):
        point1 = sd.get_point(a, b)
        point2 = sd.get_point(c, d)
        b += 100
        d += 100
        brick = sd.rectangle(point1, point2, width=1)
        a += 100
        c += 100
        brick = sd.rectangle(point1, point2, width=1)

def first(b,d):
    a,c = 0,  100
    for i in range(10):
        point1 = sd.get_point(a, b)
        point2 = sd.get_point(c, d)
        b += 100
        d += 100
        brick = sd.rectangle(point1, point2, width=1)

first(0,50)
second()




# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for

# TODO здесь ваш код

sd.pause()
