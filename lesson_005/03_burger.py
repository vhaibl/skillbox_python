# -*- coding: utf-8 -*-

# Создать модуль my_burger. В нем определить функции добавления инградиентов:
#  - булочки
#  - котлеты
#  - огурчика
#  - помидорчика
#  - майонеза
#  - сыра
# В каждой функции выводить на консоль что-то вроде "А теперь добавим ..."

# В этом модуле создать рецепт двойного чизбургера (https://goo.gl/zA3goZ)
# с помощью фукций из my_burger и вывести на консоль.

# Создать рецепт своего бургера, по вашему вкусу.
# Если не хватает инградиентов - создать соответствующие функции в модуле my_burger

# TODO здесь ваш код
import my_burger
# TODO И тут попробуйте from ... import func1, func2, func3.... очень удобная фича)
# TODO Кроме прочему конкретный импорт всегда лучше - тк он не забивает глобальное пространство имён
# TODO Другими словами не импортирует ничего лишнего, если оно там есть
# TODO Особенно важно это при работе с большими библиотеками
my_burger.buns()
my_burger.cutlets()
my_burger.onion()
my_burger.cucumber()
my_burger.tomato()
my_burger.cheese()
my_burger.mayo()