from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    """Category Model"""
    category = models.CharField(max_length=50, verbose_name="category")

    class Meta:
        verbose_name = "category"


class Locate(models.Model):
    """Location Model"""
    ru_locate = models.CharField(max_length=50)
    us_locate = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "locate"
