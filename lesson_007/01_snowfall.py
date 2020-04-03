# -*- coding: utf-8 -*-

import simple_draw as sd

# Шаг 1: Реализовать падение снежинки через класс. Внести в методы:
#  - создание снежинки с нужными параметрами
#  - отработку изменений координат
#  - отрисовку
N = 10


class Snowflake:
    def __init__(self):
        self.x = sd.random_number(000, 600)
        self.y = sd.random_number(550, 1200)
        self.point = sd.get_point(self.x, self.y)
        self.size = sd.random_number(10, 20)

    def clear_previous_picture(self):
        sd.snowflake(center=self.point, length=self.size, color=sd.background_color)

    def move(self):
        self.y -= sd.random_number(0, 20)
        self.x += sd.random_number(-15, 15)
        self.point = sd.get_point(self.x, self.y)

    def draw(self):
        sd.snowflake(center=self.point, length=self.size, color=sd.COLOR_WHITE)

    def can_fall(self):
        return self.y > -100


flake = Snowflake()

while True:
    flake.clear_previous_picture()
    flake.move()
    flake.draw()
    if not flake.can_fall():
        break
    sd.sleep(0.01)
    if sd.user_want_exit():
        break




def get_flakes(count=N):
    global flakes_list
    flakes_list = []
    for i in range(count):
        flakes_list.append(Snowflake())
    return flakes_list


new_list = []


def get_fallen_flakes():
    global new_list
    new_list = []
    for i in flakes_list:
        if not flake.can_fall():
            new_list.append(i)
    return new_list
    # TODO Немогу понять, как правильно собирать индексы в текущей ситуации, вариант как в предыдущем модуле не катит
    # return fallen


def append_flakes(count):
    for _ in range(len(new_list)):
        if not flake.can_fall():
            flakes.append(Snowflake())


def remove_flakes():
    if not flake.can_fall():
        for _ in new_list:
            flakes.remove(_)
            # print(count)

flakes = get_flakes(count=N)  # создать список снежинок
while True:
    fallen = 0
    sd.start_drawing()

    for flake in flakes:
        flake.clear_previous_picture()
        flake.move()
        flake.draw()
        fallen_flakes = get_fallen_flakes()
    if fallen_flakes:
        remove_flakes()
        append_flakes(count=enumerate(fallen_flakes))

    sd.finish_drawing()
    sd.sleep(0.01)

    if sd.user_want_exit():
        break

sd.pause()

sd.pause()
