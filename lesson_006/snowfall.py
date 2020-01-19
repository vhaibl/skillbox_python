import simple_draw as sd

def create_snowflakes():
    global N, x_list, y_list, size_list, new_list, count
    N = 20
    count = 0
    x_list = []
    y_list = []
    size_list = []  # инициализация списков
    new_list = []
    for list_create in range(N + 1):
        x_list.append(sd.random_number(10, 600))
        y_list.append(sd.random_number(600, 1200))  # создание рандомных координат и размеров
        size_list.append(sd.random_number(10, 50))  # для N снежинок
    return N, x_list, y_list, size_list, new_list, count



def clear_snowflakes(N, x_list, y_list, size_list, count):
    for i, y in enumerate(y_list):
        if y_list[i] >= 30:
            point = sd.get_point(x_list[i], y_list[i])
            sd.snowflake(center=point, length=size_list[i], color=sd.background_color)
    return N, x_list, y_list, size_list, count

def move_snowflakes(N, x_list, y_list, size_list, count):

    for i, y in enumerate(y_list):
        if y_list[i] >= 30:
            y_list[i] -= sd.random_number(-5, 20)
            x_list[i] += sd.random_number(-15, 15)
    return N, x_list, y_list, size_list, count

def draw_snowflakes(N, x_list, y_list, size_list, count):
    for i, y in enumerate(y_list):
        if y_list[i] >= 30:
            point = sd.get_point(x_list[i], y_list[i])
            sd.snowflake(center=point, length=size_list[i], color=sd.COLOR_WHITE)
    return N, x_list, y_list, size_list, count

def fallen_snowflakes(N, x_list, y_list, size_list, new_list, count):
#    count = 0
    for i, y in enumerate(y_list):
        if y_list[i] < 30:
             new_list.append(i)
             point1 = sd.get_point(x_list[i], y_list[i])
             sd.snowflake(center=point1, length=size_list[i], color=sd.background_color)
             sd.user_want_exit()
             print(new_list)
             count += 1
    return N, x_list, y_list, size_list,new_list, count

def remove_snowflakes(N, x_list, y_list, size_list, new_list, count):
    for index in reversed(new_list):
         size_list.pop(index)
         y_list.pop(index)
         x_list.pop(index)

    return N, x_list, y_list, size_list, new_list, count

def new_snowflakes(N, x_list, y_list, size_list, count):
    for list_create in range(count + 1):
        x_list.append(sd.random_number(10, 600))
        y_list.append(sd.random_number(600, 1200))  # создание рандомных координат и размеров
        size_list.append(sd.random_number(10, 50))  # для N снежинок
    return N, x_list, y_list, size_list, count


create_snowflakes()
while True:
    sd.start_drawing()
    clear_snowflakes(N, x_list, y_list, size_list, count)
    move_snowflakes(N, x_list, y_list, size_list, count)
    draw_snowflakes(N, x_list, y_list, size_list, count)
    sd.finish_drawing()
    fallen_snowflakes(N, x_list, y_list, size_list, new_list, count)
    remove_snowflakes(N, x_list, y_list, size_list, new_list, count)
    new_list = []
    new_snowflakes(N, x_list, y_list, size_list, count)
# while True:
#     sd.start_drawing()
#     for i, y in enumerate(y_list):
#
#         if y_list[i] >= 30:
#             point = sd.get_point(x_list[i], y_list[i])
#             sd.snowflake(center=point, length=size_list[i], color=sd.background_color)
#             y_list[i] -= sd.random_number(-5, 20)
#             x_list[i] += sd.random_number(-15, 15)
#             point = sd.get_point(x_list[i], y_list[i])
#             sd.snowflake(center=point, length=size_list[i], color=sd.COLOR_WHITE)
#         else:
#             new_list.append(i)
#             point1 = sd.get_point(x_list[i], y_list[i])
#             sd.snowflake(center=point1, length=size_list[i], color=sd.background_color)
#             sd.user_want_exit()
#
#     sd.sleep(0.02)
#     sd.finish_drawing()
#     for index in reversed(new_list):
#         size_list.pop(index)
#         y_list.pop(index)
#         x_list.pop(index)
#     new_list = []

sd.pause()