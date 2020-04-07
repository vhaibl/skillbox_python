# -*- coding: utf-8 -*-

from termcolor import cprint
from random import randint


class House:

    def __init__(self):
        self.money = 100
        self.food = 50
        self.petfood = 30
        self.mess = 0
        self.total_got_money = 0
        self.total_food_eaten = 0
        self.total_furcoats_purchased = 0
        pass

    def __str__(self):
        return 'В тумбочке {} денег, в холодильнике {} еды, кошачего корма {}, бардак в доме {}%'.format \
            (self.money, self.food, self.petfood, self.mess)


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

    def pet_the_cat(self):
        self.fullness -= 10
        self.happiness += 5
        print('{} играл(а) с котом'.format(self.name))

    def go_to_the_house(self, house):
        self.house = house
        self.fullness -= 10

        cprint('{} теперь живет в доме'.format(self.name), color='cyan')

    def act(self):
        if self.house.mess >= 80: self.happiness -= 10
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
            elif self.house.money <= 100:
                self.work()
            else:
                if dice == 1:
                    self.work()
                elif dice == 2:
                    self.work()
                elif dice == 3:
                    self.pet_the_cat()
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
            elif self.happiness <= 40:
                self.buy_fur_coat()
                return
            elif self.house.petfood <= 10:
                self.zooshopping()
                return
            elif self.house.mess >= 70:
                self.clean_house()
            else:
                if dice == 1:
                    self.eat()
                elif dice == 2:
                    self.shopping()
                elif dice == 3:
                    self.clean_house()
                elif dice == 4 and self.house.money >= 500:
                    self.buy_fur_coat()

                else:
                    self.pet_the_cat()

    def shopping(self):
        if self.house.money >= 50:
            self.fullness -= 10
            self.house.money -= 50
            self.house.food += 50
            print('{} сходила в магазин за едой'.format(self.name))
        else:
            print('Нет денег')

    def zooshopping(self):
        if self.house.money >= 50:
            self.fullness -= 10
            self.house.money -= 50
            self.house.petfood += 50
            print('{} звкупилась кошачим кормом'.format(self.name))
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


class Cat:

    def __init__(self, name):
        self.name = name
        self.fullness = 30
        self.house = None

    def __str__(self):
        return '{} - сытость {}'.format(self.name, self.fullness)

    def act(self):
        if self.fullness <= 0:
            cprint('Кот {} умер от голода...'.format(self.name), color='red')
            return
        elif self.house.mess >= 100:
            cprint('Кот {} задохнулся от грязи...'.format(self.name), color='red')
            return
        dice = randint(1, 6)
        if self.fullness <= 10:
            self.eat()
        elif dice == 1:
            self.soil()
        elif dice == 2:
            self.eat()
        else:
            self.sleep()

    def eat(self):
        if self.house.petfood >= 10:
            cprint('Кот {} пожрал'.format(self.name), color='yellow')
            self.fullness += 20
            self.house.petfood -= 10

    def sleep(self):
        self.fullness -= 10
        cprint('Кот {} проспал весь день'.format(self.name), color='yellow')

    def soil(self):
        cprint('Кот {} весь день драл обои'.format(self.name), color='yellow')
        self.fullness -= 10
        self.house.mess += 5

    def go_to_the_house(self, house):
        self.house = house
        self.fullness -= 10
        cprint('Кот {} теперь живет в доме'.format(self.name), color='cyan')


home = House()
serge = Husband(name='Сережа')
masha = Wife(name='Маша')
tomas = Cat(name='Томас')
serge.go_to_the_house(home)
masha.go_to_the_house(home)
tomas.go_to_the_house(home)

for day in range(365):
    cprint('================== День {} =================='.format(day), color='red')
    if home.mess >= 95:
        home.mess == 100  # TODO Просмотрел видимо где-то этот момент
        # TODO Это действие само по себе сравнивает грязь в доме с 100
        # TODO Тут скорее надо заменить == на =
        # TODO А вообще этот метод хорошо бы в дом убрать, что-то вроде home.act()
    else:
        home.mess += 5
    serge.act()
    masha.act()
    tomas.act()
    cprint(serge, color='cyan')
    cprint(masha, color='cyan')
    cprint(tomas, color='cyan')
    cprint(home, color='cyan')
print("Съедено {} еды".format(home.total_food_eaten))
print("{} денег заработано".format(home.total_got_money))
print("{} шуб куплено".format(home.total_furcoats_purchased))

# # TODO после правки можете сливать ветки
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
# class Child:
#
#     def __init__(self):
#         pass
#
#     def __str__(self):
#         return super().__str__()
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
