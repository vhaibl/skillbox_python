import simple_draw as sd

count = 0
x_list = []
y_list = []
size_list = []
new_list = []


def create_snowflakes(N):
    global x_list, y_list, size_list
    for list_create in range(N + 1):
        x_list.append(sd.random_number(10, 600))
        y_list.append(sd.random_number(600, 1200))
        size_list.append(sd.random_number(10, 50))


def clear_snowflakes():
    global x_list, y_list, size_list
    for i, y in enumerate(y_list):
        if y_list[i] >= 30:
            point = sd.get_point(x_list[i], y_list[i])
            sd.snowflake(center=point, length=size_list[i], color=sd.background_color)


def move_snowflakes():
    global x_list, y_list
    for i, y in enumerate(y_list):
        if y_list[i] >= 30:
            y_list[i] -= sd.random_number(-5, 20)
            x_list[i] += sd.random_number(-15, 15)


def draw_snowflakes():
    global x_list, y_list, size_list
    for i, y in enumerate(y_list):
        if y_list[i] >= 30:
            point = sd.get_point(x_list[i], y_list[i])
            sd.snowflake(center=point, length=size_list[i], color=sd.COLOR_WHITE)


def fallen_snowflakes(new_list, count):  # TODO А вот здесь и далее, убрать new_list и count не получается...
    global x_list, y_list, size_list
    for i, y in enumerate(y_list):
        if y_list[i] < 30:
            new_list.append(i)
            point1 = sd.get_point(x_list[i], y_list[i])
            sd.snowflake(center=point1, length=size_list[i], color=sd.background_color)
            sd.user_want_exit()
            print(new_list)
            count += 1


def remove_snowflakes(new_list):
    global x_list, y_list, size_list
    for index in reversed(new_list):
        size_list.pop(index)
        y_list.pop(index)
        x_list.pop(index)


def new_snowflakes(count):
    global x_list, y_list, size_list
    for list_create in range(count + 1):
        x_list.append(sd.random_number(10, 600))
        y_list.append(sd.random_number(600, 1200))
        size_list.append(sd.random_number(10, 50))
