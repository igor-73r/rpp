from django.db import models


class Area(models.Model):
    width = models.FloatField()
    length = models.FloatField()

    class Meta:
        verbose_name = 'Площадь'
        verbose_name_plural = 'Площадь'


class PrecipitationType(models.Model):
    type = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Тип осадков'
        verbose_name_plural = 'Тип осадков'

class Position(models.Model):
    longitude = models.FloatField()
    latitude = models.FloatField()
    area = models.ForeignKey(Area, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Координаты'
        verbose_name_plural = 'Координаты'

class Precipitation(models.Model):
    amount = models.FloatField()
    type = models.ForeignKey(PrecipitationType, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Осадки'
        verbose_name_plural = 'Осадки'


class Total(models.Model):
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    precipitation = models.ForeignKey(Precipitation, on_delete=models.CASCADE)
    date = models.DateField()

    class Meta:
        verbose_name = 'Общее'
        verbose_name_plural = 'Общее'

