import simple_draw as sd

N = 20

x_list = []
y_list = []
size_list = []  # инициализация списков
new_list = []
for list_create in range(N + 1):
    x_list.append(sd.random_number(10, 250))
    y_list.append(sd.random_number(600, 1200))  # создание рандомных координат и размеров
    size_list.append(sd.random_number(10, 50))  # для N снежинок


def snowfall():

    #while True:
    #sd.start_drawing()
    for i, y in enumerate(y_list):

        if y_list[i] >= 30:
            point = sd.get_point(x_list[i], y_list[i])
            sd.snowflake(center=point, length=size_list[i], color=sd.background_color)
            y_list[i] -= sd.random_number(-5, 20)
            x_list[i] += sd.random_number(-15, 15)
            point = sd.get_point(x_list[i], y_list[i])
            sd.snowflake(center=point, length=size_list[i], color=sd.COLOR_WHITE)
        else:
            y_list[i] += sd.random_number(600,1200)
            # new_list.append(i)
            # point1 = sd.get_point(x_list[i], y_list[i])
            # sd.snowflake(center=point1, length=size_list[i], color=sd.background_color)
            # sd.user_want_exit()

        # Попробуйте реализовать следующую идею:
        # Снежинки, которые дошли до границы - записывайте по индексам в отдельный список
        # Дальше, после этого цикла, пройдитесь циклом по списку с индексами и удаляйте упавшие снежинки
        # Только удаляйте не с начала, а с конца (иначе индексы перепутаются)
    #sd.sleep(0.02)
    #sd.finish_drawing()
    # for index in reversed(new_list):
    #     size_list.pop(index)
    #     y_list.pop(index)
    #     x_list.pop(index)
    # new_list = []