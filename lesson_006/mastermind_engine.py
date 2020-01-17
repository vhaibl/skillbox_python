# Составить отдельный модуль mastermind_engine, реализующий функциональность игры.
# В этом модуле нужно реализовать функции:
#   загадать_число()
#   проверить_число(NN) - возвращает словарь {'bulls': N, 'cows': N}
# Загаданное число хранить в глобальной переменной.
# Обратите внимание, что строки - это список символов.
MAX_SYMBOLS = 4
def make_a_number():
    pass

def guess_a_number():
    pass

def validator():
    global userinput
    userinput = input("загадай четырехзначное число с уникальными цифрами:")

    if len(userinput) != MAX_SYMBOLS:
        print('Ошибка! Неверное количество символов')
        validator()
    elif sorted(userinput) != sorted(set(userinput)):
        print('Есть одинаковые')
        validator()
    return userinput