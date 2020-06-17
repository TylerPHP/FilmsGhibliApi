from django.db import models


# Create your models here.
class Locate(models.Model):
    """Модель локализации"""
    title = models.CharField(max_length=50)
    director = models.CharField(max_length=50)
    producer = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Имена и название фильмов на русском"
        verbose_name_plural = "Имена и название фильмов на русском"
