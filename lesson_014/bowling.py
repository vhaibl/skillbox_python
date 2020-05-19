# -*- coding: utf-8 -*-


def convert(result):
    zeroes = result.replace("-", "0")
    strikes = zeroes.replace("X", "X0")
    converted = strikes.replace("Х", "X0")
    if '0' in result: raise ValueError('Invalid input data: 0 in data')

    if len(converted) != 20: raise ValueError('Not 10 frames')
    return converted


def chunks(s, n):
    for start in range(0, len(s), n):
        yield s[start:start + n]


def get_score(result):
    sum = 0
    for chunk in chunks(convert(result), 2):
        # print(chunk, end=' ')
        if 'X' in chunk[0] or 'Х' in chunk[0]:
            sum += 20
            # print(f'STRIKE!! 20 points and now sum is {sum}')

        elif 'X' in chunk[1] or 'Х' in chunk[1]:
            raise ValueError('Invalid input data: Strike in second throw')

        elif chunk.isdigit() and int(chunk[1]) > (9 - int(chunk[0])):
            raise ValueError('Invalid inout data: Too Many Pins')

        elif chunk.isdigit():
            score = (int(chunk[0]) + int(chunk[1]))
            sum += score
            # print(f'frame score {score} points and now sum is {sum}')

        elif '/' in chunk[0]:
            raise ValueError('Invalid input data: Spare In First Throw')

        elif '/' in chunk[-1]:
            sum += 15
            # print(f'SPARE! 15 ponts and now sum is {sum}')

        else:
            raise ValueError('Invalid input data')

    # print(f'Количество очков для результатов {result} - {sum}')
    return int(sum)


# result = get_score('55-/8/8/34X8/5/1854')  # Эта строка должна вызывать ошибку, сумма цифр фрэйма не должна
#                                            # превышать 9. Иначе это должен быть spare ("5/")
# print(result, '++++++++++++++++++++')
# result = get_score('1X18/8/34X8/5/1854')   # Страйк не может идти вторым броском
# print(result, '++++++++++++++++++++')
# result = get_score('011/8/34X8/5/185412')  # 0 не должно быть в строке, вместо них используются "-"
# print(result, '++++++++++++++++++++')
