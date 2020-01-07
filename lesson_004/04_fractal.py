# -*- coding: utf-8 -*-

import simple_draw as sd


# 1) Написать функцию draw_branches, которая должна рисовать две ветви дерева из начальной точки
# Функция должна принимать параметры:
# - точка начала рисования,
# - угол рисования,
# - длина ветвей,
# Отклонение ветвей от угла рисования принять 30 градусов,

# 2) Сделать draw_branches рекурсивной
# - добавить проверку на длину ветвей, если длина меньше 10 - не рисовать
# - вызывать саму себя 2 раза из точек-концов нарисованных ветвей,
#   с параметром "угол рисования" равным углу только что нарисованной ветви,
#   и параметром "длинна ветвей" в 0.75 меньшей чем длина только что нарисованной ветви

# 3) первоначальный вызов:


def draw_bunches(start_point, angle, length):
    if length < 10:
        return
    v1 = sd.get_vector(start_point=start_point, angle=angle, length=length, width=1)
    v1.draw(sd.COLOR_GREEN)
    angle1 = (angle - 30) * (1 + (sd.random_number(-40, 40) / 100))
    angle2 = (angle + 30) * (1 + (sd.random_number(-40, 40) / 100))
    next_point = v1.end_point
    next_length = length * 0.75 * (1 + (sd.random_number(-20, 20) / 100))
    draw_bunches(start_point=next_point, angle=angle1, length=next_length)
    draw_bunches(start_point=next_point, angle=angle2, length=next_length)


root_point = sd.get_point(300, 30)
sd.start_drawing()
draw_bunches(start_point=root_point, angle=90, length=100)
sd.finish_drawing()
# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# Возможный результат решения см lesson_004/results/exercise_04_fractal_01.jpg

# можно поиграть -шрифтами- цветами и углами отклонения

# 4) Усложненное задание (делать по желанию)
# - сделать рандомное отклонение угла ветвей в пределах 40% от 30-ти градусов
# - сделать рандомное отклонение длины ветвей в пределах 20% от коэффициента 0.75
# Возможный результат решения см lesson_004/results/exercise_04_fractal_02.jpg

# Пригодятся функции
# sd.random_number()

sd.pause()
