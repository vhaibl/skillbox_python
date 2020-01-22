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


def fallen_snowflakes(new_list):  # А вот здесь и далее, убрать new_list и count не получается...
    # count можно попросту удалить, нам особо не нужна эта информация
    # а new_list можно создавать заново внутри этой функции new_list = []
    # И его тогда возвращать return-ом, чтобы потом передавать этот список в функцию удаления
    # Что-то все равно не понятно. Count-ом у меня добавляются новые снежинки в список, получается нельзя убирать
    # его полностью.
    # А как только я пробую убрать new_list из параметров в глобальную переменную - он начинает распухать...

    global x_list, y_list, size_list, count
    # TODO После того, как убираете его из параметров
    # TODO Вы вот тут new_list обновляйте
    # TODO new_list = []
    # TODO По сути его и глобальным делать не нужно
    # TODO Просто тут сперва создаете пустой список, затем заполняете, затем отдаёте ретурном
    # TODO А уже в следующей функции используете
    # TODO Кстати вместо count можно использовать длину списка, который вернулся из этой функции
    for i, y in enumerate(y_list):
        if y_list[i] < 30:
            new_list.append(i)
            point1 = sd.get_point(x_list[i], y_list[i])
            sd.snowflake(center=point1, length=size_list[i], color=sd.background_color)
            sd.user_want_exit()
            print(new_list)
            count += 1
    #return new_list


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
