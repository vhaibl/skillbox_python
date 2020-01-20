# -*- coding: utf-8 -*-

import simple_draw as sd

# На основе кода из lesson_004/05_snowfall.py
# сделать модуль snowfall.py в котором реализовать следующие функции
#  создать_снежинки(N) - создает N снежинок
#  нарисовать_снежинки_цветом(color) - отрисовывает все снежинки цветом color
#  сдвинуть_снежинки() - сдвигает снежинки на один шаг
#  номера_достигших_низа_экрана() - выдает список номеров снежинок, которые вышли за границу экрана
#  удалить_снежинки(номера) - удаляет снежинки с номерами из списка
#
# В текущем модуле реализовать главный цикл падения снежинок,
# обращаясь ТОЛЬКО к функциям модуля snowfall


from snowfall import create_snowflakes, clear_snowflakes, move_snowflakes, draw_snowflakes, fallen_snowflakes, \
    remove_snowflakes, new_snowflakes, x_list, y_list, size_list, count, new_list

N = 10

create_snowflakes(N)
while True:
    sd.start_drawing()
    clear_snowflakes(x_list, y_list, size_list)
    move_snowflakes(x_list, y_list)
    draw_snowflakes(x_list, y_list, size_list)
    sd.finish_drawing()
    fallen_snowflakes(x_list, y_list, size_list, new_list, count)
    remove_snowflakes(x_list, y_list, size_list, new_list)
    new_list = []
    new_snowflakes(x_list, y_list, size_list, count)
    sd.sleep(0.1)
    if sd.user_want_exit():
        break
sd.pause()
