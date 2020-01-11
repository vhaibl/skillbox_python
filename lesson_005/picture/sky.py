import simple_draw as sd
rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                      sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)
color_list = {'0': {'color_name': 'red', 'sd_name': sd.COLOR_RED},
                  '1': {'color_name': 'orange', 'sd_name': sd.COLOR_ORANGE},
                  '2': {'color_name': 'yellow', 'sd_name': sd.COLOR_YELLOW},
                  '3': {'color_name': 'green', 'sd_name': sd.COLOR_GREEN},
                  '4': {'color_name': 'cyan', 'sd_name': sd.COLOR_CYAN},
                  '5': {'color_name': 'blue', 'sd_name': sd.COLOR_BLUE},
                  '6': {'color_name': 'purple', 'sd_name': sd.COLOR_PURPLE}}
color_list2 = {'0': {'color_name': 'red', 'sd_name': sd.COLOR_DARK_RED},
                  '1': {'color_name': 'orange', 'sd_name': sd.COLOR_ORANGE},
                  '2': {'color_name': 'yellow', 'sd_name': sd.COLOR_DARK_YELLOW},
                  '3': {'color_name': 'green', 'sd_name': sd.COLOR_DARK_GREEN},
                  '4': {'color_name': 'cyan', 'sd_name': sd.COLOR_DARK_CYAN},
                  '5': {'color_name': 'blue', 'sd_name': sd.COLOR_DARK_BLUE},
                  '6': {'color_name': 'purple', 'sd_name': sd.COLOR_DARK_PURPLE}}
def rainbow():
    radius1 = 400
    for color in rainbow_colors:

        point = sd.get_point(1200, 1100)
        radius1 += 20
        circle = sd.circle(center_position=point, width=20, color=color, radius=radius1)

def sun():
    start = sd.get_point(100, 700)

    sd.circle(start, 50, sd.COLOR_YELLOW, 50)

    for i in range(0, 360, 30):
        sd.vector(start, i, 100, sd.COLOR_YELLOW, 5)

def sun2():
    start = sd.get_point(100, 700)

    sd.circle(start, 50, sd.COLOR_YELLOW, 50)

    for i in range(0, 360, 30):
        sd.vector(start, i+15, 100, sd.COLOR_YELLOW, 5)

