from peewee import *

db = SqliteDatabase('weather.db')
db_proxy = DatabaseProxy()


class Weather(Model):
    day = DateField(formats='%Y-%m-%d')
    daterus = CharField()
    temperature = CharField()
    condition = CharField()
    wind = CharField()
    humidity = CharField()
    pressure = CharField()
    picture = CharField()

    class Meta:
        database = db_proxy


db_proxy.initialize(db)
# TODO Инициализацию наддо вынести в класс БД
# TODO Кроме того принимать она должна не db, а объект, созданный из db url
# TODO db_url передается в метод connect - так создается объект типа SqliteDatabase
# TODO И уже этот объект, созданный connect-ом надо инициализировать
