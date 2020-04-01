# -*- coding: utf-8 -*-

import simple_draw as sd


# Шаг 1: Реализовать падение снежинки через класс. Внести в методы:
#  - создание снежинки с нужными параметрами
#  - отработку изменений координат
#  - отрисовку


class Snowflake:
    def __init__(self):
        self.x = sd.random_number(000, 600)
        self.y = sd.random_number(500, 600)
        self.point = sd.get_point(self.x, self.y)
        self.size = sd.random_number(10, 20)

    def clear_previous_picture(self):
        sd.snowflake(center=self.point, length=self.size, color=sd.background_color)

    def move(self):
        self.y -= sd.random_number(-5, 20)
        self.x += sd.random_number(-15, 15)
        self.point = sd.get_point(self.x, self.y)

    def draw(self):
        sd.snowflake(center=self.point, length=self.size, color=sd.COLOR_WHITE)

    def can_fall(self):
        return True if self.y > 0 else False


flake = Snowflake()

while True:
    flake.clear_previous_picture()
    flake.move()
    flake.draw()
    if not flake.can_fall():
        break
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

# шаг 2: создать снегопад - список объектов Снежинка в отдельном списке, обработку примерно так:
# flakes = get_flakes(count=N)  # создать список снежинок
# while True:
#     for flake in flakes:
#         flake.clear_previous_picture()
#         flake.move()
#         flake.draw()
#     fallen_flakes = get_fallen_flakes()  # подчитать сколько снежинок уже упало
#     if fallen_flakes:
#         append_flakes(count=fallen_flakes)  # добавить еще сверху
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break

sd.pause()
