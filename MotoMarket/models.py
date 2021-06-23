from django.db import models
import base64


class Country(models.Model):
    name = models.CharField(max_length=125, blank=True)

    def __str__(self):
        return self.name


class Moto(models.Model):
    brand = models.CharField(max_length=255)
    motomodel = models.CharField(max_length=255)
    engine = models.IntegerField()
    mileage = models.IntegerField()
    comment = models.TextField(blank=True)
    image = models.TextField(blank=True)
    price = models.DecimalField(default=0.00, max_digits=12, decimal_places=2)
    country = models.ForeignKey(to=Country, null=True, on_delete=models.DO_NOTHING)

    class Meta:
        abstract = True
        managed = False

    @property
    def modelname(self):
        return self._meta.object_name

    def __str__(self):
        return f'Марка: {self.brand} | Модель: {self.motomodel} | Объем: {self.engine} '


class Sportbike(Moto):
    track_only = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Sportbikes'


class Cruiser(Moto):
    is_chopper = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Cruisers'


class Enduro(Moto):
    is_roadside = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Enduros'


class Quadro(Moto):
    max_deep = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = 'Quadros'
