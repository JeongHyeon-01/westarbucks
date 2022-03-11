from django.db import models


# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length=45)

    class Meta:
        db_table = 'product_menu'


class Category(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    name = models.CharField(max_length=45)

    class Meta:
        db_table = 'product_categories'


class Drink(models.Model):
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    korean_name = models.CharField(max_length=45)
    english_name = models.CharField(max_length=45)
    description = models.TextField()
    allergy = models.ManyToManyField('Allergy','self')

    class Meta:
        db_table = 'product_drink'

class Nutritions(models.Model):
    drink = models.ForeignKey('Drink', on_delete=models.CASCADE)
    size_id = models.ForeignKey('Sizes', on_delete=models.CASCADE)
    one_serving_kcal= models.DecimalField(decimal_places=1,max_digits=2)
    sodium_mg = models.DecimalField(decimal_places=2,max_digits=2)
    saturated_fat_g = models.DecimalField(decimal_places=2,max_digits=2)
    sugars_g = models.DecimalField(decimal_places=2,max_digits=2)
    protein_g = models.DecimalField(decimal_places=2,max_digits=2)
    caffeine_mg = models.DecimalField(decimal_places=2,max_digits=2)

    class Meta:
        db_table = 'product_nutritions'
        

class Allergy(models.Model):
    name = models.CharField(max_length=45)

    class Meta:
        db_table = 'product_allergy'

class Images(models.Model):
    img_url = models.CharField(max_length=2000)
    drink = models.ForeignKey('Drink', on_delete=models.CASCADE)

    class Meta:
        db_table = 'product_images'


class Sizes(models.Model):
    name = models.CharField(max_length=45)
    size_ml = models.CharField(max_length=45, null=True)
    size_fluid_ounce = models.CharField(max_length=45, null=True)

    class Meta:
        db_table = 'product_size'
        