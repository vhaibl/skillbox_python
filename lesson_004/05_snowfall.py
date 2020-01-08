# -*- coding: utf-8 -*-

# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длинн лучей снежинок (от 10 до 100) и пусть все снежинки будут разные
import simple_draw as sd

N = 20

x_list = []
y_list = []
size_list = []  # инициализация списков
new_list = []
for list_create in range(N + 1):
    x_list.append(sd.random_number(10, 600))
    y_list.append(sd.random_number(600, 1200))  # создание рандомных координат и размеров
    size_list.append(sd.random_number(10, 50))  # для N снежинок

while True:
    sd.start_drawing()
    for i, y in enumerate(y_list):

        if y_list[i] >= 30:
            point = sd.get_point(x_list[i], y_list[i])
            sd.snowflake(center=point, length=size_list[i], color=sd.background_color)
            y_list[i] -= sd.random_number(-5, 20)
            x_list[i] += sd.random_number(-15, 15)
            point = sd.get_point(x_list[i], y_list[i])
            sd.snowflake(center=point, length=size_list[i], color=sd.COLOR_WHITE)
        else:
            new_list.append(i)
            point1 = sd.get_point(x_list[i], y_list[i])
            sd.snowflake(center=point1, length=size_list[i], color=sd.background_color)
            sd.user_want_exit()

        # Попробуйте реализовать следующую идею:
        # Снежинки, которые дошли до границы - записывайте по индексам в отдельный список
        # Дальше, после этого цикла, пройдитесь циклом по списку с индексами и удаляйте упавшие снежинки
        # Только удаляйте не с начала, а с конца (иначе индексы перепутаются)
    sd.sleep(0.02)
    sd.finish_drawing()
    for index in reversed(new_list):
        size_list.pop(index)
        y_list.pop(index)
        x_list.pop(index)
    new_list = [] 

sd.pause()

# подсказка! для ускорения отрисовки можно
#  - убрать clear_screen()
#  - в начале рисования всех снежинок вызвать sd.start_drawing()
#  - на старом месте снежинки отрисовать её же, но цветом sd.background_color
#  - сдвинуть снежинку
#  - отрисовать её цветом sd.COLOR_WHITE на новом месте
#  - после отрисовки всех снежинок, перед sleep(), вызвать sd.finish_drawing()


# 4) Усложненное задание (делать по желанию)
# - сделать рандомные отклонения вправо/влево при каждом шаге
# - сделать сугоб внизу экрана - если снежинка долетает до низа, оставлять её там,
#   и добавлять новую снежинку
# Результат решения см https://youtu.be/XBx0JtxHiLg

#зачет!