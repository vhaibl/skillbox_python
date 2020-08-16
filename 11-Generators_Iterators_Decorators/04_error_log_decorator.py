# -*- coding: utf-8 -*-

# Написать декоратор, который будет логировать (записывать в лог файл)
# ошибки из декорируемой функции и выбрасывать их дальше.
#
# Имя файла лога - function_errors.log
# Формат лога: <имя функции> <параметры вызова> <тип ошибки> <текст ошибки>
# Лог файл открывать каждый раз при ошибке в режиме 'a'

def get_log_errors(filename):
    def log_errors(func):
        def wrapped(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except ValueError as e:
                with open(filename, 'a') as a:
                    a.write(f"{func} {args} {kwargs} ValueError: {e}" + "\n")
                raise ValueError(f'{e}')
            except ZeroDivisionError as e:
                print(f'ZeroDivisionError: {e}')
                with open(filename, 'a') as a:
                    a.write(f"{func} {args} {kwargs} ZeroDivisionError: {e}" + "\n")
                raise ZeroDivisionError

        return wrapped

    return log_errors


# Проверить работу на следующих функциях
@get_log_errors('function_errors_1.log')
def perky(param):
    return param / 0


@get_log_errors('function_errors_2.log')
def check_line(line):
    name, email, age = line.split(' ')
    if not name.isalpha():
        raise ValueError("it's not a name")
    if '@' not in email or '.' not in email:
        raise ValueError("it's not a email")
    if not 10 <= int(age) <= 99:
        raise ValueError('Age not in 10..99 range')


lines = [
    'Ярослав bxh@ya.ru 600',
    'Земфира tslzp@mail.ru 52',
    'Тролль nsocnzas.mail.ru 82',
    'Джигурда wqxq@gmail.com 29',
    'Земфира 86',
    'Равшан wmsuuzsxi@mail.ru 35',
]
for line in lines:
    try:
        check_line(line)
    except Exception as exc:
        print(f'Invalid format: {exc}')
perky(param=42)
# Усложненное задание (делать по желанию).
# Написать декоратор с параметром - именем файла
#
# @log_errors('function_errors.log')
# def func():
#     pass
#зачет!