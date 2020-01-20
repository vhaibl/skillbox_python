import simple_draw as sd

count = 0
x_list = []
y_list = []
size_list = []
new_list = []


def create_snowflakes(N):
    global x_list, y_list, size_list, new_list, count
    for list_create in range(N + 1):
        x_list.append(sd.random_number(10, 600))
        y_list.append(sd.random_number(600, 1200))
        size_list.append(sd.random_number(10, 50))
        # TODO Не понятно. Функция заполняет три списка. Зачем нужно столько элементов возвращать?)
    return N, x_list, y_list, size_list, new_list, count
# TODO Сами элементы, если они глобальные - меняются в момент работы цикла
# TODO ретурн же позволяет присвоить возвращенные элементы какой-нибудь переменной
# TODO например
# TODO элементы = create_snowflakes(20)
# TODO Если бы ретурна не было, элементы приравнялся бы к None
# TODO А в нашем случае туда запишется весь скоп значений, которые мы вернули)
# TODO Далее такая же логика. Тк здесь мы проходили глобальный оператор, можно делать через него, ретурны не нужны

def clear_snowflakes(x_list, y_list, size_list):
    # TODO То же кстати относится к параметрам. Если они работают с глобальными переменными - передавать их не надо
    # TODO Просто указываем global ... и используем
    for i, y in enumerate(y_list):
        if y_list[i] >= 30:
            point = sd.get_point(x_list[i], y_list[i])
            sd.snowflake(center=point, length=size_list[i], color=sd.background_color)
    return x_list, y_list, size_list


def move_snowflakes(x_list, y_list):
    for i, y in enumerate(y_list):
        if y_list[i] >= 30:
            y_list[i] -= sd.random_number(-5, 20)
            x_list[i] += sd.random_number(-15, 15)
    return x_list, y_list


def draw_snowflakes(x_list, y_list, size_list):
    for i, y in enumerate(y_list):
        if y_list[i] >= 30:
            point = sd.get_point(x_list[i], y_list[i])
            sd.snowflake(center=point, length=size_list[i], color=sd.COLOR_WHITE)
    return x_list, y_list, size_list


def fallen_snowflakes(x_list, y_list, size_list, new_list, count):
    for i, y in enumerate(y_list):
        if y_list[i] < 30:
            new_list.append(i)
            point1 = sd.get_point(x_list[i], y_list[i])
            sd.snowflake(center=point1, length=size_list[i], color=sd.background_color)
            sd.user_want_exit()
            print(new_list)
            count += 1
    return x_list, y_list, size_list, new_list, count


def remove_snowflakes(x_list, y_list, size_list, new_list):
    for index in reversed(new_list):
        size_list.pop(index)
        y_list.pop(index)
        x_list.pop(index)

    return x_list, y_list, size_list, new_list


def new_snowflakes(x_list, y_list, size_list, count):
    for list_create in range(count + 1):
        x_list.append(sd.random_number(10, 600))
        y_list.append(sd.random_number(600, 1200))
        size_list.append(sd.random_number(10, 50))
    return x_list, y_list, size_list, count
