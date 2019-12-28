# -*- coding: utf-8 -*-

# (цикл while)

# Ежемесячная стипендия студента составляет educational_grant руб., а расходы на проживание превышают стипендию
# и составляют expenses руб. в месяц. Рост цен ежемесячно увеличивает расходы на 3%, кроме первого месяца
# Составьте программу расчета суммы денег, которую необходимо единовременно попросить у родителей,
# чтобы можно было прожить учебный год (10 месяцев), используя только эти деньги и стипендию.
# Формат вывода:
#   Студенту надо попросить ХХХ.ХХ рублей

educational_grant, expenses = 10000, 12000
month = 0  # Вы забыли тут поправить единицу на 0 :)
sum_expenses = 0
while month < 10:  # Поэтому здесь было 9 итераций вместо 10
    sum_expenses += expenses
    expenses = expenses * 1.03
    month += 1
from_parents = sum_expenses - (educational_grant * month)
print('Студенту надо попросить', round(from_parents, 0), 'рублей')

#зачет!