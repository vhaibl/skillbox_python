# -*- coding: utf-8 -*-

# Подземелье было выкопано ящеро-подобными монстрами рядом с аномальной рекой, постоянно выходящей из берегов.
# Из-за этого подземелье регулярно затапливается, монстры выживают, но не герои, рискнувшие спуститься к ним в поисках
# приключений.
# Почуяв безнаказанность, ящеры начали совершать набеги на ближайшие деревни. На защиту всех деревень не хватило
# солдат и вас, как известного в этих краях героя, наняли для их спасения.
#
# Карта подземелья представляет собой json-файл под названием rpg.json. Каждая локация в лабиринте описывается объектом,
# в котором находится единственный ключ с названием, соответствующем формату "Location_<N>_tm<T>",
# где N - это номер локации (целое число), а T (вещественное число) - это время,
# которое необходимо для перехода в эту локацию. Например, если игрок заходит в локацию "Location_8_tm30000",
# то он тратит на это 30000 секунд.
# По данному ключу находится список, который содержит в себе строки с описанием монстров а также другие локации.
# Описание монстра представляет собой строку в формате "Mob_exp<K>_tm<M>", где K (целое число) - это количество опыта,
# которое получает игрок, уничтожив данного монстра, а M (вещественное число) - это время,
# которое потратит игрок для уничтожения данного монстра.
# Например, уничтожив монстра "Boss_exp10_tm20", игрок потратит 20 секунд и получит 10 единиц опыта.
# Гарантируется, что в начале пути будет две локации и один монстр
# (то есть в коренном json-объекте содержится список, содержащий два json-объекта, одного монстра и ничего больше).
#
# На прохождение игры игроку дается 123456.0987654321 секунд.
# Цель игры: за отведенное время найти выход ("Hatch")
#
# По мере прохождения вглубь подземелья, оно начинает затапливаться, поэтому
# в каждую локацию можно попасть только один раз,
# и выйти из нее нельзя (то есть двигаться можно только вперед).
#
# Чтобы открыть люк ("Hatch") и выбраться через него на поверхность, нужно иметь не менее 280 очков опыта.
# Если до открытия люка время заканчивается - герой задыхается и умирает, воскрешаясь перед входом в подземелье,
# готовый к следующей попытке (игра начинается заново).
#
# Гарантируется, что искомый путь только один, и будьте аккуратны в рассчетах!
# При неправильном использовании библиотеки decimal человек, играющий с вашим скриптом рискует никогда не найти путь.
#
# Также, при каждом ходе игрока ваш скрипт должен запоминать следущую информацию:
# - текущую локацию
# - текущее количество опыта
# - текущие дату и время (для этого используйте библиотеку datetime)
# После успешного или неуспешного завершения игры вам необходимо записать
# всю собранную информацию в csv файл dungeon.csv.
# Названия столбцов для csv файла: current_location, current_experience, current_date
#
#
# Пример взаимодействия с игроком:
#
# Вы находитесь в Location_0_tm0
# У вас 0 опыта и осталось 123456.0987654321 секунд до наводнения
# Прошло времени: 00:00
#
# Внутри вы видите:
# — Вход в локацию: Location_1_tm1040
# — Вход в локацию: Location_2_tm123456
# Выберите действие:
# 1.Атаковать монстра
# 2.Перейти в другую локацию
# 3.Сдаться и выйти из игры
#
# Вы выбрали переход в локацию Location_2_tm1234567890
#
# Вы находитесь в Location_2_tm1234567890
# У вас 0 опыта и осталось 0.0987654321 секунд до наводнения
# Прошло времени: 20:00
#
# Внутри вы видите:
# — Монстра Mob_exp10_tm10
# — Вход в локацию: Location_3_tm55500
# — Вход в локацию: Location_4_tm66600
# Выберите действие:
# 1.Атаковать монстра
# 2.Перейти в другую локацию
# 3.Сдаться и выйти из игры
#
# Вы выбрали сражаться с монстром
#
# Вы находитесь в Location_2_tm0
# У вас 10 опыта и осталось -9.9012345679 секунд до наводнения
#
# Вы не успели открыть люк!!! НАВОДНЕНИЕ!!! Алярм!
#
# У вас темнеет в глазах... прощай, принцесса...
# Но что это?! Вы воскресли у входа в пещеру... Не зря матушка дала вам оберег :)
# Ну, на этот-то раз у вас все получится! Трепещите, монстры!
# Вы осторожно входите в пещеру... (текст умирания/воскрешения можно придумать свой ;)
#
# Вы находитесь в Location_0_tm0
# У вас 0 опыта и осталось 123456.0987654321 секунд до наводнения
# Прошло уже 0:00:00
# Внутри вы видите:
#  ...
#  ...
#
# и так далее...
import csv
import datetime
import json
import re
from decimal import *
from termcolor import cprint

remaining_time = '123456.0987654321'
remaining_time = Decimal(remaining_time)
current_experience = 0
field_names = ['current_location', 'current_experience', 'current_date']

with open("rpg.json", "r") as read_file:
    loaded_json_file = json.load(read_file)

# TODO Мне кажется над структурой программы всё же стоит ещё поработать.
# TODO Создайте три класса - Карта, Герой, Игра
# TODO К карте отнесите методы - загрузка карты, смена локации и анализ локации
# TODO К герою методы получения опыта и учет затраченного времени (можно сделать что-то вроде is_alive() метода
# TODO который вернет True, если герой ещё жив (осталось времени больше 0))
# TODO Игра же будет инициализировать объекты других классов и запускать их методы
# TODO + собирать указания пользователя и вызывать выбранные им методы
# TODO ВАЖНО! Каждый ввод пользователя проверять!
def action_list():
    global act, current_location
    print(
        f"Вы находитесь в локации {name1}. \nВремени осталось {remaining_time}, опыта: {current_experience} \nВы можете:")
    current_location = name1
    z = 0
    act = {}

    for line in current:
        if type(line) is dict:
            for loc in line:
                z += 1

                act[str(z)] = loc
                hatch_or_loc = (z, " - Перейти в локацию", act[str(z)])
                if 'atch' in hatch_or_loc[2]:
                    print(z, " - ОТКРЫТЬ ЛЮК", act[str(z)])
                else:
                    print(z, " - Перейти в локацию", act[str(z)])
        elif 'Mob' in line:
            z += 1
            act[str(z)] = line
            print(z, "- Атаковать монстра", act[str(z)])
        elif 'Boss' in line:
            z += 1
            act[str(z)] = line
            print(z, "- Напасть на БОССА", act[str(z)])
    z += 1
    act[str(z)] = 'exit'
    print(z, '- Выход')


with open('game_log.csv', 'w', encoding='utf-8') as gamelog:
    writer = csv.writer(gamelog, dialect='excel')  # <_csv.writer object at 0x03B0AD80>
    writer.writerow(field_names)

name1 = 'Location_0_tm0'
current = loaded_json_file[name1]
prev = current
mob_exp = r'exp(\d{1,5})_'
find_time = r'tm([\d\.\d]+)'
add_exp = 0
nowis = None
while remaining_time > 0:

    action_list()
    action = None
    action = input("Ваши действия >  ")
    while action not in act:  # проверяем корректность ввода
        print('Вы ввели некорректный номер!')
        action = input("Ваши действия > ")

    if 'Mob' in act[action]:
        add_exp = re.findall(mob_exp, act[action])
        add_time = re.findall(find_time, act[action])
        current_experience += int(add_exp[0])
        remaining_time -= Decimal(add_time[0])
        current.remove(str(act[action]))
        cprint(f'Вы убили монстра {act[action]}! Опыта получено {add_exp[0]}, времени потрачено {add_time[0]}',
               color='green')
    if 'Boss' in act[action]:
        add_exp = re.findall(mob_exp, act[action])
        add_time = re.findall(find_time, act[action])
        current_experience += int(add_exp[0])
        remaining_time -= Decimal(add_time[0])
        current.remove(str(act[action]))
        cprint(f'Вы убили БОССА {act[action]}! Опыта получено {add_exp[0]}, времени потрачено {add_time[0]}',
               color='red')
    if 'Hatch' in act[action]:
        # add_exp = re.findall(mob_exp, act[action])
        add_time = re.findall(find_time, act[action])
        print(add_time)
        current_experience += int(add_exp[0])
        # remaining_time -= Decimal(add_time[0])
        print(current_experience, Decimal(remaining_time), Decimal(add_time[0]))
        # TODO Почему по итогу результат выводится такой? 320 159.0987654321 159.098765432
        # TODO 1) опыта должно быть 280 - за выход Hatch опыт не начисляется
        if current_experience >= 200 and Decimal(remaining_time) >= Decimal(add_time[0]):
            # TODO По условию опыта должно было быть больше 280
            remaining_time = Decimal(remaining_time) - Decimal(add_time[0])
            # current.remove(str(act[action]))

            cprint(f'Вы выбрались из подземелья! Опыта получено {current_experience}, времени осталось '
                   f'{Decimal(remaining_time):.10f}', color='blue')
            break
        else:
            remaining_time -= Decimal(add_time[0])
            cprint(f'У вас не хватило опыта, чтобы открыть люк', color='blue')
            pass
    if 'Location' in act[action]:
        add_time = re.findall(find_time, act[action])
        remaining_time -= Decimal(add_time[0])
        name1 = act[action]
        cprint(f'Вы переместились в локацию {act[action]}. Времени потрачено {add_time[0]}', color='green')

        for x, y in enumerate(current):
            if act[action] in y:
                current = current[x][act[action]]

    if 'exit' in act[action]:
        print("Вы решили сдаться и погибли")
        break

    if len(current) == 0 or remaining_time <= 0:
        if len(current) == 0:
            cprint('ТУПИК, НАЗАД ДОРОГИ НЕТ', color='cyan')
        if remaining_time <= 0:
            cprint('ЗАКОНЧИЛОСЬ ВРЕМЯ', color='cyan')

        cprint(
            'У вас темнеет в глазах... прощай, принцесса...\n Но что это?! Вы воскресли у входа в пещеру... '
            'Не зря матушка дала вам оберег :)\n Ну, на этот-то раз у вас все получится! Трепещите, монстры!\n '
            'Вы осторожно входите в пещеру...\n', color='blue')
        with open("rpg.json", "r") as read_file:
            loaded_json_file = json.load(read_file)
        remaining_time = '123456.0987654321'
        remaining_time = Decimal(remaining_time)
        current_experience = 0
        name1 = 'Location_0_tm0'
        current = loaded_json_file[name1]

    now = datetime.datetime.now()
    current_time = now.strftime('%H:%M:%S')
    fields = (current_location, str(current_experience), current_time)

    with open('game_log.csv', 'a', encoding='utf-8') as gamelog:
        writer = csv.writer(gamelog, dialect='excel')  # <_csv.writer object at 0x03B0AD80>
        writer.writerow(fields)

