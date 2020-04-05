# -*- coding: utf-8 -*-

from random import randint

# Доработать практическую часть урока lesson_007/python_snippets/08_practice.py

# Необходимо создать класс кота. У кота есть аттрибуты - сытость и дом (в котором он живет).
# Кот живет с человеком в доме.
# Для кота дом характеризируется - миской для еды и грязью.
# Изначально в доме нет еды для кота и нет грязи.

# Доработать класс человека, добавив методы
#   подобрать кота - у кота появляется дом.
#   купить коту еды - кошачья еда в доме увеличивается на 50, деньги уменьшаются на 50.
#   убраться в доме - степень грязи в доме уменьшается на 100, сытость у человека уменьшается на 20.
# Увеличить кол-во зарабатываемых человеком денег до 150 (он выучил пайтон и устроился на хорошую работу :)

# Кот может есть, спать и драть обои - необходимо реализовать соответствующие методы.
# Когда кот спит - сытость уменьшается на 10
# Когда кот ест - сытость увеличивается на 20, кошачья еда в доме уменьшается на 10.
# Когда кот дерет обои - сытость уменьшается на 10, степень грязи в доме увеличивается на 5
# Если степень сытости < 0, кот умирает.
# Так же надо реализовать метод "действуй" для кота, в котором он принимает решение
# что будет делать сегодня

# Человеку и коту надо вместе прожить 365 дней.

from random import randint

from termcolor import cprint


class Man:

    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = None
        self.cats = []

    def __str__(self):
        return 'Я - {}, сытость {}'.format(self.name, self.fullness)

    def eat(self):
        if self.house.food >= 10:
            cprint('{} поел'.format(self.name), color='yellow')
            self.fullness += 10
            self.house.food -= 10
        else:
            cprint('{} нет еды'.format(self.name), color='red')

    def work(self):
        cprint('{} сходил на работу'.format(self.name), color='blue')
        self.house.money += 150
        self.fullness -= 10

    def watch_MTV(self):
        cprint('{} смотрел MTV целый день'.format(self.name), color='green')
        self.fullness -= 10

    def shopping(self):
        if self.house.money >= 50:
            cprint('{} сходил в магазин за едой'.format(self.name), color='magenta')
            self.house.money -= 50
            self.house.food += 50
        else:
            cprint('{} деньги кончились!'.format(self.name), color='red')

    def zoo_shopping(self):
        if self.house.money >= 50:
            cprint('{} сходил в магазин за кошачим кормом'.format(self.name), color='magenta')
            self.house.money -= 50
            self.house.petfood += 50
        else:
            cprint('{} деньги кончились!'.format(self.name), color='red')

    def go_to_the_house(self, house):
        self.house = house
        self.fullness -= 10
        cprint('{} Вьехал в дом'.format(self.name), color='cyan')

    def get_a_pet(self, pet, house):
        pet.house = house
        self.cats.append(pet)
        cprint('{} Взял кота {}'.format(self.name, pet.name), color='cyan')

    def clean_mess(self):
        self.house.mess = 0
        self.fullness -= 20
        cprint('{} целый день убирался'.format(self.name), color='cyan')

    def act(self):
        if self.fullness <= 0:
            cprint('{} умер...'.format(self.name), color='red')
            return
        elif self.house.mess >= 100:
            cprint('{} задохнулся от грязи...'.format(self.name), color='red')
            return
        dice = randint(1, 6)
        if self.house.mess >= 90:
            self.clean_mess()
        elif self.fullness <= 30:
            self.eat()
        elif self.house.food <= 20:
            self.shopping()
        elif self.house.petfood <= 10:
            self.zoo_shopping()
        elif self.house.money < 100:
            self.work()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        else:
            self.watch_MTV()


class Pet:
    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = None

    def __str__(self):
        return 'Кот {}, сытость {}'.format(
            self.name, self.fullness)

    def eat(self):
        if self.house.petfood >= 10:
            cprint('Кот {} пожрал'.format(self.name), color='yellow')
            self.fullness += 20
            self.house.petfood -= 10

    def sleep(self):
        self.fullness -= 10
        cprint('Кот {} проспал весь день'.format(self.name), color='yellow')

    def tear_wallpaper(self):
        cprint('Кот {} весь день драл обои'.format(self.name), color='yellow')
        self.fullness -= 10
        self.house.mess += 5

    def act(self):
        if self.fullness <= 0:
            cprint('Кот {} умер от голода...'.format(self.name), color='red')
            return
        elif self.house.mess >= 100:
            cprint('Кот {} задохнулся от грязи...'.format(self.name), color='red')
            return
        dice = randint(1, 6)
        if self.fullness < 20:
            self.eat()
        elif dice == 1:
            self.tear_wallpaper()
        elif dice == 2:
            self.eat()
        else:
            self.sleep()


class House:

    def __init__(self):
        self.food = 50
        self.money = 0
        self.petfood = 50
        self.mess = 0

    def __str__(self):
        return 'В доме еды осталось {}, корма осталось {}, денег осталось {}, бардак {}%'.format(
            self.food, self.petfood, self.money, self.mess)


citizens = [Man(name='Бивис')]
pets = [Pet(name='Васька'), Pet(name='Мурзик'), Pet(name='Кузьмич')]
my_sweet_home = House()

for citisen in citizens:
    citisen.go_to_the_house(house=my_sweet_home)
    for cat in pets:
        citisen.get_a_pet(pet=cat, house=my_sweet_home)
    print('{} теперь не один, у него живут, живут коты'.format(citisen.name))
    for cat in citisen.cats:
        print(cat.name)
for day in range(1, 366):
    print('================ день {} =================='.format(day))
    for citisen in citizens:
        citisen.act()
    for cat in pets:
        cat.act()
    print('--- в конце дня ---')
    for citisen in citizens:
        print(citisen)
    for cat in pets:
        print(cat)
    print(my_sweet_home)

# Усложненное задание (делать по желанию)
# Создать несколько (2-3) котов и подселить их в дом к человеку.
# Им всем вместе так же надо прожить 365 дней.

# (Можно определить критическое количество котов, которое может прокормить человек...)
