from pony.orm import Database, Required, Json

from settings import DB_CONFIG

db = Database()
db.bind(**DB_CONFIG)


class UserState(db.Entity):
    """Состояние пользователя внутри сценария"""
    user_id = Required(str, unique=True)
    scenario_name = Required(str)
    step_name = Required(str)
    context = Required(Json)


class Registration(db.Entity):
    """Заявки на регистрацию"""
    city_from = Required(str)
    city_to = Required(str)
    flight_date = Required(str)
    phone = Required(str)
    quantity = Required(str)
    comment = Required(str)


db.generate_mapping(create_tables=True)
