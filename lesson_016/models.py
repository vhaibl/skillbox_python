from peewee import *
from playhouse.db_url import connect

db = DatabaseProxy()


class Weather(Model):
    day = DateField(formats='%Y-%m-%d')
    daterus = CharField()
    temperature = CharField()
    condition = CharField()
    wind = CharField()
    humidity = CharField()
    pressure = CharField()
    picture = CharField()

    #

    class Meta:
        database = db
