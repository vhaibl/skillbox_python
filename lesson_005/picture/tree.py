import simple_draw as sd


def draw_bunches(start_point, angle, length, color):
    if length < 15:
        color = sd.COLOR_GREEN
    if length < 3:
        return
    v1 = sd.get_vector(start_point=start_point, angle=angle, length=length, width=1)
    v1.draw(color)
    angle1 = (angle - 30) * (1 + (sd.random_number(-2, 2) / 100))
    angle2 = (angle + 30) * (1 + (sd.random_number(-2, 2) / 100))
    next_point = v1.end_point
    next_length = length * 0.75 * (1 + (sd.random_number(-2, 2) / 100))
    draw_bunches(start_point=next_point, angle=angle1, length=next_length, color=color)
    draw_bunches(start_point=next_point, angle=angle2, length=next_length, color=color)


def tree():
    tree_clear = sd.get_point(700, 0)
    sd.square(tree_clear, side=550, color=sd.background_color, width=0)
    root_point = sd.get_point(900, 30)
    color = sd.COLOR_DARK_YELLOW
    draw_bunches(start_point=root_point, angle=90, length=80, color=color)


def tree2():
    root_point = sd.get_point(1100, 00)
    color = sd.COLOR_DARK_RED
    draw_bunches(start_point=root_point, angle=90, length=50, color=color)
