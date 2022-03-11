from multiprocessing.spawn import old_main_modules
from tkinter import CASCADE
from unicodedata import category
from django.db import models
from django.forms import CharField

# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length=45)

    class Meta:
        db_table = 'menu'


class Category(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    name = models.CharField(max_length=45)

    class Meta:
        db_table = 'categories'


class Drink(models.Model):
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    korean_name = models.CharField(max_length=45)
    english_name = models.CharField(max_length=45)
    description = models.TextField()
    arrergy = models.ManyToManyField('Allergy')

    class Meta:
        db_table = 'drink'

class Nutritions(models.Model):
    drink = models.ForeignKey('Drink', on_delete=models.CASCADE)
    one_serving_kcal= models.DecimalField(decimal_places=1,max_digits=2)
    sodium_mg = models.DecimalField(decimal_places=2,max_digits=2)
    saturated_fat_g = models.DecimalField(decimal_places=2,max_digits=2)
    sugars_g = models.DecimalField(decimal_places=2,max_digits=2)
    protein_g = models.DecimalField(decimal_places=2,max_digits=2)
    caffeine_mg = models.DecimalField(decimal_places=2,max_digits=2)

    class Meta:
        db_table = 'nutritions'
        

class Allergy(models.Model):
    name = models.CharField(max_length=45)

    class Meta:
        db_table = 'allergy'

class Images(models.Model):
    img_url = models.CharField(max_length=2000)
    drink = models.ForeignKey('Drink', on_delete=models.CASCADE)

    class Meta:
        db_table = 'images'