import simple_draw as sd
rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                      sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

def rainbow():
    radius1 = 400
    for rainbow2 in rainbow_colors:

        point = sd.get_point(1200, 1100)
        radius1 += 20
        circle = sd.circle(center_position=point, width=20, color=rainbow2, radius=radius1)

def sun():
    start = sd.get_point(100, 700)
    sd.circle(start, 50, sd.COLOR_YELLOW, 50)

    for i in range(0, 360, 30):
        sd.vector(start, i, 100, sd.COLOR_YELLOW, 5)

