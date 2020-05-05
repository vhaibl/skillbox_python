# -*- coding: utf-8 -*-


# Есть функция генерации списка простых чисел


def get_prime_numbers(n):
    prime_numbers = []
    for number in range(2, n + 1):
        for prime in prime_numbers:
            if number % prime == 0:
                break
        else:
            prime_numbers.append(number)
    return prime_numbers


# Часть 1
# На основе алгоритма get_prime_numbers создать класс итерируемых обьектов,
# который выдает последовательность простых чисел до n
#
# Распечатать все простые числа до 10000 в столбик
class PrimeNumbers:

    def __init__(self, n, zfilter):
        self.a = []
        self.n = n
        self.b = 1
        self.checklist = {'1': self.is_pal, '2': self.hasthreenines, '3': self.is_lucky,
                          '4': self.is_luckynines, '5': self.is_palnines, '6': self.is_luckypal}
        self.check = self.checklist[zfilter]

    def __iter__(self):
        self.b = 1
        return self

    def __next__(self):
        while True:
            self.b += 1
            self.strnumber = str(self.b)
            if self.b >= self.n:
                raise StopIteration()
            for number in self.a:
                if self.b % number == 0:
                    break
            else:
                self.a.append(self.b)
                if self.check(): return self.b

    def sum_digits(self, numn):
        return sum(map(int, numn))

    def hasthreenines(self):
        if '999' in str(self.b):
            return True

    def is_lucky(self):
        self.strnumber = str(self.b)
        center = len(self.strnumber) // 2
        return self.sum_digits(self.strnumber[:center]) == self.sum_digits(self.strnumber[-center:])

    def is_luckynines(self):
        self.strnumber = str(self.b)
        center = len(self.strnumber) // 2
        return self.sum_digits(self.strnumber[:center]) == self.sum_digits(self.strnumber[-center:]) \
               and '999' in str(self.b)

    def is_luckypal(self):
        self.strnumber = str(self.b)
        center = len(self.strnumber) // 2
        return self.sum_digits(self.strnumber[:center]) == self.sum_digits(self.strnumber[-center:]) \
               and str(self.b) == str(self.b)[::-1] and int(self.b) > 10

    def is_pal(self):
        return str(self.b) == str(self.b)[::-1] and int(self.b) > 10

    def is_palnines(self):
        return str(self.b) == str(self.b)[::-1] and int(self.b) > 10 and '999' in str(self.b)

    def nocheck(digit):
        return True


prime_number_iterator = PrimeNumbers(n=100000, zfilter='6')
print('Фильтры: 1 - Палиндромное, 2 - 999 в номере, 3 - Счастливое, 4 - Счастливое и 999, 5 - Палиндромное и 999,'
      ' 6 - Палиндромное и Счастлтивое')
for number in prime_number_iterator:
    print(number)


# Часть 2
# Теперь нужно создать генератор, который выдает последовательность простых чисел до n
# Распечатать все простые числа до 10000 в столбик

def prime_numbers_generator(n, filter1, filter2):
    a = 1
    prime_numb = []
    while True:
        a += 1
        for number in prime_numb:
            if a % number == 0:
                break
        else:
            prime_numb.append(a)
            if filter1(str(a)) and filter2(str(a)):
                yield a
        if a > n:
            return


def is_lucky(digit):
    center = len(digit) // 2
    return sum_digits(digit[:center]) == sum_digits(digit[-center:])


def is_pal(digit):
    return str(digit) == str(digit)[::-1] and int(digit) > 10


def hasthreethrees(digit):
    if '333' in digit:
        return True


def nocheck(digit):
    return True


def sum_digits(digit):
    return sum(map(int, digit))


for number in prime_numbers_generator(n=100000, filter1=hasthreethrees, filter2=is_pal):
    print(number)

# Сделал фильтры счатливого, палиндромного и наличия 999 в числе, добавил их в генератор и итератор, сделал
# возможость запускать несколько фильтров на выбор
# Насчет "придумать свою" прошу предложить какой тип число выбрать, если проверки на 999 недостаточно,
# выбирать в википедии то, что может подойти, не очень просто
# Достаточно будет и такого) хотя конечно можно выбрать что-то поинтереснее при желании
# Часть 3
# Написать несколько функций-фильтров, которые выдает True, если число:
# 1) "счастливое" в обыденном пониманиии - сумма первых цифр равна сумме последних
#       Если число имеет нечетное число цифр (например 727 или 92083),
#       то для вычисления "счастливости" брать равное количество цифр с начала и конца:
#           727 -> 7(2)7 -> 7 == 7 -> True
#           92083 -> 92(0)83 -> 9+2 == 8+3 -> True
# 2) "палиндромное" - одинаково читающееся в обоих направлениях. Например 723327 и 101
# 3) придумать свою (https://clck.ru/GB5Fc в помощь)
#
# Подумать, как можно применить функции-фильтры к полученной последовательности простых чисел
# для получения, к примеру: простых счастливых чисел, простых палиндромных чисел,
# простых счастливых палиндромных чисел и так далее. Придумать не менее 2х способов.
#
# Подсказка: возможно, нужно будет добавить параметр в итератор/генератор.
#зачет!