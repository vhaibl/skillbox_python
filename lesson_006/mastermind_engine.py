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
    if number == userinput:
        global won, cow, bull
        won = 1
        return won
    else:
        cow = 0
        bull = 0

        for x in range(0, MAX_SYMBOLS):
            if userinput[x] == number[x]:
                bull += 1
            elif userinput[x] in number:
                cow += 1
