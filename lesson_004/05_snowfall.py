# -*- coding: utf-8 -*-

# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длинн лучей снежинок (от 10 до 100) и пусть все снежинки будут разные
import simple_draw as sd

N = 20

# Пригодятся функции
# sd.get_point()
# sd.snowflake()
# sd.sleep()
# sd.random_number()
# sd.user_want_exit()

x_list = []
y_list = []
size_list= [] # инициализация списков
# TODO Надо подправить стиль Code/Reformat Code
for list_create in range(N + 1):
    x_list.append(sd.random_number(10,600))
    y_list.append(sd.random_number(600,1200)) # создание рандомных координат и размеров
    size_list.append(sd.random_number(10,50)) # для N снежинок


while True:
    sd.start_drawing()
    for draw in range(N):
        # TODO Лучшей практикой будет for i, y in enumerate(список):
        # TODO Так у вас будет доступ и к индексам (i) и к объектам списка
        # TODO Сам же алгоритм лучше не разбивать на разные циклы:
        # TODO циклом проходим по списку со снежинками
        # TODO     получаем точку из текущих координат
        # TODO     рисуем снежинку фоном
        # TODO     меняем координату и получаем новую точку
        # TODO     рисуем снежинку белым цветом
        if y_list[draw] >= 30:
            y_list[draw] -= sd.random_number(-5, 20)  #снег кружится
            x_list[draw] += sd.random_number(-15, 15) #снег летает
            point = sd.get_point(x_list[draw], y_list[draw])
            sd.snowflake(center=point, length=size_list[draw], color=sd.COLOR_WHITE)
        else:
            y_list[draw] += sd.random_number(600, 1200) #постоянно не хватает
        # TODO Попробуйте реализовать следующую идею:
        # TODO Снежинки, которые дошли до границы - записывайте по индексам в отдельный список
        # TODO Дальше, после этого цикла, пройдитесь циклом по списку с индексами и удаляйте упавшие снежинки
        # TODO Только удаляйте не с начала, а с конца (иначе индексы перепутаются)

    sd.finish_drawing()
    sd.sleep(0.01)
    sd.start_drawing()

    for clear in range(N):
        if y_list[clear] >= 31: #Тает, тает, тает снег
            point2 = sd.get_point(x_list[clear], y_list[clear])
            sd.snowflake(center=point2, length=size_list[clear], color=sd.background_color)
# https://mirmagi.ru/news/mr_credo_sneg_letaet_sneg_kruzhitsja/2010-11-13-9637
# ps: не пропаганда, строки припева к комментариям хорошо подошли)
    sd.finish_drawing()
    if sd.user_want_exit():
         break

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


