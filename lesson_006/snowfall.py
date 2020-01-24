import simple_draw as sd

x_list = []
y_list = []
size_list = []


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


def fallen_snowflakes():
    new_list = []
    global x_list, y_list, size_list
    for i, y in enumerate(y_list):
        if y < 30:
            new_list.append(i)
            point1 = sd.get_point(x_list[i], y_list[i])  # TODO А зачем тут поинт? Вроде не рисуем ничего
    return new_list


def remove_snowflakes():  # TODO Раз new_list сделали локальным, то параметром нужно будет передать список с индексами
    global x_list, y_list, size_list
    for index in reversed(new_list):  # TODO И тут его использовать
        size_list.pop(index)
        y_list.pop(index)
        x_list.pop(index)


def new_snowflakes():  # TODO А сюда параметром передавать длину списка, который передавали в remove..
    global x_list, y_list, size_list
    for list_create in new_list:  # TODO Чтобы создавать несколько снежинок
        x_list.append(sd.random_number(10, 600))
        y_list.append(sd.random_number(600, 1200))
        size_list.append(sd.random_number(10, 50))
        new_list.pop()  # TODO Это не нужно будет.
        # TODO Кроме того, не стоит удалять элементы списка, по которому идёт цикл, это приведет к путаннице и ошибкам
