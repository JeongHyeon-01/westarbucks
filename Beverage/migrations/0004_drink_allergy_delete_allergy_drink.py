# Generated by Django 4.0.3 on 2022-03-11 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Beverage', '0003_remove_drink_allergy_allergy_drink'),
    ]

    operations = [
        migrations.AddField(
            model_name='drink',
            name='allergy',
            field=models.ManyToManyField(related_name='self', to='Beverage.allergy'),
        ),
        migrations.DeleteModel(
            name='allergy_drink',
        ),
    ]
