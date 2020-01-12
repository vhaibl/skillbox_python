import simple_draw as sd


def smile1(color, x, y):
    point = sd.get_point(x, y)
    line_x = x
    line_y = y
    x -= 25
    y += 15
    point1 = sd.get_point(x, y)
    x += 50
    point2 = sd.get_point(x, y)

    sd.circle(center_position=point, color=color, radius=50)
    sd.circle(center_position=point1, radius=10, color=color)
    sd.circle(center_position=point2, radius=10, color=color)
    line_x -= 25
    line_y -= 15
    line1 = sd.get_point(line_x, line_y)
    line_x += 15
    line_y -= 15
    line2 = sd.get_point(line_x, line_y)
    line_x += 20
    line3 = sd.get_point(line_x, line_y)
    line_x += 15
    line_y += 15
    line4 = sd.get_point(line_x, line_y)
    sd.lines(point_list=(line1, line2, line3, line4), color=color)


def smile2(color, x, y):
    point = sd.get_point(x, y)
    line_x = x
    line_y = y
    x -= 25
    y += 15
    point1 = sd.get_point(x, y)
    x += 50
    point2 = sd.get_point(x, y)

    sd.circle(center_position=point, color=color, radius=50)
    sd.circle(center_position=point1, radius=10, color=color)
    sd.circle(center_position=point2, radius=1, color=color)
    line_x -= 25
    line_y -= 15
    line1 = sd.get_point(line_x, line_y)
    line_x += 15
    line_y -= 15
    line2 = sd.get_point(line_x, line_y)
    line_x += 20
    line3 = sd.get_point(line_x, line_y)
    line_x += 15
    line_y += 15
    line4 = sd.get_point(line_x, line_y)
    sd.lines(point_list=(line1, line2, line3, line4), color=color)


def smile(counter):
    if counter % 5:
        smile2(color=sd.COLOR_DARK_YELLOW, x=550, y=200)
    else:
        smile1(color=sd.COLOR_DARK_YELLOW, x=550, y=200)
