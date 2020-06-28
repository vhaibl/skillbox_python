from models import Weather, db
from playhouse.db_url import connect

db_url = 'sqlite:///weather.db'
database = connect(db_url)
db.initialize(database)
s_Weather = Weather
s_Weather.create_table()
# TODO Проверяем по дате (указываем перечень остальных данных через defaults для случая, когда запись нужно создать)
xz = s_Weather.get_or_create(day='2020-01-01', defaults={'daterus': '1 Января 2020',
                                                         'temperature': 'Днем 2° Ночью -2°',
                                                         'condition': 'снег', 'wind': '7 м/с',
                                                         'humidity': '999%',
                                                         'pressure': '742 мм',
                                                         'picture': 'python_snippets\external_data\weather_img\snow.jpg'})
print(xz)  # TODO Получаем кортеж с записью и ответом
# (True - если запись была создана, False - если такая запись уже есть)
if xz[1] is False:  # TODO Если есть - обновляем
    print('upd')
    # TODO Указываем перечень нужных данных
    s = Weather.update(day='2020-01-01', daterus='1 Января 2020',
                       temperature='Днем 2° Ночью -2°',
                       condition='снег', wind='7 м/с',
                       humidity='999%',
                       pressure='742 мм', picture='python_snippets\external_data\weather_img\snow.jpg') \
        .where(Weather.id == xz[0].id)  # TODO И уточняем какую запись надо заменить
    s.execute()  # TODO Подтверждаем обновление
