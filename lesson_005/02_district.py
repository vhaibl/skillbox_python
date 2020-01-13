# -*- coding: utf-8 -*-
# Составить список всех живущих на районе и Вывести на консоль через запятую
# Формат вывода: На районе живут ...
# подсказка: для вывода элементов списка через запятую можно использовать функцию строки .join()
# https://docs.python.org/3/library/stdtypes.html#str.join
from district.central_street.house1.room1 import folks as ch1r1
from district.central_street.house1.room2 import folks as ch1r2
from district.central_street.house2.room1 import folks as ch2r1
from district.central_street.house2.room2 import folks as ch2r2
from district.soviet_street.house1.room1 import folks as sh1r1
from district.soviet_street.house1.room2 import folks as sh1r2
from district.soviet_street.house2.room1 import folks as sh2r1
from district.soviet_street.house2.room2 import folks as sh2r2

residents = ch1r1 + ch1r2 + ch2r1 + ch2r2 + sh1r1 + sh1r2 + sh2r1 + sh2r2
print(', '.join(residents))
#зачет!