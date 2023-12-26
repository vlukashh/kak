from django.db import models
from django.contrib.auth.models import AbstractUser



class AdvUser(AbstractUser):
    photo = models.ImageField(verbose_name="Фото", blank=False, upload_to='user/')

class Product(models.Model):
    name = models.CharField(verbose_name="Название товара", max_length=150)
    description = models.CharField(verbose_name="Описание", max_length=150)
    image = models.ImageField(verbose_name="Фотография",  upload_to='images/', blank=False)

class App(models.Model):
    user = models.ForeignKey(AdvUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
