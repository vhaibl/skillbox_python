# -*- coding: utf-8 -*-

# Есть файл с протоколом регистраций пользователей на сайте - registrations.txt
# Каждая строка содержит: ИМЯ ЕМЕЙЛ ВОЗРАСТ, разделенные пробелами
# Например:
# Василий test@test.ru 27
#
# Надо проверить данные из файла, для каждой строки:
# - присутсвуют все три поля
# - поле имени содержит только буквы
# - поле емейл содержит @ и .
# - поле возраст является числом от 10 до 99
#
# В результате проверки нужно сформировать два файла
# - registrations_good.log для правильных данных, записывать строки как есть
# - registrations_bad.log для ошибочных, записывать строку и вид ошибки.
#
# Для валидации строки данных написать метод, который может выкидывать исключения:
# - НЕ присутсвуют все три поля: ValueError
# - поле имени содержит НЕ только буквы: NotNameError (кастомное исключение)
# - поле емейл НЕ содержит @ и .(точку): NotEmailError (кастомное исключение)
# - поле возраст НЕ является числом от 10 до 99: ValueError
# Вызов метода обернуть в try-except.
class NotNameError(Exception):
    pass


class NotEmailError(Exception):
    pass


def validate(line):
    username, email, age = line.split(' ')
    age = int(age)

    if username.isalpha() is False:
        raise NotNameError
    elif '@' not in email and '.' not in email:
        raise NotEmailError
    elif age < 10 or age > 99:
        raise ValueError('Bad Age')


def check_regs(filename):
    with open(filename, 'r', encoding='utf8') as ff:
        count = 0
        bad_regs = open('registrations_bad.log  ', "w", encoding='utf-8')
        good_regs = open('registrations_good.log', "w", encoding='utf-8')
        for line in ff:
            line = line[:-1]
            count += 1
            try:
                validate(line)
                good_regs.write(line + '\n')
            except ValueError as exc:
                if 'unpack' in exc.args[0]:
                    valerror = f'Не хватает данных в строке {count}: {line}'
                    print(valerror)
                    bad_regs.write(valerror + '\n')
                else:
                    ageerror = f'Неправильно указан возвраст в строке {count}: {line}'
                    print(ageerror)
                    bad_regs.write(ageerror + '\n')
            except NotNameError:
                nameerror = f'Неправильно указано имя в строке {count}: {line}'
                print(nameerror)
                bad_regs.write(nameerror + '\n')

            except NotEmailError:
                emailerror = f'Неправильно указана электронная почта в строке {count}: {line}'
                print(emailerror)
                bad_regs.write(emailerror + '\n')
        bad_regs.close()
        good_regs.close()


check_regs('registrations.txt')
