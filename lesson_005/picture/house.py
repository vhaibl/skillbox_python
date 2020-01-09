# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd
#sd.resolution = (1200, 600)
def house():
    left_bottom = sd.get_point(375,0)
    sd.square(left_bottom, side=350, color=sd.COLOR_DARK_RED, width=0)


    for row, y in enumerate(range(0, 350, 25)):
        x0 = 0 if row % 2 else -25  # Как вам такой приём? :)
        x1 = x0 + 400
        for x in range(x1, 700, 50):
            point1 = sd.get_point(x, y)
            point2 = sd.get_point(x + 50, y + 25)
            brick = sd.rectangle(point1, point2, width=1, color=(127,127,127))

    left_bottom = sd.get_point(475,125)
    sd.square(left_bottom, side=150, color=sd.COLOR_BLACK, width=0)

    point1 = sd.get_point(350,350)
    point2 = sd.get_point(550,450)
    point3 = sd.get_point(750,350)
    point_list  = point1, point2, point3
    sd.polygon(point_list, color=sd.COLOR_DARK_ORANGE, width=0)



