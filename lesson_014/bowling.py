# -*- coding: utf-8 -*-


def convert(result):
    zeroes = result.replace("-", "0")
    strikes = zeroes.replace("X", "X0")
    converted = strikes.replace("Х", "X0")
    if len(converted) != 20: raise ValueError('Not 10 frames')
    return converted


def chunks(s, n):
    for start in range(0, len(s), n):
        yield s[start:start + n]


def get_score(result):
    sum = 0
    for chunk in chunks(convert(result), 2):
        print(chunk, end=' ')
        if 'X' in chunk or 'Х' in chunk:
            sum += 20
            print(f'STRIKE!! 20 points and now sum is {sum}')
        elif chunk.isdigit() and int(chunk[1]) > (10 - int(chunk[0])):
            raise ValueError('Invalid inout data: Too Many Pins')

        elif chunk.isdigit():
            score = (int(chunk[0]) + int(chunk[1]))
            sum += score
            print(f'frame score {score} points and now sum is {sum}')
        elif '/' in chunk[0]:
            raise ValueError('Invalid input data: Spare In First Throw')

        elif '/' in chunk[-1]:
            sum += 15
            print(f'SPARE! 15 ponts and now sum is {sum}')
        else:
            raise ValueError('Invalid input data')

    print(f'Количество очков для результатов {result} - {sum}')
    return sum


result = get_score('55-/8/8/34X8/5/1854')  # TODO Эта строка должна вызывать ошибку, сумма цифр фрэйма не должна
# TODO превышать 9. Иначе это должен быть spare ("5/")
print(result, '++++++++++++++++++++')
result = get_score('1X18/8/34X8/5/1854')  # TODO Страйк не может идти вторым броском
print(result, '++++++++++++++++++++')
result = get_score('011/8/34X8/5/185412')  # TODO 0 не должно быть в строке, вместо них используются "-"
print(result, '++++++++++++++++++++')
