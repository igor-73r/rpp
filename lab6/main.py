from db_init import *

with db:
    db.create_tables([Area, Position, PrecipitationType, Precipitation, Total])
