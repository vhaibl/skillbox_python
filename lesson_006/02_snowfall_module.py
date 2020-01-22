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
    remove_snowflakes, new_snowflakes, new_list, count

N = 20
create_snowflakes(N)
while True:
    sd.start_drawing()
    clear_snowflakes()
    move_snowflakes()
    draw_snowflakes()
    sd.finish_drawing()
    fallen_snowflakes(new_list)
    remove_snowflakes(new_list)
    new_list = []
    new_snowflakes(count)

    sd.sleep(0.01)
    if sd.user_want_exit():
        break
sd.pause()
# создать_снежинки(N)

#  нарисовать_снежинки_цветом(color=sd.background_color)
#  сдвинуть_снежинки()
#  нарисовать_снежинки_цветом(color)
#  если есть номера_достигших_низа_экрана() то
#       удалить_снежинки(номера)
#       создать_снежинки(count)
