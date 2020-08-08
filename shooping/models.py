from django.db import models

class City(models.Model):
    """Города"""
    title = models.CharField("Город", max_length=150)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Город"
        verbose_name_plural = "Города"

class Street(models.Model):
    """Улицы"""
    name = models.CharField("Улица", max_length=150)
    city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name="город")
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Улица"
        verbose_name_plural = "Улицы"


class Shoop(models.Model):
    """Магазины"""
    title = models.CharField("Название магазина", max_length=150)
    city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name="город")
    street = models.ForeignKey(Street, on_delete=models.CASCADE, verbose_name="Улица")
    home = models.SmallIntegerField("Дом")
    open_time = models.TimeField(auto_now=False, auto_now_add=False)
    close_time = models.TimeField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.title

    def create(self, validated_data):
        return Shoop.objects.create(**validated_data)

    class Meta:
        verbose_name = "Магазин"
        verbose_name_plural = "Магазины"

