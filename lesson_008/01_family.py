# -*- coding: utf-8 -*-

from termcolor import cprint
from random import randint


######################################################## Часть первая
#
# Создать модель жизни небольшой семьи.
#
# Каждый день участники жизни могут делать только одно действие.
# Все вместе они должны прожить год и не умереть.
#
# Муж может:
#   есть,
#   играть в WoT,
#   ходить на работу,
# Жена может:
#   есть,
#   покупать продукты,
#   покупать шубу,
#   убираться в доме,

# Все они живут в одном доме, дом характеризуется:
#   кол-во денег в тумбочке (в начале - 100)
#   кол-во еды в холодильнике (в начале - 50)
#   кол-во грязи (в начале - 0)
#
# У людей есть имя, степень сытости (в начале - 30) и степень счастья (в начале - 100).
#
# Любое действие, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Кушают взрослые максимум по 30 единиц еды, степень сытости растет на 1 пункт за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе чел умрет от голода.
#
# Деньги в тумбочку добавляет муж, после работы - 150 единиц за раз.
# Еда стоит 10 денег 10 единиц еды. Шуба стоит 350 единиц.
#
# Грязь добавляется каждый день по 5 пунктов, за одну уборку жена может убирать до 100 единиц грязи.
# Если в доме грязи больше 90 - у людей падает степень счастья каждый день на 10 пунктов,
# Степень счастья растет: у мужа от игры в WoT (на 20), у жены от покупки шубы (на 60, но шуба дорогая)
# Степень счастья не должна падать ниже 10, иначе чел умрает от депресии.
#
# Подвести итоги жизни за год: сколько было заработано денег, сколько сьедено еды, сколько куплено шуб.


class House:

    def __init__(self):
        self.money = 100
        self.food = 50
        self.mess = 0
        self.total_got_money = 0
        self.total_food_eaten = 0
        self.total_furcoats_purchased = 0
        pass

    def __str__(self):
        return 'В тумбочке {} денег, в холодильнике {} еды, бардак в доме {}%'.format(self.money, self.food, self.mess)


class Man:

    def __init__(self, name):
        self.fullness = 30
        self.happiness = 100
        self.name = name
        self.alive = True

    def __str__(self):
        return '{} - сытость {}, счастье {}'.format(self.name, self.fullness, self.happiness)

    def eat(self):
        if self.house.food >= 10:
            self.fullness += 10
            self.house.food -= 10
            self.house.total_food_eaten += 10
            print('{} поел(а)'.format(self.name))
        else:
            print('Нет еды')

    def go_to_the_house(self, house):
        self.house = house
        self.fullness -= 10

        cprint('{} теперь живет в доме'.format(self.name), color='cyan')

    def act(self):
        if self.house.mess >= 70: self.happiness -= 10
        if self.fullness <= 0:
            cprint('{} умер(ла) от голода...'.format(self.name), color='red')
            return
        elif self.house.mess >= 100:
            cprint('{} задохнулся(ась) от грязи...'.format(self.name), color='red')
            return
        elif self.happiness <= 10:
            cprint('{} повесился(ась)...'.format(self.name), color='red')
            return
        if self.fullness <= 0 or self.house.mess >= 100 or self.happiness <= 10:
            return False
        else:
            return True


class Husband(Man):

    def act(self):
        if super().act() is True:
            dice = randint(1, 6)
            if self.fullness <= 20:
                self.eat()
            elif self.house.money <= 50:
                self.work()
            else:
                if dice == 1:
                    self.work()
                elif dice == 2:
                    self.work()
                else:
                    self.gaming()
        else:
            return

    def work(self):
        self.fullness -= 10
        self.house.money += 150
        print('{} весь день работал'.format(self.name))
        self.house.total_got_money += 150

    def gaming(self):
        self.fullness -= 10
        self.happiness += 20
        print('{} весь день играл в World of Tanks'.format(self.name))


class Wife(Man):

    def act(self):
        if super().act() is True:
            dice = randint(1, 6)
            if self.fullness <= 20:
                self.eat()
                return
            elif self.house.food <= 50:
                self.shopping()
                return
            elif self.happiness <= 30:
                self.buy_fur_coat()
                return
            else:
                if dice == 1:
                    self.eat()
                elif dice == 2:
                    self.shopping()
                else:
                    self.clean_house()

    def shopping(self):
        if self.house.money >= 50:
            self.fullness -= 10
            self.house.money -= 50
            self.house.food += 50
            print('{} сходила в магазин за едой'.format(self.name))
        else:
            print('Нет денег')

    def buy_fur_coat(self):
        if self.house.money < 350:
            print('{} хотела купить шубу, но у нее нет денег!'.format(self.name))
        else:
            self.fullness -= 10
            self.house.money -= 350
            self.happiness += 60
            self.house.total_furcoats_purchased += 1

            print('{} купила шубу'.format(self.name))

    def clean_house(self):
        self.fullness -= 10
        self.house.mess = 0
        print('{} убралась в доме'.format(self.name))


class Child(Man):

    def act(self):
        if self.fullness <= 10:
            self.eat()
            return
        dice = randint(1, 2)

        if dice == 1:
            self.eat()
        elif dice == 2:
            self.sleep()

    def eat(self):
        if self.house.food >= 10:
            self.fullness += 10
            self.house.food -= 10
            self.house.total_food_eaten += 10
            print('{} поел(а)'.format(self.name))
        else:
            print('Нет еды')

    def sleep(self):
        self.fullness -= 10
        print('{} весь день спал'.format(self.name))


home = House()
serge = Husband(name='Сережа')
masha = Wife(name='Маша')
kolya = Child(name='Коля')

serge.go_to_the_house(home)
masha.go_to_the_house(home)
kolya.go_to_the_house(home)

for day in range(365):
    cprint('================== День {} =================='.format(day), color='red')
    if home.mess >= 95:
        home.mess == 100
    else:
        home.mess += 5
    serge.act()
    masha.act()
    kolya.act()
    cprint(serge, color='cyan')
    cprint(masha, color='cyan')
    cprint(kolya, color='cyan')
    cprint(home, color='cyan')
print("Съедено {} еды".format(home.total_food_eaten))
print("{} денег заработано".format(home.total_got_money))
print("{} шуб куплено".format(home.total_furcoats_purchased))

# # TODO после реализации первой части - отдать на проверку учителю
#
# ######################################################## Часть вторая
# #
# # После подтверждения учителем первой части надо
# # отщепить ветку develop и в ней начать добавлять котов в модель семьи
# #
# # Кот может:
# #   есть,
# #   спать,
# #   драть обои
# #
# # Люди могут:
# #   гладить кота (растет степень счастья на 5 пунктов)
# #
# # В доме добавляется:
# #   еда для кота (в начале - 30)
# #
# # У кота есть имя и степень сытости (в начале - 30)
# # Любое действие кота, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# # Еда для кота покупается за деньги: за 10 денег 10 еды.
# # Кушает кот максимум по 10 единиц еды, степень сытости растет на 2 пункта за 1 пункт еды.
# # Степень сытости не должна падать ниже 0, иначе кот умрет от голода.
# #
# # Если кот дерет обои, то грязи становится больше на 5 пунктов
#
#
# class Cat:
#
#     def __init__(self):
#         pass
#
#     def act(self):
#         pass
#
#     def eat(self):
#         pass
#
#     def sleep(self):
#         pass
#
#     def soil(self):
#         pass
#
#
# ######################################################## Часть вторая бис
# #
# # После реализации первой части надо в ветке мастер продолжить работу над семьей - добавить ребенка
# #
# # Ребенок может:
# #   есть,
# #   спать,
# #
# # отличия от взрослых - кушает максимум 10 единиц еды,
# # степень счастья  - не меняется, всегда ==100 ;)
#

# # TODO после реализации второй части - отдать на проверку учителем две ветки
#
#
# ######################################################## Часть третья
# #
# # после подтверждения учителем второй части (обоих веток)
# # влить в мастер все коммиты из ветки develop и разрешить все конфликты
# # отправить на проверку учителем.
#
#
# home = House()
# serge = Husband(name='Сережа')
# masha = Wife(name='Маша')
# kolya = Child(name='Коля')
# murzik = Cat(name='Мурзик')
#
# for day in range(365):
#     cprint('================== День {} =================='.format(day), color='red')
#     serge.act()
#     masha.act()
#     kolya.act()
#     murzik.act()
#     cprint(serge, color='cyan')
#     cprint(masha, color='cyan')
#     cprint(kolya, color='cyan')
#     cprint(murzik, color='cyan')
#
#
# # Усложненное задание (делать по желанию)
# #
# # Сделать из семьи любителей котов - пусть котов будет 3, или даже 5-10.
# # Коты должны выжить вместе с семьей!
# #
# # Определить максимальное число котов, которое может прокормить эта семья при значениях зарплаты от 50 до 400.
# # Для сглаживание случайностей моделирование за год делать 3 раза, если 2 из 3х выжили - считаем что выжили.
# #
# # Дополнительно вносить некий хаос в жизнь семьи
# # - N раз в год вдруг пропадает половина еды из холодильника (коты?)
# # - K раз в год пропадает половина денег из тумбочки (муж? жена? коты?!?!)
# # Промоделировать - как часто могут случаться фейлы что бы это не повлияло на жизнь героев?
# #   (N от 1 до 5, K от 1 до 5 - нужно вычислит максимумы N и K при котором семья гарантированно выживает)
# #
# # в итоге должен получится приблизительно такой код экспериментов
# # for food_incidents in range(6):
# #   for money_incidents in range(6):
# #       life = Simulation(money_incidents, food_incidents)
# #       for salary in range(50, 401, 50):
# #           max_cats = life.experiment(salary)
# #           print(f'При зарплате {salary} максимально можно прокормить {max_cats} котов')
#
