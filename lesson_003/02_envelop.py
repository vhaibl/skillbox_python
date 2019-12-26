# -*- coding: utf-8 -*-

# (if/elif/else)

# Заданы размеры envelop_x, envelop_y - размеры конверта и paper_x, paper_y листа бумаги
#
# Определить, поместится ли бумага в конверте (стороны листа параллельны сторонам конверта)
#
# Результат проверки вывести на консоль (ДА/НЕТ)
# Использовать только операторы if/elif/else, можно вложенные
def test():
    if paper_x > envelop_x or paper_x > envelop_y:
        if paper_y > envelop_x or paper_y > envelop_y:
            print("НЕТ")
        else:
            print("ДА")
    else:
        print("ДА")


envelop_x, envelop_y = 10, 7
paper_x, paper_y = 8, 9
test()
# проверить для
paper_x, paper_y = 9, 8
test()
paper_x, paper_y = 6, 8
test()
paper_x, paper_y = 8, 6
test()
paper_x, paper_y = 3, 4
test()
paper_x, paper_y = 11, 9
test()
paper_x, paper_y = 9, 11
test()
# (просто раскоментировать нужную строку и проверить свой код)

# Усложненное задание, решать по желанию.
# Заданы размеры hole_x, hole_y прямоугольного отверстия и размеры brick_х, brick_у, brick_z кирпича (все размеры
# могут быть в диапазоне от 1 до 1000)
#
# Определить, пройдет ли кирпич через отверстие (грани кирпича параллельны сторонам отверстия)
print("----------------")


def test2():
    if (hole_x >= brick_x and hole_y >= brick_y) or (hole_x >= brick_y and hole_y >= brick_x) or (
            hole_x >= brick_x and hole_y >= brick_z) or (hole_x >= brick_z and hole_y >= brick_x) or (
            hole_x >= brick_z and hole_y >= brick_y) or (hole_x >= brick_y and hole_y >= brick_z):

        print('ДА')

    else:
        print("НЕТ")


hole_x, hole_y = 8, 9
brick_x, brick_y, brick_z = 11, 10, 2
test2()
brick_x, brick_y, brick_z = 11, 2, 10
test2()
brick_x, brick_y, brick_z = 10, 11, 2
test2()
brick_x, brick_y, brick_z = 10, 2, 11
test2()
brick_x, brick_y, brick_z = 2, 10, 11
test2()
brick_x, brick_y, brick_z = 2, 11, 10
test2()
brick_x, brick_y, brick_z = 3, 5, 6
test2()
brick_x, brick_y, brick_z = 3, 6, 5
test2()
brick_x, brick_y, brick_z = 6, 3, 5
test2()
brick_x, brick_y, brick_z = 6, 5, 3
test2()
brick_x, brick_y, brick_z = 5, 6, 3
test2()
brick_x, brick_y, brick_z = 5, 3, 6
test2()
brick_x, brick_y, brick_z = 11, 3, 6
test2()
brick_x, brick_y, brick_z = 11, 6, 3
test2()
brick_x, brick_y, brick_z = 6, 11, 3
test2()
brick_x, brick_y, brick_z = 6, 3, 11
test2()
brick_x, brick_y, brick_z = 3, 6, 11
test2()
brick_x, brick_y, brick_z = 3, 11, 6
test2()
# (просто раскоментировать нужную строку и проверить свой код)

#зачет!