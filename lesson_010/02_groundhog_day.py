# -*- coding: utf-8 -*-

# День сурка
#
# Напишите функцию one_day() которая возвращает количество кармы от 1 до 7
# и может выкидывать исключения:
# - IamGodError
# - DrunkError
# - CarCrashError
# - GluttonyError
# - DepressionError
# - SuicideError
# Одно из этих исключений выбрасывается с вероятностью 1 к 13 каждый день
#
# Функцию оберните в бесконечный цикл, выход из которого возможен только при накоплении
# кармы до уровня ENLIGHTENMENT_CARMA_LEVEL. Исключения обработать и записать в лог.
# При создании собственных исключений максимально использовать функциональность
# базовых встроенных исключений.
from random import randint


class IamGodError(Exception):
    pass


class DrunkError(Exception):
    pass


class CarCrushError(Exception):
    pass


class GluttonyError(Exception):
    pass


class DepressionError(Exception):
    pass


class SuicideError(Exception):
    pass


def one_day():
    situation = randint(1, 6)
    if situation == 1:
        raise IamGodError("I am God")
    elif situation == 2:
        raise DrunkError("Got Drunk")
    elif situation == 3:
        raise CarCrushError("Crushed in a car")
    elif situation == 4:
        raise GluttonyError("Died from gluttony")
    elif situation == 5:
        raise DepressionError("Died in depression")
    elif situation == 6:
        raise SuicideError("Suicide death")


def day_by_day():
    carma = 0
    day = 0
    my_file = open('log_groundhound_day.txt', "w", encoding='utf-8')
    while carma < ENLIGHTENMENT_CARMA_LEVEL:
        chance = randint(1, 13)
        day += 1
        if chance == 1:
            try:
                one_day()
                carma = carma_gen(carma)
            except Exception as esc:
                out = 'Day ' + str(day) + ' : ' + str(esc)
                print(out)
                my_file.write(out + '\n')
        else:
            carma = carma_gen(carma)
        print('Day', day, 'carma:', carma)
    my_file.close()


def carma_gen(carma):
    if carma < 772:
        carma += randint(1, 7)
    else:
        carma = 777
    return carma


ENLIGHTENMENT_CARMA_LEVEL = 777
day_by_day()

# https://goo.gl/JnsDqu
#зачет!