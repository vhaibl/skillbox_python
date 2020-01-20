import random

won = 0
MAX_SYMBOLS = 4

number = None


def make_a_number():
    global number
    number = []
    while len(set(number)) < MAX_SYMBOLS or number[0] == 0:
        number = [random.randint(0, 9) for n in range(MAX_SYMBOLS)]
    print(number)
    return number


def guess_a_number(userinput):
    if number == userinput:  # TODO Вот тут интересный момент. Это частный случай при проверке
        global won, cow, bull  # TODO Если с его помощью мы избегаем длительных вычислений - то оправдать
        won = 1  # TODO Такое действие можно...
        return won
    else:
        cow = 0
        bull = 0  # TODO ...НО. Если мы можем убрать проверку на частный случай и делать вывод на основе
        # TODO количества посчитанных быков - лучше так и поступить. Код станет меньше и понятнее.
        for x in range(0, MAX_SYMBOLS):
            if userinput[x] == number[x]:
                bull += 1
            elif userinput[x] in number:
                cow += 1
