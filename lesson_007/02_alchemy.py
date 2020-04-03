# -*- coding: utf-8 -*-

# Создать прототип игры Алхимия: при соединении двух элементов получается новый.
# Реализовать следующие элементы: Вода, Воздух, Огонь, Земля, Шторм, Пар, Грязь, Молния, Пыль, Лава.
# Каждый элемент организовать как отдельный класс.
# Таблица преобразований:
#   Вода + Воздух = Шторм
#   Вода + Огонь = Пар
#   Вода + Земля = Грязь
#   Воздух + Огонь = Молния
#   Воздух + Земля = Пыль
#   Огонь + Земля = Лава

# Сложение элементов реализовывать через __add__
# Если результат не определен - то возвращать None
# Вывод элемента на консоль реализовывать через __str__
#
# Примеры преобразований:

#   print(Fire(), '+', Air(), '=', Fire() + Air())

class Water:

    def __str__(self):
        return 'Вода'

    def __add__(self, other):
        if isinstance(other, Air):
            return Storm(self, Air)
        elif isinstance(other, Fire):
            return Steam(self, Fire)
        elif isinstance(other, Earth):
            return Mood(self, Earth)
        else:
            return None



class Air:

    def __str__(self):
        return 'Воздух'

    def __add__(self, other):
        if isinstance(other, Fire):
            return Lightning(self, Fire)
        elif isinstance(other, Earth):
            return Dust(self, Earth)
        elif isinstance(other, Water):
            return Storm(self, Water)
        elif isinstance(other, Life):
            return Angel(self, Life)
        else:
            return None


class Fire:

    def __str__(self):
        return 'Огонь'

    def __add__(self, other):
        if isinstance(other, Earth):
            return Lava(self, Earth)
        elif isinstance(other, Water):
            return Lava(self, Water)
        elif isinstance(other, Air):
            return Lava(self, Air)
        elif isinstance(other, Life):
            return Phoenix(self, Life)
        else:
            return None


class Earth:

    def __str__(self):
        return 'Земля'

    def __add__(self, other):
        if isinstance(other, Fire):
            return Lava(self, Fire)
        elif isinstance(other, Water):
            return Mood(self, Water)
        elif isinstance(other, Air):
            return Dust(self, Air)
        elif isinstance(other, Life):
            return Troll(self, Life)
        else:
            return None


class Storm:

    def __init__(self, part1, part2):
        self.part1 = Water
        self.part2 = Air

    def __str__(self):
        return 'Шторм'


class Steam:

    def __init__(self, part1, part2):
        self.part1 = Air
        self.part2 = Fire

    def __str__(self):
        return 'Пар'


class Mood:

    def __init__(self, part1, part2):
        self.part1 = Air
        self.part2 = Earth

    def __str__(self):
        return 'Грязь'


class Lightning:

    def __init__(self, part1, part2):
        self.part1 = Air
        self.part2 = Fire

    def __str__(self):
        return 'Молния'


class Dust:

    def __init__(self, part1, part2):
        self.part1 = Air
        self.part2 = Earth

    def __str__(self):
        return 'Пыль'


class Lava:

    def __init__(self, part1, part2):
        self.part1 = Fire
        self.part2 = Earth

    def __str__(self):
        return 'Лава'


class Life:

    def __str__(self):
        return 'Жизнь'

    def __add__(self, other):
        if isinstance(other, Fire):
            return Phoenix(self, Fire)
        if isinstance(other, Earth):
            return Troll(self, Earth)
        if isinstance(other, Air):
            return Angel(self, Air)
        if isinstance(other, Water):
            return Mermaid(self, Water)


class Phoenix:

    def __init__(self, part1, part2):
        self.part1 = Fire
        self.part2 = Life

    def __str__(self):
        return 'Феникс'


class Troll:

    def __init__(self, part1, part2):
        self.part1 = Life
        self.part2 = Earth

    def __str__(self):
        return 'Тролль'


class Angel:

    def __init__(self, part1, part2):
        self.part1 = Air
        self.part2 = Life

    def __str__(self):
        return 'Ангел'


class Mermaid:

    def __init__(self, part1, part2):
        self.part1 = Water
        self.part2 = Life

    def __str__(self):
        return 'Русалка'


print(Water(), '+', Air(), '=', Water() + Air())
print(Water(), '+', Fire(), '=', Water() + Fire())
print(Water(), '+', Earth(), '=', Water() + Earth())
print(Air(), '+', Fire(), '=', Air() + Fire())
print(Air(), '+', Earth(), '=', Air() + Earth())
print(Fire(), '+', Earth(), '=', Fire() + Earth())
print(Life(), '+', Air(), '=', Life() + Air())
print(Life(), '+', Earth(), '=', Life() + Earth())
print(Life(), '+', Water(), '=', Life() + Water())
print(Life(), '+', Fire(), '=', Life() + Fire())
print(Life(), '+', Life(), '=', Life() + Life())
# Усложненное задание (делать по желанию)
# Добавить еще элемент в игру.
# Придумать что будет при сложении существующих элементов с новым.
#Зачет!