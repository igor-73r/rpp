from peewee import *

# Подключение к базе данных
db = SqliteDatabase('my_database.db')


# Определение моделей
class Standard(Model):
    id = PrimaryKeyField(unique=True)

    class Meta:
        database = db


class Area(Standard):
    width = FloatField()
    length = FloatField()

    class Meta:
        db_table = "areas"


class Position(Standard):
    longitude = FloatField()
    latitude = FloatField()
    area = ForeignKeyField(Area)

    class Meta:
        db_table = "positions"


class PrecipitationType(Standard):
    type = CharField()

    class Meta:
        db_table = "precipitation types"


class Precipitation(Standard):
    amount = FloatField()
    type = ForeignKeyField(PrecipitationType)

    class Meta:
        db_table = "precipitations"


class Total(Standard):
    position = ForeignKeyField(Position)
    precipitation = ForeignKeyField(Precipitation)
    date = DateField()


TABLES = [Area, Position, PrecipitationType, Precipitation, Total]
db.create_tables(TABLES)
