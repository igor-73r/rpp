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


def get_fields(table):
    return table._meta.fields.keys()


def table_getter(table):
    match table:
        case "Area":
            return Area
        case "Position":
            return Position
        case "Precipitation":
            return Precipitation
        case "PrecipitationType":
            return PrecipitationType
        case "Total":
            return Total


TABLES = [Area, Position, PrecipitationType, Precipitation, Total]
db.create_tables(TABLES)
